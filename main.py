from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import functions

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

    driver = functions.login_intomark()

    driver = functions.search_word_similar(driver, mark1, class1, group1)

    results=functions.results_count(driver)

    trademarks=functions.get_trademarks(driver)

    driver = functions.logout_intomark(driver)

    return {"mark1": mark1, "class1": class1, "group1":group1, "results":results }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
