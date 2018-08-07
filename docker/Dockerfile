FROM registry.cn-shenzhen.aliyuncs.com/pihou-api/api-base:1.0

MAINTAINER monkey <bufan108@gmail.com>

RUN mkdir -p /app /data/log

ADD . /app
RUN ls /app
RUN cp /app/docker/nginx.conf /usr/local/openresty/nginx/conf/nginx.conf && \
cp /app/docker/longban.conf /etc/nginx/conf.d/default.conf

RUN pip install --index-url https://mirrors.aliyun.com/pypi/simple/ -r /app/docker/requirements.txt

WORKDIR /app
VOLUME /data/log/
EXPOSE 80

CMD ["supervisord", "-n", "-c", "/app/docker/supervisord.conf"]

