FROM python:3.13-alpine

WORKDIR /app
COPY ./requirements.txt ./requirements.txt
COPY ./*.py ./
COPY ./templates /app/templates

RUN mkdir tmp
RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "--worker-tmp-dir", "/app/tmp", "-b", "0.0.0.0:8000", "website:app"]
