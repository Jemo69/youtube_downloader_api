from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from src.settings import TORTOISE_ORM
from src.router.video import router as video_router


app = FastAPI()

app.include_router(video_router, prefix="/video")


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
