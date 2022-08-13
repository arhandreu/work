FROM python

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt

#EXPOSE

CMD ["python", "bot.py"]
