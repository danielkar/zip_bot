from datetime import datetime, timedelta
import time
import dbworker

def check_time(chat_id):
    time_load_str = dbworker.get_field(chat_id, 'date')
    print(time_load_str)
    time_load = datetime.strptime(time_load_str, '%Y-%m-%d %H:%M:%S.%f')
    time_now = datetime.fromtimestamp(time.time())

    if time_now < time_load + timedelta(weeks=1):
        return True
    else:
        return False
