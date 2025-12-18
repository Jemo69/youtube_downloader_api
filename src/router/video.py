from fastapi import APIRouter
from pydantic import BaseModel
from pytubefix import YouTube
from src.models import Video

router = APIRouter()

class VideoModel(BaseModel):
   url: str

@router.post("/posts/")
async def get_video(video: VideoModel):
    yt = YouTube(video.url)
    title = yt.title

    video_stream = yt.streams.get_highest_resolution()

    video_stream.download()
    video_data = Video(title=title, url=video.url)
    await video_data.save() 
    return {"message": "Video downloaded successfully"}

 

