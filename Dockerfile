FROM python:3.11

COPY . /app/

WORKDIR /app

RUN python -m pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]