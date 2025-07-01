 **🚀 Hello FastAPI CI/CD on Google Cloud**

This project demonstrates a complete CI/CD pipeline for a FastAPI web API using:

- **Google Cloud Run** (serverless deployment)
- **Artifact Registry** (Docker image storage)
- **GitHub Actions** (CI/CD automation)
- **Trivy** (security scanning)



 📦 What’s Included

- ✅ FastAPI-based JSON API: `{ "status": "ok" }`
- ✅ Dockerized using a multi-stage, non-root image
- ✅ Trivy scan for vulnerabilities during CI
- ✅ Docker image published to Artifact Registry
- ✅ Deployed to Cloud Run (fully managed)
- ✅ CI/CD automated via GitHub Actions
- ✅ IAM roles follow least-privilege principle


🛠️ Setup Instructions

1. Clone the Repository

git clone https://github.com/farhan92cr/hello-fastapi-cloudrun.git
cd hello-fastapi-cloudrun



2. Enable Required GCP Services (one-time) 
gcloud services enable run.googleapis.com artifactregistry.googleapis.com


3. Manual Build & Push (Optional)
docker build -t hello-api .
docker tag hello-api us-central1-docker.pkg.dev/<YOUR_PROJECT_ID>/hello-api/hello-api:latest
docker push us-central1-docker.pkg.dev/<YOUR_PROJECT_ID>/hello-api/hello-api:latest


🔄 GitHub Actions CI/CD
CI/CD is triggered on each push to the main branch.

Steps:

✅ Authenticate to GCP using GCP_SA_KEY GitHub secret

🐳 Build and tag Docker image

🛡️ Run Trivy vulnerability scan

📤 Push image to Artifact Registry

🚀 Deploy latest revision to Cloud Run



🔐 IAM Roles Used
The service account has the following least-privilege IAM roles:

Cloud Run Admin
Artifact Registry Writer
Service Account User



🔎 Security: Trivy Vulnerability Scanning
This pipeline includes a Trivy security scan step before pushing the image.
It scans for:

OS-level vulnerabilities (CVEs)
Python package vulnerabilities
Only HIGH and CRITICAL issues are reported
📄 Output is shown in the GitHub Actions logs.


📊 Cost Estimate (Free Tier)
Resource	Free Tier Limit
Cloud Run	2 million requests/month
Artifact Registry	First 0.5 GB storage/month
GitHub Actions	2,000 minutes/month
GCP Credits	$300 free for 90 days (new users)
✅ This project stays fully within the free tier


🔗 Live Demo
Public URL: https://hello-api-17486051359.us-central1.run.app/
Swagger Docs: https://hello-api-17486051359.us-central1.run.app/docs

