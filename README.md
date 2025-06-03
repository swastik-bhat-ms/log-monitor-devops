# 🔍 Log Monitor DevOps Project

This project demonstrates a complete DevOps pipeline that continuously generates and monitors log files using Python, Docker, and GitHub Actions.

## 📦 Components

- **Log Generator**: Simulates application logs.
- **Log Monitor**: Scans logs for keywords like `error`, `failed`, `critical`.
- **GitHub Actions**: Automates testing and CI pipeline.
- **Docker & Docker Compose**: Containerizes the entire setup.

## 🛠 How It Works

1. **Log Generator** writes random log messages to `sample.log`.
2. **Log Monitor** continuously reads the file and prints alerts for critical messages.
3. **GitHub Actions** runs `pytest` to ensure functionality.

## 🧪 Running Locally

```bash
# Start containers
docker-compose up --build
