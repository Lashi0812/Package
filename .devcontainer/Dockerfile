FROM python:3.11.7

ARG DEBIAN_FRONTEND=noninteractive
# Install dependencies
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && \
    apt-get install -y \
        curl \
        git \
        zsh \
        ca-certificates \
        bash \
        build-essential \
        && \
    rm -rf /var/lib/apt/lists/*

ENV SHELL /bin/zsh
COPY .devcontainer/zsh-plugins/.p10k.zsh .devcontainer/zsh-plugins/ohmyzsh.sh /root/
RUN chmod +x /root/ohmyzsh.sh && sh -c /root/ohmyzsh.sh

RUN pip install build





