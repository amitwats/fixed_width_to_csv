# Use the official Python image from the Docker Hub
FROM python:3.11

WORKDIR /fixed_width_to_csv
ENV PYTHONPATH "${PYTHONPATH}:/fixed_width_to_csv"
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "main.py"]

