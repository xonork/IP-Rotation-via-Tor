import time
from stem import Signal
from stem.control import Controller
import requests

def main():
    proxies = {
        "http": "socks5://127.0.0.1:9050"
    }

    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11'
    }

    while True:
        # Rotates IP every 20 seconds
        time.sleep(20)
        with Controller.from_port(port = 9051) as controller:
            # Password for the ControlPort
            controller.authenticate(password="")
            controller.signal(Signal.NEWNYM)
        # Checks the IP
        r = requests.get("http://icanhazip.com", proxies=proxies, headers=headers)
        print (r.text)


if __name__ == '__main__':
    main()
