FROM python:3.10

WORKDIR /app

COPY /app/requirements.txt /app
RUN pip install -r requirements.txt

COPY /app /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]
