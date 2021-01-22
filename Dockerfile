FROM python:3.8

WORKDIR /anecdotes
ADD . .

RUN apt-get update && apt-get install -y curl
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py
RUN python3 -m pip install Django
RUN python3 manage.py migrate

EXPOSE 8000

ENTRYPOINT ["python3","manage.py"]
CMD ["runserver","0.0.0.0:8000"]

