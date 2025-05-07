FROM python:3.11-alpine as builder

WORKDIR /app

RUN apk add --no-cache gcc musl-dev libffi-dev postgresql-dev libpq

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --prefix=/install --no-cache-dir -r requirements.txt

FROM python:3.11-alpine

WORKDIR /app

COPY --from=builder /install /usr/local

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
