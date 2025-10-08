#  Base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy your project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (FastAPI default)
EXPOSE 8000

# Run FastAPI using uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
