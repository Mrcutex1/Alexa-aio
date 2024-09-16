FROM nikolaik/python-nodejs:python3.10-nodejs19

RUN apt-get update \
    && apt-get install -y --no-install-recommends git zip curl ffmpeg \
    && apt upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/
RUN pip3 install pip --upgrade
RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD bash start
