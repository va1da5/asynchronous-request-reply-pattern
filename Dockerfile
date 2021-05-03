FROM python:3.8.7-slim

EXPOSE 8000

WORKDIR /app

RUN apt update && apt upgrade -y \
  && adduser --no-create-home fastapi \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

USER fastapi

ENTRYPOINT [ "sh" ]

CMD [ "-c", "uvicorn app.main:app --reload --host 0.0.0.0 --port 8000" ]
