FROM python:3.10-slim-bullseye

RUN pip3 install google-api-python-client grpcio pyvmomi

RUN mkdir -p /entrypoint.py/tools/
COPY *.py /entrypoint.py/
COPY tools/*.py /entrypoint.py/tools/

CMD ["python3", "/entrypoint.py/vcenter-csi-driver.py"]

