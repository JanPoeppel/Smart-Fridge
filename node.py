"""
node.py

Dieses Modul kümmert sich um das Senden von Nachrichten an Node-RED

"""
ENABLED=False
try:
    import requests
    ENABLED = True
except ImportError:
    ENABLED=False


def sendMessage(msg):
    """
    Sendet eine Nachricht an die Node-RED Schnittstelle

    Args:
        msg: Die zu sendende Nachricht
    """
    if not (ENABLED):
        return
    headers = {'Content-type': 'text/plain'}
    url = 'http://localhost:1880/hello-raw'
    try:
        res = requests.post(url, headers=headers, data = msg)
    except ConnectionError:
        print("Connection Error")
        
    print(res.text)
    
