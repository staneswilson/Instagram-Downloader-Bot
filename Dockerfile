FROM python:latest

WORKDIR /app

RUN apt-get update && \
    apt-get install -y ffmpeg

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "start.sh"]