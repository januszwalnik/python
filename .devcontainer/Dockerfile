FROM python:3.10

## Pip dependencies
    # Install packages

    # Upgrade pip
RUN pip install --upgrade pip
    # Install production dependencies
COPY websockets/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt && \
    apt update && \
    apt install -y iproute2 