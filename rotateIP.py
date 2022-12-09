import time
from stem import Signal
from stem.control import Controller
import requests

def main():

# Set your ControlPort and you ControlPort Password
ControlPort = 9051
ControlPortPasswd = ""

    while True:
        # Rotates IP every 20 seconds
        time.sleep(20)
        with Controller.from_port(port = ControlPort) as controller:
            # Password for the ControlPort
            controller.authenticate(password=ControlPortPasswd)
            controller.signal(Signal.NEWNYM)


if __name__ == '__main__':
    main()
