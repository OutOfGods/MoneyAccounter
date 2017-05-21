import _pickle as pickle
import pandas as pd
import _datetime as dt
import configparser
import os

import pickle_serialization
import json_serialization
import yaml_serialization


class Accounter:
    """This class implements simple money accounter.
       You can use it for storing notes about your income and
       outcome, search notes and group them by their attributes."""
    def __init__(self, acc=pd.DataFrame(), data_file='accounter', config_file='configuration.ini'):
        """Create new Accounter object from existing DataFrame.
        >>> print(Accounter())
        List of notes is empty
        >>> print(Accounter(pd.DataFrame([{'date': pd.Timestamp("20170404"),
        ... 'value': 100, 'comment': 'new money'}])))
             comment       date  value
        0  new money 2017-04-04    100
        """
        self.account = acc
        self.data_file = data_file
        self.config_file = config_file

    def __str__(self):
        if len(self.account) == 0:
            return 'List of notes is empty'
        return str(self.account)

    def add_new_data(self, value, comment,
                     date=dt.datetime.now().strftime("%Y%m%d")):
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
           1    kupil shaurmu 2017-03-25    -45

           """
        day = pd.DataFrame([{'date': pd.Timestamp(date),
                             'value': int(value), 'comment': comment}])
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
        1    kupil shaurmu 2017-03-25    -45
        >>> acc.drop_data()
        >>> print(acc)
        List of notes is empty
        """
        self.account = pd.DataFrame()
        self.save_data()

    def get_income(self):
        """Return Accounter object only with notes where you had an income.
        >>> acc1 = Accounter(pd.DataFrame([
        ... {'date': pd.Timestamp("20170404"),
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': pd.Timestamp("20170404"),
        ... 'value': 250, 'comment': 'Neshta vernul dolg'},
        ... {'date': pd.Timestamp("20170404"),
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': pd.Timestamp("20170404"),
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
        ... {'date': pd.Timestamp("20170404"),
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': pd.Timestamp("20170404"),
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
        ... {'date': pd.Timestamp("20170404"),
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': pd.Timestamp("20170404"),
        ... 'value': 250, 'comment': 'Neshta vernul dolg'},
        ... {'date': pd.Timestamp("20170404"),
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': pd.Timestamp("20170404"),
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
        ... {'date': pd.Timestamp("20170404"),
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': pd.Timestamp("20170404"),
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
        >>> acc1 = Accounter(pd.DataFrame([
        ... {'date': pd.Timestamp("20170404"),
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': pd.Timestamp("20170404"),
        ... 'value': 250, 'comment': 'Neshta vernul dolg'},
        ... {'date': pd.Timestamp("20170404"),
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': pd.Timestamp("20170404"),
        ... 'value': -2000, 'comment': 'zaplatil za obschagu'}
        ... ]))
        >>> print(acc1)
                           comment       date  value
        0                new money 2017-04-04    100
        1       Neshta vernul dolg 2017-04-04    250
        2  kupil chai v happy cake 2017-04-04    -25
        3     zaplatil za obschagu 2017-04-04  -2000
        >>> print(acc1.get_by_comment("new money"))
             comment       date  value
        0  new money 2017-04-04    100
        >>> print(acc1.get_by_comment("not com"))
        List of notes is empty
        """
        if len(self.account) == 0:
            return Accounter()
        return Accounter(self.account[self.account.comment == comm])

    def get_by_date(self, date1, date2):
        """Return Accounter object with notes that have date attribute in given range.
        >>> acc1 = Accounter(pd.DataFrame([
        ... {'date': pd.Timestamp("20170404"),
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': pd.Timestamp("20170405"),
        ... 'value': 250, 'comment': 'Neshta vernul dolg'},
        ... {'date': pd.Timestamp("20170406"),
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': pd.Timestamp("20170407"),
        ... 'value': -2000, 'comment': 'zaplatil za obschagu'}
        ... ]))
        >>> print(acc1)
                           comment       date  value
        0                new money 2017-04-04    100
        1       Neshta vernul dolg 2017-04-05    250
        2  kupil chai v happy cake 2017-04-06    -25
        3     zaplatil za obschagu 2017-04-07  -2000
        >>> print(acc1.get_by_date("20170404", "20170405"))
                      comment       date  value
        0           new money 2017-04-04    100
        1  Neshta vernul dolg 2017-04-05    250
        >>> print(acc1.get_by_date("20170404", "20170404"))
             comment       date  value
        0  new money 2017-04-04    100
        """
        if len(self.account) == 0:
            return Accounter()
        return Accounter(self.account[(self.account.date >=
                                       pd.Timestamp(date1)) &
                                      (self.account.date <=
                                       pd.Timestamp(date2))])

    def get_income_by_range(self, from_value, to_value):
        """Return Accounter object with notes that have income in given range.
        >>> acc = Accounter(pd.DataFrame([
        ... {'date': pd.Timestamp('20170404'),
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': pd.Timestamp('20170404'),
        ... 'value': 250, 'comment': 'Neshta vernul dolg'},
        ... {'date': pd.Timestamp('20170404'),
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': pd.Timestamp('20170404'),
        ... 'value': -2000, 'comment': 'zaplatil za obschagu'}
        ... ]))
        >>> print(acc.get_income_by_range(200, 500))
                      comment       date  value
        1  Neshta vernul dolg 2017-04-04    250

        """
        if len(self.account) == 0:
            return Accounter()
        return Accounter(self.account[(self.account.value >= from_value) &
                                      (self.account.value <= to_value)])

    def get_outcome_by_range(self, from_value, to_value):
        """Return Accounter object with notes that have outcome in given range.
        >>> acc = Accounter(pd.DataFrame([
        ... {'date': pd.Timestamp('20170404'),
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': pd.Timestamp('20170404'),
        ... 'value': 250, 'comment': 'Neshta vernul dolg'},
        ... {'date': pd.Timestamp('20170404'),
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': pd.Timestamp('20170404'),
        ... 'value': -2000, 'comment': 'zaplatil za obschagu'}
        ... ]))
        >>> print(acc.get_outcome_by_range(2000, 4000))
                        comment       date  value
        3  zaplatil za obschagu 2017-04-04  -2000
        """
        if len(self.account) == 0:
            return 0
        return Accounter(self.account[(self.account.value >= -to_value) &
                                      (self.account.value <= -from_value)])

    def group_by_comment(self):
        """Return Accounter object with notes grouped by comment.
        >>> acc1 = Accounter(pd.DataFrame([
        ... {'date': pd.Timestamp("20170404"),
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': pd.Timestamp("20170405"),
        ... 'value': 250, 'comment': 'new money'},
        ... {'date': pd.Timestamp("20170406"),
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': pd.Timestamp("20170407"),
        ... 'value': -2000, 'comment': 'zaplatil za obschagu'}
        ... ]))
        >>> print(acc1)
                           comment       date  value
        0                new money 2017-04-04    100
        1                new money 2017-04-05    250
        2  kupil chai v happy cake 2017-04-06    -25
        3     zaplatil za obschagu 2017-04-07  -2000
        >>> print(acc1.group_by_comment())
                                 value
        comment
        kupil chai v happy cake    -25
        new money                  350
        zaplatil za obschagu     -2000
        """
        if len(self.account) == 0:
            return Accounter()
        return Accounter(self.account.groupby('comment').sum())

    def group_by_date(self):
        """Return Accounter object with notes grouped by date.
        >>> acc1 = Accounter(pd.DataFrame([
        ... {'date': "20170404",
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': "20170404",
        ... 'value': 250, 'comment': 'new money'},
        ... {'date': "20170405",
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': "20170405",
        ... 'value': -2000, 'comment': 'zaplatil za obschagu'}
        ... ]))
        >>> print(acc1)
                           comment      date  value
        0                new money  20170404    100
        1                new money  20170404    250
        2  kupil chai v happy cake  20170405    -25
        3     zaplatil za obschagu  20170405  -2000
        >>> print(acc1.group_by_date())
                  value
        date
        20170404    350
        20170405  -2025
        """
        if len(self.account) == 0:
            return Accounter()
        return Accounter(self.account.groupby('date').sum())

    def print_data(self):
        """Show all notes in accounter.
        >>> Accounter(pd.DataFrame([{'date': pd.Timestamp('20170404'),
        ... 'comment': 'new money', 'value': 50}])).print_data()
        **************************************************
             comment       date  value
        0  new money 2017-04-04     50
        >>> Accounter().print_data()
        **************************************************
        List of notes is empty
        """
        print('*'*50)
        print(self)

    def sort_by_date(self):
        """Sort notes using date as key.
        >>> acc = Accounter(pd.DataFrame([
        ... {'date': pd.Timestamp('20170404'),
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': pd.Timestamp('20170402'),
        ... 'value': 250, 'comment': 'Neshta vernul dolg'},
        ... {'date': pd.Timestamp('20170411'),
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': pd.Timestamp('20170408'),
        ... 'value': -2000, 'comment': 'zaplatil za obschagu'}
        ... ]))
        >>> print(acc)
                           comment       date  value
        0                new money 2017-04-04    100
        1       Neshta vernul dolg 2017-04-02    250
        2  kupil chai v happy cake 2017-04-11    -25
        3     zaplatil za obschagu 2017-04-08  -2000
        >>> acc.sort_by_date()
        >>> print(acc)
                           comment       date  value
        1       Neshta vernul dolg 2017-04-02    250
        0                new money 2017-04-04    100
        3     zaplatil za obschagu 2017-04-08  -2000
        2  kupil chai v happy cake 2017-04-11    -25
        """
        if len(self.account) == 0:
            return Accounter()
        self.account = self.account.sort_values(['date'])

    def sort_by_indexes(self):
        self.account = self.account.sort_index()

    def get_income_sum(self):
        """Return sum of all incomes.
        >>> acc1 = Accounter(pd.DataFrame([
        ... {'date': "20170404",
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': "20170403",
        ... 'value': 250, 'comment': 'new money'},
        ... {'date': "20170402",
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': "20170405",
        ... 'value': -2000, 'comment': 'zaplatil za obschagu'}
        ... ]))
        >>> print(acc1)
                           comment      date  value
        0                new money  20170404    100
        1                new money  20170403    250
        2  kupil chai v happy cake  20170402    -25
        3     zaplatil za obschagu  20170405  -2000
        >>> print(acc1.get_income_sum())
        350
        """
        if len(self.account) == 0:
            return 0
        return self.account[self.account.value > 0].value.sum()

    def get_outcome_sum(self):
        """Return sum of all outcomes.
        >>> acc1 = Accounter(pd.DataFrame([
        ... {'date': "20170404",
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': "20170403",
        ... 'value': 250, 'comment': 'new money'},
        ... {'date': "20170402",
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': "20170405",
        ... 'value': -2000, 'comment': 'zaplatil za obschagu'}
        ... ]))
        >>> print(acc1)
                           comment      date  value
        0                new money  20170404    100
        1                new money  20170403    250
        2  kupil chai v happy cake  20170402    -25
        3     zaplatil za obschagu  20170405  -2000
        >>> print(acc1.get_outcome_sum())
        -2025
        """
        if len(self.account) == 0:
            return 0
        return self.account[self.account.value < 0].value.sum()

    def get_sum(self):
        """Return sum of all income and outcome.
        >>> acc1 = Accounter(pd.DataFrame([
        ... {'date': "20170404",
        ... 'value': 100, 'comment': 'new money'},
        ... {'date': "20170403",
        ... 'value': 250, 'comment': 'new money'},
        ... {'date': "20170402",
        ... 'value': -25, 'comment': 'kupil chai v happy cake'},
        ... {'date': "20170405",
        ... 'value': -2000, 'comment': 'zaplatil za obschagu'}
        ... ]))
        >>> print(acc1)
                           comment      date  value
        0                new money  20170404    100
        1                new money  20170403    250
        2  kupil chai v happy cake  20170402    -25
        3     zaplatil za obschagu  20170405  -2000
        >>> print(acc1.get_sum())
        -1675"""
        if len(self.account) == 0:
            return 0
        return self.account.value.sum()

    def save_data(self):
        """Serialize data into file using method specified in configuration file."""
        config = configparser.ConfigParser()
        config.read(self.config_file)
        if 'Serialization' in config:
            if config['Serialization']['Method'] == 'pickle':
                with open(self.data_file + '.pickle', 'wb') as f:
                        pickle_serialization.serialize(self, f)
            elif config['Serialization']['Method'] == 'json':
                with open(self.data_file + '.json', 'w') as f:
                    json_serialization.serialize(self, f)
            elif config['Serialization']['Method'] == 'yaml':
                with open(self.data_file + '.yaml', 'w') as f:
                    yaml_serialization.serialize(self, f)

    def load_data(self):
        """Load data from file."""
        config = configparser.ConfigParser()
        config.read(self.config_file)
        data_files = []
        data_files.append(self.data_file + '.pickle')
        data_files.append(self.data_file + '.json')
        data_files.append(self.data_file + '.yaml')
        print(data_files)
        last_changed_file = max(data_files, key=lambda a: os.path.getmtime(a))
        if last_changed_file == self.data_file + '.pickle':
            try:
                with open(last_changed_file, 'rb') as f:
                    self.account = pickle_serialization.deserialize(f)
            except FileNotFoundError:
                print('Pickle file with data not found')
        elif last_changed_file == self.data_file + '.json':
            try:
                with open(last_changed_file, 'r') as f:
                    self.account = json_serialization.deserialize(f)
            except FileNotFoundError:
                print('JSON file with data not found')
        elif last_changed_file == self.data_file + '.yaml':
            try:
                with open(last_changed_file, 'r') as f:
                    self.account = yaml_serialization.deserialize(f)
            except FileNotFoundError:
                print('YAML file with data not found')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
