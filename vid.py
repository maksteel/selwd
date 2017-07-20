from watch import *
import time, sys, datetime
from selenium.common.exceptions import UnexpectedAlertPresentException
try:
        if len(sys.argv) > 1:
		video_id = str(sys.argv[1])
	else:
		video_id = "GSAfPHun-9I"
	print("Watching %s at %s" % (video_id, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")) )
	example = WatchYoutube(video_id=video_id, download_addon=False)
        example.thread.join()
except UnexpectedAlertPresentException:
        print("Standing down")
        time.sleep(300)
