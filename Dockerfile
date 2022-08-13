FROM python

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt

#EXPOSE 3000

CMD ["python", "bot.py"]
