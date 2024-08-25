# Use an official Python runtime as a parent image
FROM python:3.11.7-slim

# Install Node.js
RUN apt update && apt install -y nodejs npm

# Install Python requirements
ADD requirements.txt requirements.txt
RUN pip install requirements.txt

# Copy project
ADD /app /src/app
ADD /tailwindcss/ /src

# Set workdir
WORKDIR /src

# Install Tailwind CSS and DaisyUI

# Make sure to follow official docs to fulfill installation
RUN npm install tailwindcss
RUN npm install daisyui

# Command to run when image started
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload