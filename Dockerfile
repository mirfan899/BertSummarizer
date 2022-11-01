FROM python:3.8.13-bullseye

WORKDIR app/

COPY . .
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["python", "api.py"]
