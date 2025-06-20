import time
from datetime import datetime
while(True):
    now=datetime.now()
    hour=now.hour
    minute=now.minute
    second=now.second
    
   if hour>=0:
        if minute>=0:
            if second>=0:
                print(f"Time:{hour:02d}:{minute:02d}:{second:02d}")
    time.sleep(1)
