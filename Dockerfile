FROM python:3.11-slim

RUN pip install fastapi uvicorn beautifulsoup4 requests openai

ARG AZURE_OPENAI_KEY
ENV AZURE_OPENAI_KEY=$AZURE_OPENAI_KEY

WORKDIR /app

COPY . .

EXPOSE 8008

CMD ["uvicorn", "back.fastapi_chat:app", "--host", "0.0.0.0", "--port", "8008"]