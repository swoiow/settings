FROM alpine

ENV SS_VERSION=2.9.1

WORKDIR /ss
RUN wget -O- https://github.com/shadowsocks/shadowsocks/archive/${SS_VERSION}.tar.gz | tar zx \
    && apk add python3 \
    && cd shadowsocks-${SS_VERSION} \
    && python3 setup.py install

ENTRYPOINT ["/usr/bin/ssserver"]