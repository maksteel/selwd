from watch import *
import time
from selenium.common.exceptions import UnexpectedAlertPresentException
try:
        example = WatchYoutube(download_addon=False)
        example.thread.join()
except UnexpectedAlertPresentException:
        print("Standing down")
        time.sleep(300)
