import accounter
import pandas as pd
import yaml

def serialize(obj, file_name):
    """
    Encode obj to yaml format and write it into file.
    """
    rows_list = []
    for i in range(len(obj.account)):
        row_dict = {}
        row_dict['comment'] = obj.account.iloc[i]['comment']
        row_dict['date'] = str(obj.account.iloc[i]['date'])
        row_dict['value'] = int(obj.account.iloc[i]['value'])
        rows_list.append(row_dict)
    with open(file_name, 'w') as f:
        yaml.dump(rows_list, f)


def deserialize(file_name):
    """
    Decode from yaml file to Python-object.
    """
    try:
        with open(file_name) as f:
            obj = yaml.safe_load(f)
            for record in obj:
                record['date'] = pd.Timestamp(record['date'])
            return accounter.Accounter(pd.DataFrame(obj))
    except FileNotFoundError:
        print("File not found")


if __name__ == '__main__':
    acc = accounter.Accounter()
    acc.load_data()
    print(acc)
    print("")
    serialize(acc, 'accounter.yaml')
    acc = deserialize('accounter.yaml')
    print(acc)
