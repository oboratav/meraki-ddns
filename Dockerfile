FROM alpine:latest

WORKDIR /opt/meraki-ddns

ENV AWS_ACCESS_KEY_ID AKIASOMETHINGSOMETHING
ENV AWS_SECRET_ACCESS_KEY YOUR_SECRET_KEY
ENV R53_HOSTED_ZONE YOUR_ROUTE53_HOSTED_ZONE_ID
ENV R53_FQDN YOUR_FQDN
ENV R53_TTL 300

ENV UPDATE_FREQ 299

ENV MERAKI_API_KEY YOUR_MERAKI_API_KEY
ENV MERAKI_NETWORK_ID YOUR_NETWORK_ID
ENV MERAKI_DEVICE_SN YOUR_DEVICE_SERIAL

RUN apk add --update --no-cache python3 && \
    find / -type d -name __pycache__ -exec rm -r {} +   && \
    rm -r /usr/lib/python*/ensurepip                    && \
    rm -r /usr/lib/python*/lib2to3                      && \
    rm -r /usr/lib/python*/turtledemo                   && \
    rm /usr/lib/python*/turtle.py                       && \
    rm /usr/lib/python*/webbrowser.py                   && \
    rm /usr/lib/python*/doctest.py                      && \
    rm /usr/lib/python*/pydoc.py                        && \
    rm -rf /root/.cache /var/cache /usr/share/terminfo

RUN pip3 install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py app.py

CMD ["python3", "app.py"]
