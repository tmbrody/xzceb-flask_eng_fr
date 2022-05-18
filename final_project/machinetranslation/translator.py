"""
This module translates any English text into French and vice versa
"""

# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['API_KEY']
url = os.environ['API_URL']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator= authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    This function translates the provided English text into French
    """
    if english_text is None:
        return None

    french_text = language_translator.translate(
        text= english_text,
        model_id= 'en-fr').get_result()
    return french_text.get('translations')[0].get('translation')

def french_to_english(french_text):
    """
    This function translates the provided English text into French
    """
    if french_text is None:
        return None

    english_text = language_translator.translate(
        text= french_text,
        model_id= 'fr-en').get_result()
    return english_text.get('translations')[0].get('translation')
