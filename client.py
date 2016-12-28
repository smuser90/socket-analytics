import json;
import os;
import signal;
import sys;
from Analytics import Analytics;
from socketIO_client import SocketIO;

SOCKET_HOST = 'http://eval.socket.nio.works'

def clear_screen():
    print(chr(27) + "[2J");
    _unused = os.system("clear");

def signal_handler(signal, frame):
    print('\r\nShutting down... please wait.')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
fruitAnalytics = Analytics("fruit");

def handle_message(message, *args):
    """ Called whenever a message comes through the socket.

    Args:
        message (str): The message we just received
        *args: Any additional arguments received, likely will be empty
    """

    parsedMessage = json.loads(message);
    amount = parsedMessage['amount'];
    cart = parsedMessage['cart'];
    shopper = parsedMessage['shopper']

    clear_screen();
    fruitAnalytics.transaction(cart);
    print("Mean fruit is",round(fruitAnalytics.getMean(),2),'per transaction');
    print("Fruit per second is",round(fruitAnalytics.catPerSecond(),2));
    print("Transactions per second is",round(fruitAnalytics.transPerSecond(),4))
    # print("Amount: ",amount);
    # print("Cart: ",cart);
    # print("Shopper: ",shopper);

with SocketIO(SOCKET_HOST) as sock:
    # Set up our message handler
    sock.on('recvData', handle_message)
    # Join the "fruits" room
    sock.emit('ready', 'groceries')
    # Wait for messages to come through! Ctrl-C to quit
    sock.wait()
