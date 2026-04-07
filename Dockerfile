FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir fastmcp requests

COPY server.py .

CMD ["python", "server.py"]
