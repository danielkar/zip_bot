from datetime import datetime, timedelta
import dbworker

def check_time(chat_id):
    time_load = dbworker.get_field(chat_id, 'time')
    time_now = datetime.datetime.now().timestamp()
    
    if time_now < time_load + timedelta(weeks = 1):
        return True
    else:
        return False
