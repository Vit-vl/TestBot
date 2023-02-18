import requests  # type: ignore
import time
from settings import token

API_URL: str = 'https://api.telegram.org/bot'
TEXT: str = 'Здесь должна была быть картинка с котиком :('
API_FOX: str = 'https://randomfox.ca/floof/'
MAX_COUNTER: int = 30

offset: int = -2
counter: int = 0
chat_id: int
cat_response: requests.Response
fox_link: str

while counter < MAX_COUNTER:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{token}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_FOX)
            if cat_response.status_code == 200:
                fox_link = cat_response.json()['image']
                requests.get(f'{API_URL}{token}/sendPhoto?chat_id={chat_id}&photo={fox_link}')
            else:
                requests.get(f'{API_URL}{token}/sendMessage?chat_id={chat_id}&text={TEXT}')
    time.sleep(1)
    counter += 1
