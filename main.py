import json
import os

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


SHOW_REPL = os.getenv("SHOW_REPL", True)

@app.get("/")
async def pyscript_root(request: Request):

    dataset = {
        "foo": "bar",
        "bar": "baz",
    }

    return templates.TemplateResponse(
        "pyscript.html",
        {
            "request": request,
            "repl": int(SHOW_REPL),
            "packages": ["requests", "ssl"],
            "data": json.dumps(dataset),
        },
    )
