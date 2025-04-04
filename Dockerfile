FROM python:3.9-alpine

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && \ 
    pip install --no-cache-dir requests

COPY pokemon_scanner.py /app/

CMD ["python", "pokemon_scanner.py"]

