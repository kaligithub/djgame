# Command for building the container sending the build arguments.
# docker-compose build --build-arg ssh_prv_key="$(cat ~/.ssh/id_rsa)" --build-arg ssh_pub_key="$(cat ~/.ssh/id_rsa.pub)"

FROM python:3.8

ENV PYTHONUNBUFFERED 1

# Receive the current user's ssh keys as command line arguments while
# building the container.
ARG ssh_prv_key
ARG ssh_pub_key

RUN apt-get update && apt-get install -y git

# Authorize SSH Host
RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan phab.renewbuy.com > /root/.ssh/known_hosts

# Add the keys and set permissions
RUN echo "$ssh_prv_key" > /root/.ssh/id_rsa && \
    echo "$ssh_pub_key" > /root/.ssh/id_rsa.pub && \
    chmod 600 /root/.ssh/id_rsa && \
    chmod 600 /root/.ssh/id_rsa.pub

RUN mkdir /code /var/log/play /code/static

WORKDIR /code

ADD requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt -U

# Remove SSH keys
RUN rm -rf /root/.ssh/

# Copy all the code.
COPY . /code/

