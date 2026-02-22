






# Start with slim Python 3.13 image for smaller size
FROM python:3.13.11-slim

# Copy uv binary from official uv image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set working directory inside container
WORKDIR /app

# Add virtual environment to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency files first (better caching)
COPY "pyproject.toml" "uv.lock" ".python-version" ./
# Install all dependencies (pandas, sqlalchemy, psycopg2)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev
    
RUN uv sync --locked

# Copy ingestion script
COPY ingest_data.py ingest_data.py 

# Set entry point to run the ingestion script
ENTRYPOINT [ "python", "ingest_data.py" ]