FROM registry.access.redhat.com/rhscl/python-36-rhel7:latest
ENV FLASK_APP=main.py

COPY ./* /opt/app-root/src
RUN cd /opt/app-root/src
RUN pip install -r requirements.txt

USER 1001
CMD ["flask", "run", "-h", "0.0.0.0"]
