FROM python:3.9


COPY analyzer.py .

RUN pip install pandas openpyxl sodapy

CMD ["python", "analyzer.py"]