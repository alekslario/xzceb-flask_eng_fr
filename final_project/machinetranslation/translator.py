import os
import requests
import json
apikey = os.environ['IBM_API_KEY']
#https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/e6ff0d30-1e83-4ccc-b53a-39f13f06e8ab/v3/translate?version=2018-05-01
url = os.environ['IBM_URL']
headers = {'content-type': 'application/json'}

def translate(input_string, source_language, target_language):
    """
    This function takes a string as input and returns a string of the
    machine translation of the input string.
    """
    json_data = {
        'text': [
            input_string
        ],
        'model_id': f'{source_language}-{target_language}',
    }
    response = requests.post(url, headers=headers, json=json_data, auth=('apikey', apikey))
    result = json.loads(response.content)
    return result["translations"][0]["translation"]

def english_to_french(input_string):
    return translate(input_string, 'en', 'fr')

def french_to_english(input_string):
    return translate(input_string, 'fr', 'en')
