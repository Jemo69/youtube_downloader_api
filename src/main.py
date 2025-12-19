from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from src.settings import TORTOISE_ORM
from src.router.video import router as video_router
from src.router.playlist import router as playlist_router
from src.router.user import router as user_router


app = FastAPI()

app.include_router(video_router, prefix="/video")
app.include_router(user_router, prefix="/user")
app.include_router(playlist_router, prefix="/playlist")


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
)
