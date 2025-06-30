# Use a minimal Python image
FROM python:3.12-slim-bullseye

# Create & switch to non-root user
RUN useradd --create-home appuser

# Set working directory
WORKDIR /app

# Copy & install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create writable output directories, set ownership
RUN mkdir logs qr_codes \
    && chown appuser:appuser logs qr_codes

# Copy your application code as non-root
COPY --chown=appuser:appuser . .

# Run as non-root user
USER appuser

# Default entrypoint & cmd
ENTRYPOINT ["python", "main.py"]
CMD ["--url", "https://github.com/ar2369git"]
