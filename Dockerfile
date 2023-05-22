# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the Django project code to the container
COPY . /code/

# Expose the Django development server port (change it if needed)
EXPOSE 2000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:2000"]
