FROM python:3.11-bookworm
WORKDIR /usdrub

COPY usdrub/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python -m unittest discover -v test
CMD ["python", "runservers.py"]