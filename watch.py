import threading
import time, sys, datetime
from selenium import webdriver
import urllib

class WatchYoutube(object):
    """ WatchYoutube class
    The run() method will be started and it will run in the background
    until the video ends.
    """

    def __init__(self, interval=1, video_id='GSAfPHun-9I', download_addon=True):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        :type video_id: str
        :param video_id: Youtube Video Id
        """
        if download_addon == True:
            urllib.urlretrieve("https://addons.mozilla.org/firefox/downloads/file/338640/one_click_proxy_ip-1.0.0-fx-windows.xpi", "one_click_proxy_ip-1.0.0-fx-windows.xpi")
        
        self.interval = interval
        profile = webdriver.FirefoxProfile()
        profile.add_extension(extension='one_click_proxy_ip-1.0.0-fx-windows.xpi')
        self.driver = webdriver.Firefox(firefox_profile=profile)
        self.video_id = video_id
        self.driver.get("https://www.youtube.com/watch?v=" + self.video_id)
        self.player_status = 1
        self.player_time = self.interval 
        self.thread = threading.Thread(target=self.run, args=())
        self.thread.daemon = True                            # Daemonize thread
        self.thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs until video is finished """
        while self.player_status > 0:
            self.player_status = self.driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
            if self.player_status == 0:
                self.driver.close()
            sys.stdout.write("\r" + str(datetime.timedelta(seconds=self.player_time)))
            sys.stdout.flush()   
            time.sleep(self.interval)
            self.player_time += self.interval

