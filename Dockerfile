FROM python:3.9.1-slim-buster
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
COPY app/gromit.py /usr/local/bin/gromit
RUN chmod +x /usr/local/bin/gromit
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install pyaml
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]