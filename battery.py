import psutil
import time
import fire

from common.selenium_manager import SeleniumManager
from common.logger import set_logger
logger = set_logger(__name__)

VIDEO_URL = "https://www.youtube.com/watch?v=ArQvRDWulns"

def run():
    logger.info("start")
    battery = psutil.sensors_battery()
    if not battery:
        logger.error("This pc has not battery")
        return None
    
    manager = SeleniumManager(use_headless=False)
    chrome = manager.start_chrome()
    chrome.get(VIDEO_URL)
    
    while True:
        logger.info(battery.percent)
        time.sleep(60 * 10)
    

if __name__ == "__main__":
    fire.Fire(run)