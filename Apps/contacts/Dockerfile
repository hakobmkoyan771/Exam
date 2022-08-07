FROM ubuntu

COPY . /project/

ENV MONGO_DB_IP_ADDRESS "None"

RUN apt-get -y update && apt-get -y install systemctl

RUN apt-get -y update

RUN apt-get -y install python3

RUN apt-get -y install python3-pip

RUN pip3 install -r /project/requirements.txt

RUN apt -y install curl

ENTRYPOINT ["python3"]

CMD ["/project/main.py"]
