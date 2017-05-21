import json
import accounter
import pickle

def serialize(obj, file):
    """
    Encode obj to binary row using pickle write it into file.
    """
    pickle.dump(obj.account, file)


def deserialize(file):
    """
    Decode from binary row to Python-object using pickle.
    """
    data = pickle.load(file)
    return data

