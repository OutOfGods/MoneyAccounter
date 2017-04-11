import _pickle as pickle
import pandas as pd
# import matplotlib.pyplot as plt
import _datetime as dt


class Accounter:
    """This class implements simple money accounter.
       You can use it for storing notes about your income and
       outcome, search notes and group them by their attributes."""
    def __init__(self, acc=pd.DataFrame()):
        """Create new Accounter object from existing DataFrame.
        >>> print(Accounter())
        List of notes is empty
        >>> print(Accounter(pd.DataFrame([{'date': pd.Timestamp(dt.datetime.now().strftime("%Y%m%d")),
        ... 'value': 100, 'comment': 'new money'}])))
             comment       date  value
        0  new money 2017-04-04    100
        """
        self.account = acc

    def __str__(self):
        if len(self.account) == 0:
            return 'List of notes is empty'
        return str(self.account)

    def add_new_data(self, value, comment, date=dt.datetime.now()):
        """Create new note from given value, date and comment.
           Date is read automatically from OS time.
           Date is python date.
           >>> acc = Accounter()
           >>> acc.add_new_data(25, 'nashel v kurtke', '20170321')
           >>> print(acc)
                      comment       date  value
           0  nashel v kurtke 2017-03-21     25
           >>> acc.add_new_data(-45, 'kupil shaurmu', '20170325')
           >>> print(acc)
                      comment       date  value
           0  nashel v kurtke 2017-03-21     25
           0    kupil shaurmu 2017-03-25    -45

           """
        day = pd.DataFrame([{'date': pd.Timestamp(date.strftime("%Y%m%d")), 'value': value, 'comment': comment}])
        self.account = self.account.append(day)
        self.account = self.account.reset_index(drop=True)

    def drop_data(self):
        """Delete all notes.
           >>> acc = Accounter()
           >>> acc.add_new_data(25, 'nashel v kurtke', '20170321')
           >>> acc.add_new_data(-45, 'kupil shaurmu', '20170325')
           >>> print(acc)
                      comment       date  value
           0  nashel v kurtke 2017-03-21     25
           0    kupil shaurmu 2017-03-25    -45
           >>> acc.drop_data()
           >>> print(acc)
           List of notes is empty
        """
        self.account = pd.DataFrame()
        self.save_data()

    def get_income(self):
        """Return Accounter object only with notes where you had an income.
        >>> acc1 = Accounter(pd.DataFrame([
        ... {'date': pd.Timestamp(dt.datetime.now().strftime("%Y%m%d")),
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': pd.Timestamp(dt.datetime.now().strftime("%Y%m%d")),
        ... 'value': 250, 'comment': 'Neshta vernul dolg'},
        ... {'date': pd.Timestamp(dt.datetime.now().strftime("%Y%m%d")),
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': pd.Timestamp(dt.datetime.now().strftime("%Y%m%d")),
        ... 'value': -2000, 'comment': 'zaplatil za obschagu'}
        ... ]))
        >>> print(acc1)
                           comment       date  value
        0                new money 2017-04-04    100
        1       Neshta vernul dolg 2017-04-04    250
        2  kupil chai v happy cake 2017-04-04    -25
        3     zaplatil za obschagu 2017-04-04  -2000
        >>> print(acc1.get_income())
                      comment       date  value
        0           new money 2017-04-04    100
        1  Neshta vernul dolg 2017-04-04    250
        >>> acc2 = Accounter(pd.DataFrame([
        ... {'date': pd.Timestamp(dt.datetime.now().strftime("%Y%m%d")),
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': pd.Timestamp(dt.datetime.now().strftime("%Y%m%d")),
        ... 'value': -2000, 'comment': 'zaplatil za obschagu'}
        ... ]))
        >>> print(acc2.get_income())
        List of notes is empty
        >>> acc1.drop_data()
        >>> print(acc1.get_income())
        List of notes is empty
        """

        if len(self.account) == 0:
            return Accounter()
        return Accounter(self.account[self.account.value > 0])

    def get_outcome(self):
        """Return Accounter object only with notes where you had an outcome.
        >>> acc1 = Accounter(pd.DataFrame([
        ... {'date': pd.Timestamp(dt.datetime.now().strftime("%Y%m%d")),
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': pd.Timestamp(dt.datetime.now().strftime("%Y%m%d")),
        ... 'value': 250, 'comment': 'Neshta vernul dolg'},
        ... {'date': pd.Timestamp(dt.datetime.now().strftime("%Y%m%d")),
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': pd.Timestamp(dt.datetime.now().strftime("%Y%m%d")),
        ... 'value': -2000, 'comment': 'zaplatil za obschagu'}
        ... ]))
        >>> print(acc1)
                           comment       date  value
        0                new money 2017-04-04    100
        1       Neshta vernul dolg 2017-04-04    250
        2  kupil chai v happy cake 2017-04-04    -25
        3     zaplatil za obschagu 2017-04-04  -2000
        >>> print(acc1.get_outcome())
                           comment       date  value
        2  kupil chai v happy cake 2017-04-04    -25
        3     zaplatil za obschagu 2017-04-04  -2000
        >>> acc2 = Accounter(pd.DataFrame([
        ... {'date': pd.Timestamp(dt.datetime.now().strftime("%Y%m%d")),
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': pd.Timestamp(dt.datetime.now().strftime("%Y%m%d")),
        ... 'value': 250, 'comment': 'Neshta vernul dolg'}
        ... ]))
        >>> print(acc2.get_outcome())
        List of notes is empty
        >>> acc1.drop_data()
        >>> print(acc1.get_outcome())
        List of notes is empty
        """

        if len(self.account) == 0:
            return Accounter()
        return Accounter(self.account[self.account.value < 0])

    def get_by_comment(self, comm):
        """Return Accounter object with notes that have given comment.
        """
        return Accounter(self.account[self.account.comment == comm])

    def get_by_date(self, date1, date2):
        """Return Accounter object with notes that have date attribute in given range."""
        return Accounter(self.account[(self.account.date >= pd.Timestamp(date1)) &
                                      (self.account.date <= pd.Timestamp(date2))])

    def get_income_by_range(self, from_value, to_value):
        """Return Accounter object with notes that have income in given range."""
        return Accounter(self.account[(self.account.value >= from_value) &
                                      (self.account.date <= to_value)])

    def get_outcome_by_range(self, from_value, to_value):
        """Return Accounter object with notes that have outcome in given range."""
        return Accounter(self.account[(self.account.value >= -to_value) &
                                      (self.account.date <= -from_value)])

    def group_by_comment(self):
        """Return Accounter object with notes grouped by comment."""
        return Accounter(self.account.groupby('comment').sum())

    def group_by_date(self):
        """Return Accounter object with notes grouped by date."""
        return Accounter(self.account.groupby('date').sum())

    def print_data(self):
        """Show all notes in accounter."""
        print('*'*50)
        print(self.account)

    def sort_by_date(self):
        """Sort notes using date as key."""
        self.account = self.account.sort_values(['date'])

    def sort_by_indexes(self):
        self.account = self.account.sort_index()

    def get_income_sum(self):
        """Return sum of all incomes."""
        self.account[self.account.value > 0].value.sum()

    def get_outcome_sum(self):
        """Return sum of all outcomes."""
        self.account[self.account.value < 0].value.sum()

    def get_sum(self):
        """Return sum of all income and outcome."""
        return self.account.value.sum()

    def save_data(self):
        """Save data into binary file using _pickle."""
        try:
            with open('data.pickle', 'wb') as f:
                pickle.dump(self.account, f)
                print(self.account)
        except FileNotFoundError:
            print("File not found")

    def load_data(self):
        """Load data from binary file using _pickle."""
        try:
            with open('data.pickle', 'rb') as f:
                self.account = pickle.load(f)
        except FileNotFoundError:
            print("File not found")
            self.account = acc

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    # acc = Accounter()
    # acc.drop_data()
    # print('unsorted:')
    # acc.add_new_data(1100, 'stepuha', '20170321')
    # acc.add_new_data(-200, 'eda')

    # acc.add_new_data(999, 'eee babos', '20170322')
    # acc.add_new_data(-500, 'na pivandrii')
    # acc.add_new_data(400, 'nashel na ulichke', '20170320')
    # acc.add_new_data(-200, 'eda', '20140320')
    # acc.add_new_data(-10, 'proebal', '20170319')
    # acc.add_new_data(123, 'test123', '20150320')
    # acc.print_data()
    # print('\nsorted by date:')
    # acc.sort_by_date()
    # acc.save_data()
    # acc.print_data()
    # print('\nacc.get_by_date(\'20170320\', \'20170326\').get_outcome().print_data():')
    # acc.get_by_date('20170320', '20170326').get_outcome().print_data()
    # print('\nacc.get_by_comment(\'eda\').print_data():')
    # acc.get_by_comment('eda').print_data()
    # print('\nacc.group_by_comment().print_data():')
    # acc.group_by_comment().print_data()
    # print('\nacc.group_by_date().print_data():')
    # acc.group_by_date().print_data()
    # print('*'*20, "print some summ:")
    # print("Sum for comment *eda*: ", acc.get_by_comment('eda').get_sum())
    # print("Sum for all table: ", acc.get_sum())

