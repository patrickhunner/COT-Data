FROM python:3.9

WORKDIR /app

COPY app/analyzer.py .

RUN pip install pandas openpyxl sodapy

CMD ["python", "analyzer.py"]