import uvicorn
import contexts.database
from fastapi import FastAPI
from routes import router

app = FastAPI()
app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
