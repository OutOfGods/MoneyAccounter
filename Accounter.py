import _pickle as pickle
import pandas as pd
import matplotlib.pyplot as plt
import _datetime as dt

class Accounter:
    def add_new_data(self, value, comment, date=dt.datetime.now().strftime("%Y%m%d")):
        day = pd.DataFrame([{'date': pd.Timestamp(date), 'value': value, 'comment': comment}])
        self.account = self.account.append(day)

    def save_data(self):
        try:
            with open('data.pickle', 'wb') as f:
                pickle.dump(self.account, f)
        except FileNotFoundError:
            print("File not found")

    def load_data(self):
        try:
            with open('data.pickle', 'rb') as f:
                self.account = pickle.load(f)
        except FileNotFoundError:
            print("File not found")
            self.account = acc

    def __init__(self, acc=pd.DataFrame()):
        self.account = acc

    def drop_data(self):
        self.account = pd.DataFrame()
        self.save_data()

    def get_income(self):
        return Accounter(self.account[self.account.value > 0])

    def get_expenses(self):
        return Accounter(self.account[self.account.value < 0])

    def get_by_comment(self, comm):
        return Accounter(self.account[self.account.comment == comm])

    def get_by_date(self, date1, date2):
        return Accounter(self.account[(self.account.date >= pd.Timestamp(date1)) &
                                      (self.account.date <= pd.Timestamp(date2))])

    def group_by_comment(self):
        return Accounter(self.account.groupby('comment').sum())

    def group_by_date(self):
        return Accounter(self.account.groupby('date').sum())

    def print_data(self):
        print('*'*50)
        print(self.account)

    def sort_by_date(self):
        self.account = self.account.sort_values(['date'])

    def get_sum(self):
        return self.account.value.sum()

if __name__ == "__main__":
    acc = Accounter()
    acc.drop_data()
    print('unsorted:')
    acc.add_new_data(1100, 'stepuha', '20170321')
    acc.add_new_data(-200, 'eda')
    acc.add_new_data(999, 'eee babos', '20170322')
    acc.add_new_data(-500, 'na pivandrii')
    acc.add_new_data(400, 'nashel na ulichke', '20170320')
    acc.add_new_data(-200, 'eda', '20140320')
    acc.add_new_data(-10, 'proebal', '20170319')
    acc.add_new_data(123, 'test123', '20150320')
    acc.print_data()
    print('\nsorted by date:')
    acc.sort_by_date()
    acc.save_data()
    acc.print_data()
    print('\nacc.get_by_date(\'20170320\', \'20170326\').get_expenses().print_data():')
    acc.get_by_date('20170320', '20170326').get_expenses().print_data()
    print('\nacc.get_by_comment(\'eda\').print_data():')
    acc.get_by_comment('eda').print_data()
    print('\nacc.group_by_comment().print_data():')
    acc.group_by_comment().print_data()
    print('\nacc.group_by_date().print_data():')
    acc.group_by_date().print_data()
    print('*'*20, "print some summ:")
    print("Sum for comment *eda*: ", acc.get_by_comment('eda').get_sum())
    print("Sum for all table: ", acc.get_sum())

