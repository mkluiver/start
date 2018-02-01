import time
import requests
import hashlib
import hmac
import python-bittrex

TICK_INTERVAL = 60  # seconds
#API_KEY = 'my-api-key'
#API_SECRET_KEY = b'my-api-secret-key'


def main():
    print('Starting trader bot, ticking every ' + str(TICK_INTERVAL) + 'seconds')

    while True:
        start = time.time()
        tick()
        end = time.time()

        # Sleep the thread if needed
        if end - start < TICK_INTERVAL:
            time.sleep(TICK_INTERVAL - (end - start))
            
def tick():
    pass
