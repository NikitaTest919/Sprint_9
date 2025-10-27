FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# чтобы pytest запускался при старте контейнера (по желанию)
CMD ["pytest", "-q", "--alluredir=allure_results"]
