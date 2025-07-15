#from fastapi import FastAPI
#app = FastAPI()

#@app.get("/")
#def read_root():
 #   return {"status": "Video DEMO" }

#@app.get("/health")
#def health_check():
 #   return {"status": "healthy"}

from fastapi import FastAPI
import logging

# ✅ Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("hello-fastapi")

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("📥 GET request received on '/' endpoint")
    return {"status": "WEll come to Video DEMO "}

@app.get("/health")
def health_check():
    logger.info("💚 Health check passed")
    return {"status": "healthy"}

