FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
COPY src/ ./src/
COPY data/ ./data/

RUN pip install --no-cache-dir .

ENTRYPOINT ["python", "-m", "techmart"]
CMD ["data/orders.csv"]
