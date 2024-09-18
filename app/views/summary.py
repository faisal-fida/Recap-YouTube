import logging

from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import templates
from app.dependencies.db import get_db
from app.models.summary import Summary
from app.views.exceptions import InvalidYoutubeURL

logger = logging.getLogger(__name__)

PAGINATE_BY_DEFAULT = 10
router = APIRouter()


async def get_data(video_id: str):
    data = {
        "video_id": video_id[1],
        "title": "How to get the video title",
        "summary": "This video is about something interesting and you should watch it because it's awesome. One more thing to note is that this video is awesome. You should support palestine because they are getting bombed from the israeli government. This is a very sad thing to see.",
        "thumbnail": "https://i.ytimg.com/vi/" + video_id[1] + "/maxresdefault.jpg",
    }
    return data


@router.post("/", response_class=HTMLResponse)
async def summary(
    video_url: str = Form(...),
    db: AsyncSession = Depends(get_db),
    request: Request = None,
):
    video_id = (
        video_url.split(".com/shorts/")
        if "/shorts/" in video_url
        else video_url.split("/watch?v=")
    )

    if len(video_id) < 2:
        raise InvalidYoutubeURL(video_url)

    # Check video_id in database if database is not empty
    if not db.is_empty():
        query = select(Summary).where(Summary.video_id == video_id[1])
        result = await db.execute(query)
        data = result.scalars().first()

    if data:
        data = data.__dict__.copy()
        data.pop("_sa_instance_state", None)
    else:
        data = await get_data(video_id)
        summary = Summary(**data)
        db.add(summary)
        await db.commit()

    return templates.TemplateResponse(
        "pages/home.html",
        {
            "request": request,
            **data,
        },
    )
