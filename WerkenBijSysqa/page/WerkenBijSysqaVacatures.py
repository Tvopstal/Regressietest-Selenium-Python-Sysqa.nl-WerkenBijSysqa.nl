from .BasePage import BasePage
from .locator import locator as loc
import subprocess, sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import logging, time
import driver
import data

class WerkenBijSysqaVacatures (BasePage):

    def open_sysqa_vacature_pagina (self):
        link = data.werkenBijSysqaPaginaVacatures
        logging.info(f"Startpagina WerkenbijSysqa wordt geopend:{link}")
        self.driver.get(link) 





