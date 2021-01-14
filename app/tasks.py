from celery import Celery
import urllib.request
import config


app = Celery('tasks', broker=config.CELERY_BROKER_URL)


@app.task
def upload_zip(chat_id, url):
    urllib.request.urlretrieve(url, f'./downloads/{str(chat_id)}.zip')
