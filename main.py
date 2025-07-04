from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Video DEMO" }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
