"""
node.py

Dieses Modul kümmert sich um das Senden von Nachrichten an Node-RED

"""
ENABLED=False
try:
    import requests
    from urllib3.exceptions import NewConnectionError
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
    try:
        headers = {'Content-type': 'text/plain'}
        url = 'http://localhost:1880/hello-raw'
        res = requests.post(url, headers=headers, data = msg)
    except NewConnectionError as e:    # This is the correct syntax
        res = e

    print(res.text)
