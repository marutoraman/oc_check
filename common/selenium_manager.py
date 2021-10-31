from bs4 import BeautifulSoup

import os
import zipfile
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from common.logger import set_logger


logger = set_logger(__name__)

class SeleniumManager():

    def __init__(self, use_headless: bool = True, 
                 use_proxy:bool=False, proxy_user:str=None, proxy_pass:str=None, 
                 proxy_host:str=None, proxy_port:str=None):
        self.use_headless = use_headless
        self.proxy_user = proxy_user
        self.proxy_pass = proxy_pass
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.options = None
        self.use_proxy = use_proxy
        self.chrome = self.start_chrome()

    def start_chrome(self):
        '''
        ChromeDriverを起動してブラウザを開始する
        '''
        # Chromeドライバーの読み込み
        self.options = ChromeOptions()

        # ヘッドレスモードの設定
        if self.use_headless:
            logger.info("ヘッドレスモード")
            self.options.add_argument('--headless')
        

        self.options.add_argument('log-level=3') 
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')
        self.options.add_argument('--user-data-dir=' + os.path.join(os.getcwd(),"profile"))
        self.options.add_argument('--profile-directory=Profile1')
        #self.options.add_argument('--incognito')          # シークレットモードの設定を付与
        # self.options.add_argument('--no-sandbox')          # docker環境では必須
        # self.options.add_argument('disable-infobars') # AmazonLinux用
        # self.options.add_argument("--disable-gpu")
        
        # ChromeのWebDriverオブジェクトを作成する。
        try:
            driver = Chrome(ChromeDriverManager().install(), chrome_options=self.options)
            logger.info("chrome driver起動成功")
            return driver
        except Exception as e:
            logger.error(f"driver起動エラー:{e}")
            raise Exception(f"driver起動エラー:{e}")
    
