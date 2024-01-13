FROM python:3.11.4-slim

COPY ./requirements.txt requirements.txt

# Install requirements.
RUN apt-get update && \
    apt-get install -y git && \
    python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# Copy app to working directory.
WORKDIR /app
COPY ./app /app

# Start the service with exposed port.
EXPOSE 80
ENTRYPOINT ["python", "."]
