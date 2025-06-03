# Use official Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy your script into the container
COPY log_monitor.py .

# Run the script
CMD ["python", "log_monitor.py"]

