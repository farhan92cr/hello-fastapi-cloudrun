from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", " vulnerability scanning with Trivy added" : " " }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
