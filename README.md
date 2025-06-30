# 🚀 Hello FastAPI CI/CD on Google Cloud

This project demonstrates a complete CI/CD pipeline for a FastAPI web API using:

- Google Cloud Run (serverless deployment)
- Artifact Registry (Docker image storage)
- GitHub Actions (CI/CD automation)

---

## 📦 What’s Included

- ✅ FastAPI-based JSON API: `{ "status": "ok" }`
- ✅ Dockerized with a multi-stage, secure image
- ✅ Artifact Registry publishing
- ✅ Cloud Run deployment (public URL)
- ✅ CI/CD pipeline with GitHub Actions
- ✅ GCP IAM & security best practices


## 🛠️ Setup Instructions

### 1. Clone the Repository


git clone https://github.com/your-username/hello-fastapi-cloudrun.git
cd hello-fastapi-cloudrun


Enable GCP Services (one-time)
gcloud services enable run.googleapis.com artifactregistry.googleapis.com


Build & Push Manually 


🔄 GitHub Actions CI/CD
CI/CD triggers on each push to main.
It will:
Authenticate to GCP using GCP_SA_KEY secret
Build and push Docker image to Artifact Registry
Deploy new revision to Cloud Run


🔐 IAM Roles Used
Cloud Run Admin
Artifact Registry Writer
Service Account User


💰 Cost Estimate
Resource	Cost (Free Tier)
Cloud Run	Free up to 2M requests/month
Artifact Registry	Free for first 0.5 GB/month
GitHub Actions	Free (2000 minutes/month)
GCP credits	$300 free for 90 days

✅ This project stays well within the free tier



🔗 Live Demo
Public URL: https://hello-api-17486051359.us-central1.run.app/
Swagger Docs: https://hello-api-17486051359.us-central1.run.app/docs