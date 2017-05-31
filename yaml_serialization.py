import accounter
import pandas as pd
import yaml


class YAMLSerializer:
    def serialize(self, obj, file):
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

        yaml.dump(rows_list, file)

    def deserialize(self, file):
        """
        Decode from yaml file to Python-object.
        """
        obj = yaml.safe_load(file)
        if obj is not None:
            for record in obj:
                record['date'] = pd.Timestamp(record['date'])
            return pd.DataFrame(obj)
        return pd.DataFrame()
