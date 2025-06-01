FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y ffmpeg

# Set workdir
WORKDIR /app

# Copy code and install deps
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "bot"]
