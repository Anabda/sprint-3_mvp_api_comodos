FROM python:3.9
WORKDIR /mvp_api_comodos
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV HOST=0.0.0.0
ENV PORT=5001
EXPOSE $PORT

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5001"]