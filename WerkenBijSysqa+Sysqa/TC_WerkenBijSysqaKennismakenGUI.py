import base64
import logging
import subprocess
import sys
import time
import unittest
from datetime import datetime, timedelta

import data
import driver
import page
from Extra.commonUnitTest import CommonTestCase

class WerkenBijSysqaKennismakenGUI (CommonTestCase):

    """"Tests voor de WerkenBijSysqa Kennismaken pagina"""

    def test_werkenbij_sysqa_kennismaken (self):


        self.testcase = "TC_werkenBij_WerkenBijSysqaKennismakenGUI"

        link_home_URL = data.werkenBijSysqaPaginaHome
        link_vacatures_URL = data.werkenBijSysqaPaginaVacatures
        link_verhalen_URL = data.werkenBijSysqaPaginaVerhalen
        # link_kennismaken_URL = data.werkenBijSysqaPaginaKennismaken
        # link_kennismaken_URL2 = data.werkenBijSysqaPaginaKennismaken2
        link_kennismaken_footer_URL = data.werkenBijSysqaPaginaKennismakenFooter
        tel_nummer = data.werkenBijSysqaTelefoonNummer
        # link_verhalen_en_videos_URL = data.werkenBijSysqaPaginaVerhalenEnVideos
        link_privacy_URL = data.werkenbijSysqaPaginaPrivacy
        link_quiz_URL = data.werkenBijSysqaPaginaQuiz
        link_adres_URL = data.werkenBijSysqaAdres
        link_corporate_website_URL = data.werkenBijSysqaCorporateWebsite
        link_google_maps_URL = data.werkenBijSysqaGoogleMaps
        link_mail = data.werkenBijSysqaMail
        link_instagram = data.werkenBijSysqaInstagram
        link_linkedin = data.werkenBijSysqaLinkedin
        link_twitter = data.werkenBijSysqaTwitter
        link_facebook = data.werkenBijSysqaFacebook



        sysqa = page.WerkenBijSysqa(self.driver)
        # vacatures = page.WerkenBijSysqaVacatures(self.driver)
        kennis = page.WerkenBijSysqaKennismaken(self.driver)


        #Gebruiker opent de aangemaakt testpagina met resolutie 1920 1080
        kennis.open_sysqa_kennismaken_pagina()
        self.driver.set_window_size(data.homepageDesktopWindowSizeWidth,data.homepageDesktopWindowSizeHeight)
        self.driver.set_window_position(0,0)
        size = self.driver.get_window_size()
        print (size)
        
        #Gebruiker accepteert cookies
        sysqa.accept_cookies()

        #Gebruiker controleert of het SYSQA logo correct werkt
        sysqa.check_navigatie_sysqa_logo(link_home_URL)

        #Gebruiker controleert of de Home button correct werkt 
        sysqa.check_navigatie_home_button(link_home_URL)

        #Gebruiker controleert of de Vacatures button correct werkt
        sysqa.check_navigatie_vacatures_button(link_vacatures_URL)

        #Gebruiker controleert of de Verhalen button correct werkt
        sysqa.check_navigatie_verhalen_button(link_verhalen_URL)

        #Gebruiker controleert of de Kennismaken button correct werkt
        sysqa.check_navigatie_kennismaken_button(link_kennismaken_footer_URL)

        #Gebruiker controleert of het telefoonnummer correct werkt
        sysqa.check_navigatie_telefoon_button(tel_nummer)

        #Gebruiker controleert of de Slogan correct is
        kennis.check_kennismaken_slogan()

        #Gebruiker controleert of de Naam text en box correct zijn
        kennis.check_kennismaken_naam_text()
        kennis.check_kennismaken_naam_box()

        #Gebruiker controleert of de email text en box correct zijn
        kennis.check_kennismaken_email_text()
        kennis.check_kennismaken_email_box()

        #Gebruiker controleert of de bericht text en box correct zijn
        kennis.check_kennismaken_bericht_text()
        kennis.check_kennismaken_bericht_box()
        
        #Gebruiker controleert of de voorwaarden correct zijn
        kennis.check_kennismaken_voorwaarden_text(link_privacy_URL)

        #Gebruiker controleert of de update text correct is
        kennis.check_kennismaken_updates_slogan()
        kennis.check_kennismaken_updates_text()

        #Gebruiker controleert of de Doe de Test button correct werkt/is
        sysqa.check_sysqa_quiz_button_footer(link_quiz_URL)

        #Gebruiker controleert of de in-page navigatie buttons in de footer correct werken
        sysqa.check_sysqa_home_button_footer(link_home_URL)
        sysqa.check_sysqa_vacatures_button_footer(link_vacatures_URL)
        sysqa.check_sysqa_verhalen_en_videos_button_footer(link_verhalen_URL)
        sysqa.check_sysqa_kennismaken_button_footer(link_kennismaken_footer_URL)

        #Gebruiker controleert of de adres button in de footer correct werkt/is
        sysqa.check_sysqa_adres_button_footer(link_adres_URL)

        #Gebruiker controleert of de Contact buttons correct werken
        sysqa.check_sysqa_corporate_website_button_footer(link_corporate_website_URL)
        sysqa.check_sysqa_google_maps_button_footer(link_google_maps_URL)
        sysqa.check_sysqa_telefoon_button_footer(tel_nummer)
        sysqa.check_sysqa_mail_button_footer(link_mail)

        #Gebruiker controleert of de Nieuwsbrief button correct werkt/is
        sysqa.check_sysqa_nieuwsbrief_button_footer()

        #Gebruiker controleert of de Nieuwsbrief aanmelden popup correct is
        sysqa.check_sysqa_nieuwsbrief_aanmelden_popup_zichtbaar()
        sysqa.check_sysqa_nieuwsbrief_aanmelden_popup_text()

        #Gebruiker controleert of de Nieuwsbrief aanmelden popup correct werkt
        sysqa.check_sysqa_nieuwsbrief_aanmelden_naam_box()
        sysqa.check_sysqa_nieuwsbrief_aanmelden_email_box()
        sysqa.check_sysqa_nieuwsbrief_aanmelden_accept_box()
        sysqa.check_sysqa_nieuwsbrief_aanmelden_verstuur_box()
        # sysqa.check_sysqa_nieuwsbrief_aanmelden_verificatie_text()

        #Gebruiker controleert of de Social Media buttons in de footer correct zijn
        sysqa.check_sysqa_instagram_button_footer(link_instagram)
        sysqa.check_sysqa_linkedin_button_footer(link_linkedin)
        sysqa.check_sysqa_twitter_button_footer(link_twitter)
        sysqa.check_sysqa_facebook_button_footer(link_facebook)


if __name__ == "__main__":
    if len(sys.argv) >1:
        WerkenBijSysqaKennismakenGUI.pipeline = sys.argv.pop()
    unittest.main()