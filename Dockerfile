FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -e . pytest

ENTRYPOINT ["elyria-build-tool"]
CMD ["questions"]
