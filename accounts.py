import datetime
import pytz

class Account:
    """ Simple account with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.now(datetime.UTC)
        return utc_time    #pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print(f"Account created for {self._name} ")
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more then your account balance.")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.__balance}")

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, datetime.datetime.now(datetime.UTC), datetime.datetime.now()))



if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    #tim.show_balance()
    tim.withdraw(500)
    #tim.show_balance()

    tim.withdraw(2000)
    tim.show_transactions()

    steph = Account("Steph", 800)
    steph.__balance = 200
    steph.balance = 200
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    steph.show_balance()
    print(steph.__dict__)
    steph._Account__balance = 40

    steph.show_balance()
