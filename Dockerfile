FROM python:3.7

ENV MONGO_DETAILS="mongodb+srv://juan_david_naranjo:Juanda26021998@cluster0.4l2q2.mongodb.net/?retryWrites=true&w=majority"
ENV algorithm=HS256
ENV secret=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
ENV token_expire_minutes=20
ENV token_expire_hours=1440
ENV TZ=America/Bogota

COPY requirements.txt . 
RUN pip install -r requirements.txt

EXPOSE 80

WORKDIR /app 
COPY ./app /app

#ENTRYPOINT ["ddtrace-run"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


#Elastic Search
