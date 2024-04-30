# Use an official Python runtime as the base image
FROM python:latest

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Add Google Chrome repository and install Google Chrome
RUN apt-get update && \
    apt-get install -y chromium &&\
    apt-get install -y chromium-driver

# Set up the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt
# Run migrations and populate database
RUN python manage.py migrate && \
    python parser.py && \
    python insert_to_django.py

# Expose the port the app runs on
EXPOSE 8000

# Command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]