''' Object Oriented tests. '''

from statistics import mean

class Scoop(object):
    ''' simple scoop class '''
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f'Scoop of {self.flavor}'


class Bowl(object):
    MAX_SCOOPS = 3 
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        self.scoops.extend(args[:Bowl.MAX_SCOOPS - len(self.scoops)])

    def flavors(self):
        return " ".join([scoop.flavor for scoop in self.scoops])

    def __repr__(self):
        return 'Bowl with:\n'+"\n".join([f'\t{i+1}) {flav}' 
            for i,flav in enumerate(self.scoops)])

class BigBowl(Bowl):
    MAX_SCOOPS = 5
    def add_scoops(self, *args):
        self.scoops.extend(args[:BigBowl.MAX_SCOOPS - len(self.scoops)])

class BankAccount(object):
    ''' Allows depostit and withdraws '''
    total_assets = 0
    def __init__(self):
        self.transactions = []

    def deposit(self, amount):
        self.transactions.append(amount)
        BankAccount.total_assets += amount


    def withdraw(self, amount):
        if amount < 0:
            raise ValueError('Widthdrawl must be greater than 0')
        else:
            self.transactions.append(-1*amount)
            BankAccount.total_assets -= amount

    def balance_rep(self):
        deposits = [n for n in self.transactions if n > 0]
        withdrawls = [n for n in self.transactions if n < 0]
        print(f'Deposit  : {len(deposits)} transactions, avg: {mean(deposits):.2f}')
        print(f'Withdrawl: {len(withdrawls)} transactions, avg: {mean(withdrawls):.2f}')
        print(f'Balance: {sum(self.transactions)}')

    def balance(self):
        return sum(self.transactions)

class Loan(object):
    def __init__(self, amount):
        if BankAccount.total_assets - amount >=0:
            self.outstanding = amount
            BankAccount.total_assets -= amount
        else:
            raise ValueError('Bank does not have enough money.')

    def repay(self, amount):
        self.outstanding -= amount
        BankAccount.total_assets += amount


class Person(object):
    ''' Simple Person '''
    def __init__(self, name, email, address, phone):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.accounts = []

    def greet(self):
        print (f"Hello, {self.name}")

    def add_account(self, account):
        self.accounts.append(account)

    def all_balances(self):
        return [account.balance() for account in self.accounts ]

    def current_total_balance(self):
        if self.all_balances():
            return sum(self.all_balances())

    def average_transaction_amount(self):
        return mean(self.all_balances())

    def __repr__(self):
        return f'{self.name:10s} {self.email:20s} {self.address:15s} {self.phone}'

class VerbosePerson(Person):
    def greet(self):
        print(f'Well this is great to see you {self.name}')

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
                del(self.cart[name])
        else:
            raise ValueError(f'{name} not in cart.')
    
    def __len__(self):
        return sum(self.cart[name]['quantity'] for name in self.cart)

    def total(self):
        return sum([self.cart[name]['price'] * self.cart[name]['quantity'] for name in self.cart])

    def __str__(self):
        basket_total = 0 
        basket_items=[]
        for name, items in self.cart.items():
            price, quantity = items['price'], items['quantity']
            total = price * quantity 
            basket_total += total 
            basket_items.append(f'{name:10} {quantity:3d} ${price:.2f} ${total:.2f}')
        return "\n".join(basket_items +["-"*40, f'Total:{" "*15} ${basket_total:.2f}'])


class OnlineShoppingCart(ShoppingCart):
    def total(self):
        return super().total()*1.05+10

if __name__ == '__main__':
    S1 = Scoop('chocolate')
    S2 = Scoop('vanilla')
    S3 = Scoop('coffee')

    print(S1)

    B = Bowl()
    B.add_scoops(S1, S2)
    B.add_scoops(S3,S1, S2, S3)
    print(B.flavors())

    print(B)

    BB = BigBowl()
    BB.add_scoops(S1, S2)
    BB.add_scoops(S3,S1, S2, S3)
    print(f'Big Bowl: {BB.flavors()}')


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
    
    pv = VerbosePerson(*PEOPLE[0])
    pv.greet()

    for person in plist:
        print(person)
    plist[0].email = 'gordon@shephard.org'
    for person in plist:
        print(person.email)

    BA1 = BankAccount()
    BA2 = BankAccount()

    BA1.deposit(500)
    BA1.withdraw(20)
    BA2.deposit(700)
    BA2.deposit(32)

    P1 = plist[0]
    P2 = plist[1]

    P1.add_account(BA1)
    P1.add_account(BA2)
    print(f'All Balance: {P1.all_balances()}')
    print(f'Total: {P1.current_total_balance()}')
    print(f'Avg  : {P1.average_transaction_amount()}')


    sc = ShoppingCart()
    sc.add('book', 30, 1)    # name, price-per-unit, quantity
    sc.add('toothbrush', 3, 4)
    sc.remove('toothbrush')   # removes one toothbrush -- or removes
                              # the item altogether if the quantity is 0
    
    print(f'Total Cart: {sc.total()}')  # returns the total price of items in the shopping cart
    print(f"Total Items: {len(sc)}")
    print(sc)

    osc = OnlineShoppingCart()
    osc.add('book',50,1)
    osc.add('car',50,2)
    osc.remove('car')
    print(f'Total Online: {osc.total()}')



    l1 = Loan(500)
    l2 = Loan(200)
    #l3 = Loan(700)  # raises an exception -- ValueError to indicate no money
    l1.repay(500)
    l3 = Loan(700)  # now it'll work, because the bank has sufficient funds

    print(f'Bank Assets: {BankAccount.total_assets}')
   

    P1.greet()