FROM ubuntu:20.04

RUN apt-get update \
 && apt-get install -y python3 python3-pip \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /opt
COPY app.py .

# Instaliraj Flask (ili requirements.txt ako ga imaš)
RUN pip3 install --no-cache-dir flask

# Ako app.py koristi app.run(...), ne treba nam Flask CLI
EXPOSE 8080
