# 1. Base Python image
FROM python:3.14-slim

# 2. Prevent bytecode files & buffering
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 3. System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Copy app source code
COPY . /app/

# 6. Collect static assets for production
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# 7. Start production server
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
