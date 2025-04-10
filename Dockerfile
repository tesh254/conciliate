FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install watchdog for file monitoring (hot reload)
RUN pip install --no-cache-dir watchdog[watchmedo]

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create a script to run the application with hot reload
RUN echo '#!/bin/bash\n\
watchmedo auto-restart --directory=./ --pattern="*.py" --recursive -- python "$@"' > /usr/local/bin/run-with-reload && \
    chmod +x /usr/local/bin/run-with-reload

# Command to run when container starts
CMD ["run-with-reload", "arbitrage.py"]