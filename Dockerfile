FROM python:3.11
WORKDIR /insta-botm
COPY . .
RUN pip install pyTelegramBotAPI
CMD ["python", "main.py"]
