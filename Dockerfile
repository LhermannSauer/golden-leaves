FROM python
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5001
CMD ["flask","run","--debug","--host=0.0.0.0","--port=5001"]