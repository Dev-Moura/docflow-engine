from fastapi import FastAPI

app = FastAPI(
    title="Docflow engine",
    version="1.0.0"
)

@app.get("/")
async def root():

    return {
        "message": "Docflow Engine runnig"
        }