from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Demo" }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
