FROM python:3.6-slim

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
RUN rm -rf /code/app/data/databaseurl.py
COPY ./databaseurlprod.py /code/app/data/databaseurl.py

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
