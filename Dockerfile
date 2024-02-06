FROM python:3.10-slim

ARG USER_ID
ARG USER_NAME
ENV HOME=/home/${USER_NAME} 


RUN mkdir -p /app 
WORKDIR /app 
RUN python -m pip install dask distributed --upgrade
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt



COPY . /app/


ENTRYPOINT ["python", "src/pre-process.py"]