# Use Alpine Linux as the base image
FROM python:3.9-alpine

# Set a non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set the working directory
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies using a non-root user
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the script into the container
COPY pokemon_scanner.py .

# Switch to non-root user
USER appuser

# Set entry point
ENTRYPOINT ["python", "pokemon_scanner.py"]

