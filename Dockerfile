FROM python:3.13-slim

WORKDIR /restaurant_booking_ivan_4

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN rm -rf __pycache__ .idea

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
