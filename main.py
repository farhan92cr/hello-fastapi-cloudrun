from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "DEMO VIDEO" }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
