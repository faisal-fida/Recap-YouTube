import logging

from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import templates
from app.dependencies.db import get_db
from app.models.summary import YoutubeSummary
from app.views.exceptions import InvalidYoutubeURL

logger = logging.getLogger(__name__)

PAGINATE_BY_DEFAULT = 10
router = APIRouter()


async def get_ytdata(video_id: str):
    ytdata = {
        "video_id": video_id[1],
        "title": "How to get the video title",
        "summary": "This video is about something interesting and you should watch it because it's awesome. One more thing to note is that this video is awesome. You should support palestine because they are getting bombed from the israeli government. This is a very sad thing to see.",
        "thumbnail": "https://i.ytimg.com/vi/" + video_id[1] + "/maxresdefault.jpg",
    }
    return ytdata


@router.post("/", response_class=HTMLResponse)
async def summary(video_url: str = Form(...), db: AsyncSession = Depends(get_db), request: Request = None):
    video_id = video_url.split(".com/shorts/") if "/shorts/" in video_url else video_url.split("/watch?v=")

    if len(video_id) < 2:
        raise InvalidYoutubeURL(video_url)

    # Check if the video_id is already in the database
    query = select(YoutubeSummary).where(YoutubeSummary.video_id == video_id[1])
    result = await db.execute(query)
    ytdata = result.scalars().first()

    if ytdata:
        ytdata = ytdata.__dict__.copy()
        ytdata.pop("_sa_instance_state", None)
    else:
        ytdata = await get_ytdata(video_id)
        summary = YoutubeSummary(**ytdata)
        db.add(summary)
        await db.commit()
    
    return templates.TemplateResponse(
        "pages/home.html",
        {
            "request": request,
            **ytdata,
        },
    )