from fastapi import APIRouter , Depends , Request
import random
from string import ascii_letters
from pydantic import BaseModel
from pytubefix import YouTube
from src.utils import verify_token
from fastapi.responses import FileResponse
from src.models import Video , User

router = APIRouter()

class VideoModel(BaseModel):
   user : int
   url: str
@router.post("/posts/")
async def get_video(video: VideoModel , request: Request, token_decoded: dict = Depends(verify_token))->FileResponse:
    yt = YouTube(video.url)
    token  = request.headers.get("Authorization")
    if token:
        if token.startswith("Bearer "):
            token = token[7:]
        token_decoded = verify_token(token)
    user_instance = await User.get(id=token_decoded['user_id'])
    title = yt.title

    video_stream = yt.streams.get_highest_resolution()

    random_name = ''.join(random.choice(ascii_letters) for _ in range(10))
    custom_name = f"{user_instance.name}_{random_name}.mp4"
    video_stream.download(output_path=f"./uploads/{user_instance.name}/" , filename=custom_name)
    video_data = Video(user=user_instance,title=title, url=video.url)

    final_custom_name = f"{user_instance.name}_{random_name}"
    await video_data.save()
    return  FileResponse(f"./uploads/{user_instance.name}/{final_custom_name}.mp4")
@router.get("/videos/")

async def get_videos(request : Request, token_decoded: dict = Depends(verify_token)) :
    token = request.headers.get("Authorization")
    if token:
        if token.startswith("Bearer "):
            token = token[7:]
        token_decoded = verify_token(token)
    user_instance = await User.get(id=token_decoded['user_id'])
    videos = await Video.filter(user=user_instance).all()
    return {"message": "Videos fetched successfully" , "videos": videos}


