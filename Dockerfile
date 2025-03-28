# Using an official Python image as a base
FROM python:3.10

# Set the working directory in the container
WORKDIR /usr/src

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copying application files to the container
COPY . .

# Set the working app directory in the container
WORKDIR /usr/src/app

# Command to start FastAPI server using Uvicorn
CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8003"]
