import json;
JSONstr = '{"first_name": "Guido", "last_name":"Rossum"}'

parsedJSON = json.loads(JSONstr);

print(parsedJSON);

from socketIO_client import SocketIO

SOCKET_HOST = 'http://eval.socket.nio.works'


def handle_message(message, *args):
    """ Called whenever a message comes through the socket.

    Args:
        message (str): The message we just received
        *args: Any additional arguments received, likely will be empty
    """
    parsedMessage = json.loads(message);
    print(parsedMessage);

with SocketIO(SOCKET_HOST) as sock:
    # Set up our message handler
    sock.on('recvData', handle_message)
    # Join the "fruits" room
    sock.emit('ready', 'groceries')
    # Wait for messages to come through! Ctrl-C to quit
    sock.wait()
