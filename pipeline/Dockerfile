FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
WORKDIR /code

ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev
RUN uv sync --locked

# RUN pip install pandas pyarrow


COPY ingest_data.py .

ENTRYPOINT  ["python","ingest_data.py"]



# uv run python ingest_data.py \
#   --pg-user=root \
#   --pg-pass=root \
#   --pg-host=localhost \
#   --pg-port=5432 \
#   --pg-db=ny_taxi \
#   --target-table=yellow_taxi_trips_2021_1 \
#   --year=2021 \
#   --month=1 \
#   --chunksize=100000
