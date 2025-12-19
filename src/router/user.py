from fastapi import APIRouter, BackgroundTasks, Response, status
import os
from src.utils import send_email
from pydantic import BaseModel, EmailStr
from tortoise.exceptions import DoesNotExist, IntegrityError
from string import ascii_letters, digits, punctuation
from dotenv import load_dotenv

from src.models import User
import bcrypt
import random
import jwt
from datetime import datetime, timedelta
load_dotenv()

router = APIRouter()


class UserModel(BaseModel):
    name: str
    user_email: EmailStr
    password: str


class ForgotPasswordModel(BaseModel):
    user_email: str | None = None
    new_password: str | None = None


@router.post("/registers/")
async def create_user(user: UserModel, response: Response):
    try:
        password_hash = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
        user_data = User(name=user.name, email=user.user_email, password=password_hash)
        await user_data.save()

        payload = {
                "user_id": user_data.id,
                "email": user_data.email,
                "exp": datetime.utcnow()
                + timedelta(hours=1),  # Token expires in 1 hour
            }
        token = jwt.encode(payload, os.getenv('JWT_SECRET_KEY'), algorithm="HS256")
        response.headers["Authorization"] = f"Bearer {token}"
        response.status_code = status.HTTP_201_CREATED
        return {"message": "User created successfully" , "token": token}
    except IntegrityError :
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "Email already exists", "status_code": 400}
    except Exception as e:
        print(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": str(e), "status_code": 400}


@router.post("/login/")
async def login_user(user: UserModel , response: Response):
    try:
        user_data = await User.get(email=user.user_email)
        if bcrypt.checkpw(
            user.password.encode("utf-8"), user_data.password.encode("utf-8")
        ):
            # Generate JWT token
            payload = {
                "user_id": user_data.id,
                "email": user_data.email,
                "exp": datetime.utcnow()
                + timedelta(hours=1),  # Token expires in 1 hour
            }
            token = jwt.encode(payload, os.getenv('JWT_SECRET_KEY'), algorithm="HS256")

            response.headers["Authorization"] = f"Bearer {token}"

            return {"message": "Login successful", "token": token}
        else:
            return {"message": "Invalid credentials"}
    except DoesNotExist:
        return {"message": "User not found"}


@router.post("/forgot-password/")
# this function is called but hte user and it send an email with unique id and a link to reset the password
async def forgot_password(
    forgot_password: ForgotPasswordModel, background_tasks: BackgroundTasks
):
    if forgot_password.user_email:
        user_data = await User.get(email=forgot_password.user_email)
        if user_data:
            password = "".join(
                random.choice(ascii_letters + digits + punctuation) for _ in range(13)
            )
            password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            user_data.password = password_hash
            background_tasks.add_task(
                send_email,
                forgot_password.user_email,
                "Password Reset",
                f"Your password has been reset successfully {password}",
            )

            await user_data.save()

            return {"message": "Password reset successfully", "password": password}
        else:
            return {"message": "User not found"}
    else:
        return {"message": "Email not provided"}


@router.post("/users/")
async def get_user():
    user_data = await User.all()
    print(user_data)
    return {"message": "User fetched successfully", "users": user_data}
