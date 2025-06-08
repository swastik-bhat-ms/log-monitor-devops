# 🔍 Log Monitor DevOps Project

This project demonstrates a modern DevOps pipeline using Python, Docker, GitHub Actions, and Kubernetes. It simulates log generation and monitoring in real-time and automates the full CI/CD pipeline using GitHub Container Registry (GHCR) and Kubernetes deployments.

## 📦 Components

- **Log Generator**: Simulates application logs.
- **Log Monitor**: Scans logs for keywords like `error`, `failed`, `critical`.
- **GitHub Actions: Automates Docker image builds, pushes to GHCR, and deploys to Kubernetes.
- **Kubernetes: Manages containerized application deployments.
- **Docker & Docker Compose**: Containerizes the entire setup.

## 🛠 How It Works

Log Generator (log-generator image):
Periodically writes simulated logs into a file (sample.log).
Log Monitor (log-monitor image):
Continuously reads the same file and prints alerts for specific keywords.
GitHub Actions:
Runs pytest for testing.
Builds and pushes Docker images to GHCR.
Deploys both services to Kubernetes using kubectl.

## 🧪 Running Locally
bash

# Start containers
docker-compose up --build

# 🚀 Running in Kubernetes (Production Setup)
Push code to GitHub
Automatically triggers GitHub Actions:
Runs tests
Builds log-monitor and log-generator images
Pushes to GHCR
Applies Kubernetes deployments
Or Deploy Manually:
bash
kubectl apply -f deployment.yaml

## 🧪 Running Locally (Optional Docker Compose)
Only for local development or testing — Kubernetes is the preferred platform.
bash
docker-compose up --build
