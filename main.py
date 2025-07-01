from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": " changes for DEmo" }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
