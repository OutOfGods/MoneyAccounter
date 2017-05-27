import json
import accounter
import pandas as pd

class AccounterEncoder(json.JSONEncoder):
    """Extension for json.JSONEncoder class which can encode
       objects of type Accounter.
    """
    def default(self, obj):
        """
        Extension for json.JSONEncoder.default function with adding
        ability to encode objects of type Accounter.
        """
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


def serialize(obj, file):
    """
    Encode obj to json format and write it into file.
    """
    json.dump(obj, file, cls=AccounterEncoder)


def deserialize(file):
    """
    Decode from json file to Python-object.
    """
    lst = json.load(file)
    for record in lst:
        record['date'] = pd.Timestamp(record['date'])
    return pd.DataFrame(lst)



