FROM apache/airflow:2.4.1-python3.10

USER airflow
RUN pip install -r requirements.txt

COPY airflow/patches/jinjasql /home/airflow/.local/lib/python3.10/site-packages/jinjasql


