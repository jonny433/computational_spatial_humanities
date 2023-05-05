FROM python:3.11-slim

# EXPOSE 8080

ENV APP_HOME=/home/app
ENV APP_USER=appuser

WORKDIR $APP_HOME

# Update package references
RUN apt-get update && apt-get install -y

# Install postgres client
RUN apt-get install -y \
  libpq-dev \
  libmariadb-dev-compat \
  libmariadb-dev \
  gcc \
  build-essential \
  python-dev

# Upgrade pip
RUN pip install --upgrade pip

# Install python dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY ./src .

# CMD ["python", "app.py"]
