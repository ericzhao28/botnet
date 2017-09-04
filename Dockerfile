From tensorflow/tensorflow:latest-py3

# Install apk packages
RUN apt update \
  && apt install gcc make libc-dev g++ bzip2 libssl-dev build-essential tshark -y

# Establish working directory
WORKDIR /service

# Copying pip requirement files
COPY ./requirements.txt ./requirements.txt

# Install python dependencies
RUN export C_INCLUDE_PATH=/usr/include
RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt