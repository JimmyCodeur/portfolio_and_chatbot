FROM python:3.11-slim

RUN pip install fastapi uvicorn beautifulsoup4 requests openai

WORKDIR /app

COPY back .

COPY ../front /app/front/

EXPOSE 8008

CMD ["uvicorn", "fastapi_chat:app", "--host", "0.0.0.0", "--port", "8008"]


