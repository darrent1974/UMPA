ARG BASE_IMAGE=python:3.12-slim-bookworm
FROM ${BASE_IMAGE}

ARG USER_NAME
ARG USER_UID
ARG USER_GID
ARG USER_GROUP_NAME
ARG ASUSER_NAME
ARG ASUSER_UID
ARG ASUSER_GID
ARG ASUSER_GROUP_NAME

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Australia/Melbourne
ENV PIP_ROOT_USER_ACTION=ignore

# Change to bash
SHELL [ "/bin/bash", "-c" ]

# Install packages
RUN apt-get update --fix-missing \
    && apt-get -y install --no-install-recommends \
    build-essential \
    ca-certificates \
    curl \
    git \
    gnupg \
    openssh-client \
    software-properties-common \ 
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    python3-numpy \    
    pkg-config \
    sudo

# Create user and groups
RUN groupadd --gid ${USER_GID} ${USER_GROUP_NAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USER_NAME} \
    && echo ${USER_NAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USER_NAME} \
    && chmod 0440 /etc/sudoers.d/${USER_NAME}     

# Setup python venv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN chown -R ${USER_NAME} /opt/venv/

RUN pip3 install meson ninja numpy cython pkgconfig build twine pytest
