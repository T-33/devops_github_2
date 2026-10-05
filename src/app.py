from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="DevOps Study App")

@app.get("/health", status_code=200)
def health_check():
    return {"status": "ok"}

@app.get("/", response_class=HTMLResponse)
def get_home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>FastAPI DevOps App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f4f6f8;
            }
            .card {
                background: white;
                padding: 2rem;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                text-align: center;
            }
            h1 { color: #007acc; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 DevOps Demo App</h1>
            <p>Served via FastAPI inside a multi-stage Docker container.</p>
        </div>
    </body>
    </html>
    """
