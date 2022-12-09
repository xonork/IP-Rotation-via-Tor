# Installation of Tor, Privoxy and Proxychains 
`apt-get install privoxy tor proxychains`

# Proxy configuration
- In the `/etc/privoxy/config` file we will add the following line at the end.

`forward-socks5 / 127.0.0.1:9050 .`

- Next. we will generate a hash of the password that we will use for the *ControlPort*:

`tor --hash-password "YOUR-PASS"`

- Once the hash is generated, we will open the `/etc/tor/torrc` file. We will uncomment the `ControlPort` and the `HashedControlPassword` lines.
  1. In the `ControlPort` line we will change the value of the port for the one we want (default is 9051).
  2. We will replace the value of the `HashedControlPassword` for the one generated before.
  
# Start the services
`systemctl start tor`

`systemctl start privoxy`

# **rotateIP.py** Execution
- We will install the `stem` python library. It will allow us enable the communication with the Tor's control port:

`pip install stem`

- The script **rotateIP.py** will be modified with the password that we have configured for the control port.
- The script will be executed:

`python3 rotateIP.py`

> Note: If you want to verify the IP rotating, before executing **rotateIP.py**, execute **test.py**.

# Use with proxychains
- We will edit the `/etc/proxychains4.conf` file adding the next line at the end:

`socks5 127.0.0.1 9050`

- If you want to execute a command and its traffic goes through the proxy, you will need to add `proxychains` before it:

`privoxy nmap -p- --min-rate 5000 --open target.com`
