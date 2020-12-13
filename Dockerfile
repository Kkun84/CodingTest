FROM python:3.8.6

# Timezone setting
RUN apt-get update && apt-get install -y --no-install-recommends tzdata

# Install something
RUN apt-get update && apt-get install -y --no-install-recommends fish
RUN apt-get update && apt-get install -y --no-install-recommends nano git sudo curl

# Install Python library
COPY requirements.txt /
RUN pip3 install -r /requirements.txt

ARG UID
ARG GID
ARG USER
ARG PASSWORD
RUN groupadd -g ${GID} ${USER}_group
RUN useradd -m --uid=${UID} --gid=${USER}_group --groups=sudo ${USER}
RUN echo ${USER}:${PASSWORD} | chpasswd
RUN echo 'root:root' | chpasswd
USER ${USER}

WORKDIR /workspace
