import calendar
import time

class Analytics:
    ''' Analytics class that accepts arbitrary data'''

    def __init__(self, category):
      self.category = category;
      self.start = time.time()
      self.items = 0;
      self.totalItems = 0;
      self.transactions = 0;

    def getCategory(self):
        return self.category;

    def getStart(self):
        return self.start;

    def transaction(self, cart):
        self.transactions += 1;
        itemsInCart = 0;

        # Search through the
        for item in cart:
            self.totalItems += item['quantity'];
            if(self.category in item['type']):
                itemsInCart += item['quantity'];

        self.items += itemsInCart;
        return itemsInCart;


    def getMean(self):
        return self.items / self.transactions;

    def catPerSecond(self):
        now = time.time()
        timeElapsed = now - self.start;
        return self.items / timeElapsed;

    def transPerSecond(self):
        now = time.time();
        timeElapsed = now - self.start;
        return self.transactions / timeElapsed;
