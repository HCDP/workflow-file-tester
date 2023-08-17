FROM ubuntu:latest

# Install required packages
RUN apt-get update \
    && apt-get install -y iputils-ping python3 python3-pip
RUN pip3 install --upgrade pip
RUN apt-get update && apt-get install -y wget

# Set working dir
WORKDIR /app

# Install dependencies
RUN pip3 install tapipy
RUN pip3 install secure-smtplib

# Copy the script and required files
COPY scripts/tapis_file_lister.py scripts/
COPY scripts/update_date_string.py scripts/
COPY scripts/check_file.py scripts/
COPY scripts/message.py scripts/
COPY data/default.json data/
COPY actor/task.sh /app/actor/task.sh


# This container is intended to run the task wrapper at launch, unless otherwise specified at run-time.
CMD [ "/bin/bash", "/app/actor/task.sh" ]