from fastapi import HTTPException, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

class InvalidYoutubeURL(HTTPException):
    def __init__(self, request: Request):
        self.response = templates.TemplateResponse(
            "pages/home.html",
            {
                "request": request,
                "video_id": None,
                
            },
        )
        super().__init__(status_code=400, detail="Invalid Youtube URL")