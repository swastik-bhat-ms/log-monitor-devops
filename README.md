# 🚀 DevOps Log Monitoring Pipeline with Jenkins, Docker & Python

This project demonstrates a complete DevOps pipeline using **Docker**, **Jenkins**, and **Python** to simulate and monitor log file activity in real-time.

---

## 📦 Project Structure
├── Dockerfile # For log-monitor (log-mon.py)
├── dockerfile.generator # For log-generator (log-generator.py)
├── Dockerfile.jenkins # Custom Jenkins Docker image
├── docker-compose.yml # Multi-container setup
├── log-mon.py # Python log monitor
├── log-generator.py # Python log writer
├── sample.log # Shared log file
└── Jenkinsfile # Jenkins pipeline script

## 🔧 Services (via `docker-compose.yml`)

### 1. **log-monitor**
- Reads and monitors `sample.log`
- Built from `log-mon.py`

### 2. **log-generator**
- Continuously writes logs to `sample.log`
- Built from `log-generator.py`

### 3. **jenkins**
- Jenkins server inside a Docker container
- Triggers builds and manages the CI/CD pipeline
- Custom Dockerfile includes Docker CLI and Docker Compose

---

## 🧪 How It Works

1. Jenkins runs on `localhost:8080`.
2. On each GitHub push or manual trigger, Jenkins:
   - Pulls the latest code
   - Builds and starts the log services
   - Monitors log file activity
3. Output is visible in Jenkins logs and container logs.

---

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose
- Python 3
- Git

🧠 Learning Outcomes
Set up a custom Jenkins container

Configure Docker-based services

Automate builds and log monitoring with Jenkins

Troubleshoot container conflicts during CI/CD
