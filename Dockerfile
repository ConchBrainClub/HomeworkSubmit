FROM ubuntu

EXPOSE 80
WORKDIR /app

COPY . .

RUN apt update && apt upgrade -y
RUN apt install python3 python3-pip -y

RUN pip3 install -r requirements.txt

CMD [ "python3","./src/main.py" ]
