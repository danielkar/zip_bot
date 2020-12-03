from datetime import datetime, timedelta, timezone
import time
import dbworker

def check_time(chat_id):
    time_load_str = dbworker.get_field(chat_id, 'date')
    time_now = datetime.now(timezone.utc)

    if time_now < time_load_str[0] + timedelta(weeks=1):
        return True
    else:
        return False
