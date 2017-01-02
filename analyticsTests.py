from Analytics import Analytics;
import time

cart = [{'name': 'water', 'type': 'beverage', 'quantity': 2}, {'name': 'orange', 'type': 'fruit', 'quantity': 10}, {'name': 'apple', 'type': 'fruit', 'quantity': 7}, {'name': 'popcorn', 'type': 'snack', 'quantity': 5}]

def analyticsCategoryTest():
    print("Running analytics category test");
    a = Analytics("Baseball");
    cat = a.getCategory();
    if("Baseball" in cat):
        return 'pass';
    else:
        return 'fail';

def analyticsTransactionTest(_type, _quantity):
    print("Running analytics transaction test for", _type, _quantity);
    a = Analytics(_type);
    items = a.transaction(cart);
    if(items == _quantity):
        return 'pass';
    else:
        return 'fail';

def analyticsMeanTest():
    print("Running analytics mean test");
    a = Analytics('beverage');
    a.transaction(cart);
    if(a.getMean() == 2):
        return 'pass'
    else:
        return 'false'

def analyticsPerSecondTest():
    print("Running analytics per sec test");
    a = Analytics('fruit');
    a.transaction(cart);
    time.sleep(1);
    ps = a.perSecond();
    if(round(ps,0) == 17):
        return 'pass';
    else:
        return 'false';



print(analyticsCategoryTest());
print(analyticsTransactionTest("beverage", 2));
print(analyticsTransactionTest("snack", 5));
print(analyticsMeanTest());
print(analyticsPerSecondTest());
