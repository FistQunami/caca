from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi import FastAPI

import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Привет"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Button Example</title>
        </head>
        <body>
            <h1>Hello World!</h1>
            <button onclick="alert('Button Clicked!')">Click Me</button>
        </body>
    </html>
    """

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8000)