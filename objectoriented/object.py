''' Object Oriented tests. '''

from statistics import mean

class Scoop(object):
    ''' simple scoop class '''
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl(object):
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        self.scoops.extend(args)

    def flavors(self):
        return " ".join([scoop.flavor for scoop in self.scoops])


class BankAccount(object):
    ''' Allows depostit and withdraws '''
    def __init__(self):
        self.transactions = []

    def deposit(self, amount):
        self.transactions.append(amount)

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError('Widthdrawl must be greater than 0')
        else:
            self.transactions.append(-1*amount)

    def balance_rep(self):
        deposits = [n for n in self.transactions if n > 0]
        withdrawls = [n for n in self.transactions if n < 0]
        print(f'Deposit  : {len(deposits)} transactions, avg: {mean(deposits):.2f}')
        print(f'Withdrawl: {len(withdrawls)} transactions, avg: {mean(withdrawls):.2f}')
        print(f'Balance: {sum(self.transactions)}')

    def balance(self):
        return sum(self.transactions)


class Person(object):
    ''' Simple Person '''
    def __init__(self, name, email, address, phone):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def all_balances(self):
        return [account.balance() for account in self.accounts ]

    def current_total_balance(self):
        if self.all_balances():
            return sum(self.all_balances())

    def __repr__(self):
        return f'{self.name:10s} {self.email:20s} {self.address:15s} {self.phone}'

class ShoppingCart(object):
    def __init__(self):
        self.cart = {}

    def add(self,name, price, quantity):
        if name in self.cart:
            self.cart[name]['quantity'] += quantity
        else:
            self.cart[name] = {'price':price, 'quantity': quantity}

    def remove(self,name):
        if name in self.cart:
            self.cart[name]['quantity'] -= 1
            if self.cart[name]['quantity'] == 0:
                self.cart.pop(name)
        else:
            raise ValueError(f'{name} not in cart.')

    def total(self):
        return sum([self.cart[name]['price'] * self.cart[name]['quantity'] for name in self.cart])


if __name__ == '__main__':
    S1 = Scoop('chocolate')
    S2 = Scoop('vanilla')
    S3 = Scoop('coffee')

    B = Bowl()
    B.add_scoops(S1, S2)
    B.add_scoops(S3)
    print(B.flavors())

    print(S1.flavor)
    for scoop in [S1, S2, S3]:
        print(scoop.flavor)

    PEOPLE = [ ['gordon','gordon@x.com','ann arbor','555-123-4456'],
               ['joe','joe@gmail.com','briar wood','333-212-3323'],
               ['jack', 'jack@hotmail.com','ypsi','999-232-4232'],
               ['nate','nate@xerox.com','bell harbor','393-284-4839']
               ]

    plist = []
    for p in PEOPLE:
        plist.append(Person(*p))
    
    for person in plist:
        print(person)
    plist[0].email = 'gordon@shephard.org'
    for person in plist:
        print(person.email)

    BA1 = BankAccount()
    BA2 = BankAccount()

    BA1.deposit(5)
    BA1.withdraw(2)
    BA2.deposit(9)
    BA2.deposit(32)

    P1 = plist[0]
    P2 = plist[1]

    P1.add_account(BA1)
    P1.add_account(BA2)
    print(f'All Balance: {P1.all_balances()}')
    print(f'Total: {P1.current_total_balance()}')


    sc = ShoppingCart()
    sc.add('book', 30, 1)    # name, price-per-unit, quantity
    sc.add('toothbrush', 3, 4)
    sc.remove('toothbrush')   # removes one toothbrush -- or removes
                              # the item altogether if the quantity is 0
    
    sc.total()  # returns the total price of items in the shopping cart




   
   