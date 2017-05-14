import json
import accounter
import pandas as pd

class AccounterEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, accounter.Accounter):
            rows_list = []
            for i in range(len(obj.account)):
                row_dict = {}
                row_dict['comment'] = obj.account.iloc[i]['comment']
                row_dict['date'] = str(obj.account.iloc[i]['date'])
                row_dict['value'] = int(obj.account.iloc[i]['value'])
                rows_list.append(row_dict)
            return rows_list
        return json.JSONEncoder.default(self, obj)


def serialize(obj, file_name):
    with open(file_name, 'w') as f:
        json.dump(obj, f, cls=AccounterEncoder)


def deserialize(file_name):
    try:
        with open(file_name) as f:
            lst = json.load(f)
            for record in lst:
                record['date'] = pd.Timestamp(record['date'])
            return accounter.Accounter(pd.DataFrame(lst))
    except FileNotFoundError:
        print("File not found")


if __name__ == '__main__':
    acc = accounter.Accounter()
    acc.load_data()
    print(acc)
    print("")
    serialize(acc, 'accounter.json')
    acc = deserialize('accounter.json')
    print(acc)

