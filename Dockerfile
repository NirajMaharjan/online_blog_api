# Use official Python image
FROM python:3.11-alpine

# Set workdir
WORKDIR /app

# Install system dependencies for psycopg2
RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    python3-dev

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .



# Expose port
# EXPOSE 8000

# # Run server
# CMD ["gunicorn", "online_blog.wsgi:application", "--bind", "0.0.0.0:8000"]

# Expose port (Railway will set $PORT)
EXPOSE 8080

# Run migrations and start server
CMD ["sh", "-c", "python manage.py migrate && gunicorn online_blog.wsgi:application --bind 0.0.0.0:8080"]