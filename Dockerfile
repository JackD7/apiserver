ARG PIP_INSTALL="pip3 install --no-cache-dir"

FROM python:3.7-slim-buster
ARG PIP_INSTALL

WORKDIR /opt

COPY ./python/requirements.txt .
RUN ${PIP_INSTALL} --no-deps -r requirements.txt
RUN pip3 check

COPY ./python .
RUN ${PIP_INSTALL} --no-deps -e .
RUN pip3 check

CMD ["api-server"]
