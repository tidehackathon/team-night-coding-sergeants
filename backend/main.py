import uvicorn
from fastapi import FastAPI

from backend.routes import register_routes

app = FastAPI(title='Fake News Analyzer')
register_routes(app)

@app.get('/')
async def root():
    return {
        'message': 'server working'
    }

if __name__ == '__main__':
    uvicorn.run(app, port=8080)