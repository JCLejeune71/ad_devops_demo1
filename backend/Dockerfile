FROM python:3.11-slim

WORKDIR /app
RUN pip install --no-cache-dir fastapi uvicorn

COPY main.py .

ENV APP_VERSION="v1.0"
ENV DEPLOYED_BY="manual"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
