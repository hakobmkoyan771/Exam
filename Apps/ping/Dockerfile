FROM ubuntu

COPY . /pythonping/

ENV SERVER_IP_ADDRESS "None"

RUN apt-get -y update

RUN apt-get -y install python3

RUN apt-get -y install python3-pip

RUN pip3 install -r /pythonping/requirements.txt

ENTRYPOINT ["python3"]

CMD ["/pythonping/main.py"]
