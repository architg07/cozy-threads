# Set up Flask application
FROM python:3.8-slim-buster
WORKDIR /cozy-threads/server
COPY ./requirements.txt .
RUN pip install gunicorn
ENV PATH="/path/to/gunicorn:${PATH}"
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5001
CMD ["gunicorn", "-b", ":5001", "app:app"]