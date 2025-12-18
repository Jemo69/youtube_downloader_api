from fastapi import APIRouter , BackgroundTasks
from src.utils import send_email
from pydantic import BaseModel
from string import ascii_letters, digits , punctuation 
from src.models import User
import bcrypt
import email
import random

router = APIRouter()

class UserModel(BaseModel):
   name: str
   email: str
   password: str

class ForgotPasswordModel(BaseModel):
   email: str | None = None
   new_password: str | None = None

@router.post("/users/")
async def create_user(user: UserModel):
    password_hash =  bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    user_data = User(name=user.name, email=user.email, password=password_hash)
    await user_data.save() 
    return {"message": "User created successfully"}

@router.post("/login/")
async def login_user(user: UserModel):
    user_data = await User.get(email=user.email)
    if user and bcrypt.checkpw(user.password.encode('utf-8'), user_data.password.encode('utf-8')):
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid credentials"}
@router.post("forgot-password/")
# this function is called but hte user and it send an email with unique id and a link to reset the password
async def forgot_password(forgot_password: ForgotPasswordModel , background_tasks : BackgroundTasks):
    if forgot_password.email:
        user_data = await User.get(email=forgot_password.email)
        if user_data:
            password = random.choice(ascii_letters + digits + punctuation)
            password_hash =  bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            user_data.password = password_hash
            background_tasks.add_task(send_email, forgot_password.email, "Password Reset", "Your password has been reset successfully")
            await user_data.save()
            
            return {"message": "Password reset successfully"}
        else:
            return {"message": "User not found"}
    else:
        return {"message": "Email not provided"}
