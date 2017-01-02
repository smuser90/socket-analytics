import json;
import os;
import signal;
import sys;
import time;
import numpy;
import os;
from Analytics import Analytics;
from socketIO_client import SocketIO;
from bashplotlib.scatterplot import plot_scatter;
import threading

_renderCount = 0;
SOCKET_HOST = 'http://eval.socket.nio.works'
plotList = []

def clear_screen():
    print(chr(27) + "[2J");
    _unused = os.system("clear");

def signal_handler(signal, frame):
    print('\r\nShutting down... please wait.')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
fruitAnalytics = Analytics("fruit");

def render(_last):

    global _renderCount;
    _renderCount = _renderCount + 1;
    clear_screen();

    numpy.savetxt('tmp/data.txt', numpy.asarray(plotList), '%.01f', ', ');

    plot_scatter('tmp/data.txt', 20, 100, 23, 'π','green', 'Fruit Monitor');

    print("Mean fruit is",round(fruitAnalytics.getMean(),2),'per transaction');
    print("Fruit per second is",round(fruitAnalytics.catPerSecond(),2));
    print("Transactions per second is",round(fruitAnalytics.transPerSecond(),4))
    print("Runtime:", round(time.time() - fruitAnalytics.getStart(),2), 's')
    print("Frame:",_renderCount)

    os.remove('tmp/data.txt')

def handle_message(message, *args):
    """ Called whenever a message comes through the socket.

    Args:
        message (str): The message we just received
        *args: Any additional arguments received, likely will be empty
    """

    parsedMessage = json.loads(message);
    amount = parsedMessage['amount'];
    cart = parsedMessage['cart'];
    shopper = parsedMessage['shopper'];

    items = fruitAnalytics.transaction(cart);
    plotList.append([time.time(), items])
    render(items)

with SocketIO(SOCKET_HOST) as sock:
    global _renderCount;
    _renderCount = 0;

    # Set up our message handler
    sock.on('recvData', handle_message)
    # Join the "fruits" room
    sock.emit('ready', 'groceries')
    # Wait for messages to come through! Ctrl-C to quit
    print(time.ctime())

    sock.wait()
