from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/search-form")
async def search_form(mark1: str = Form(),
                      mark2: str = Form(None),
                      mark3: str = Form(None),
                      mark4: str = Form(None),
                      class1: int = Form(),
                      group1: str = Form(),
                      class2: int = Form(None),
                      group2: str = Form(None),
                      class3: int = Form(None),
                      group3: str = Form(None)):
    return {"mark1": mark1, "class1": class1, "group1":group1 }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
