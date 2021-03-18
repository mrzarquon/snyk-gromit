FROM python:slim-buster
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
COPY app/gromit.py /usr/local/bin/gromit
RUN chmod +x /usr/local/bin/gromit
RUN apt-get update && \
    apt-get install -y git && \
    apt-get update && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/*
RUN pipenv install --system
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]