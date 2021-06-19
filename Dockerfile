# Use baseimage-docker which is a modified Ubuntu specifically for Docker
# https://hub.docker.com/r/phusion/baseimage
# https://github.com/phusion/baseimage-docker
FROM phusion/baseimage:0.11

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Update and install packages
RUN apt update && apt -y upgrade && apt -y install \
    graphviz \
    python3-dev \
    python3-pip

RUN pip3 install black networkx matplotlib pyyaml
# pip3 freeze reports
# black==21.6b0
# networkx==2.5.1
# matplotlib==3.3.4
# PyYAML==5.4.1
