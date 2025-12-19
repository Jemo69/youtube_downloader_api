from fastapi import APIRouter, Depends , Request
import concurrent.futures
import random
import os
from string import ascii_letters
from pydantic import BaseModel
from pytubefix import Playlist
from src.utils import verify_token
from src.models import Playlist as PlaylistData, User

router = APIRouter()


class PlaylistModel(BaseModel):
    url: str


def process_video(video, user_instance):
    yt = video
    title = yt.title

    video_stream = yt.streams.get_highest_resolution()

    random_name = "".join(random.choice(ascii_letters) for _ in range(10))
    custom_name = f"{user_instance.name}_{random_name}.mp4"
    video_stream.download(output_path=f"./uploads/{user_instance.name}/", filename=custom_name)


@router.post("/posts/")
async def get_playlist(playlist: PlaylistModel,request: Request, token_decoded: dict = Depends(verify_token)):
    token = request.headers.get("Authorization")
    if token:
        if token.startswith("Bearer "):
            token = token[7:]
        token_decoded = verify_token(token)
    
    # Process playlist
    yt = Playlist(playlist.url)
    title = yt.title
    user_instance = await User.get(id=token_decoded["user_id"])

    # Ensure directory exists
    os.makedirs(f"./uploads/{user_instance.name}/", exist_ok=True)

    # Process videos concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_video, video, user_instance) for video in yt.videos]
        concurrent.futures.wait(futures)

    # Save playlist data
    playlist_data = PlaylistData(user=user_instance, title=title, url=playlist.url)
    await playlist_data.save()

    return {"message": "Playlist processed successfully", "title": title}
