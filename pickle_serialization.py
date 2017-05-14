import json
import accounter
import pickle

def serialize(obj, file_name):
    """
    Encode obj to binary row using pickle write it into file.
    """
    with open(file_name, 'wb') as f:
        pickle.dump(obj.account, f)


def deserialize(file_name):
    """
    Decode from binary row to Python-object using pickle.
    """
    try:
        with open(file_name, 'rb') as f:
            data = pickle.load(f)
        return data
    except FileNotFoundError:
        print("File not found")

