from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse #インポート

### コードいろいろ... ###
app = FastAPI()

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>こんにちは</title>
        </head>
        <body>
            <h1>こんにちは</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)



@app.get("/")
async def root():
    return {"message": "Hello Worldooooooooooooooooooooo"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():

    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    return omikuji_list[random.randrange(10)]



