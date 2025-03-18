FROM python:3.13-alpine

WORKDIR /app
COPY ./requirements.txt ./requirements.txt
COPY ./*.py ./
COPY ./data/*.* ./data/

RUN pip install --no-cache-dir -r ./requirements.txt

CMD ["python", "write_image.py"]
