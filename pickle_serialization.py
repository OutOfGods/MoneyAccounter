import json
import accounter
import pickle

def serialize(obj, file_name):
    """
    Encode obj to binary row using pickle write it into file.
    """
    with open(file_name, 'wb') as f:
        pickle.dump(obj, f)


def deserialize(file_name):
    """
    Decode from binary row to Python-object using pickle.
    """
    try:
        with open(file_name, 'rb') as f:
            obj = pickle.load(f)
        return obj
    except FileNotFoundError:
        print("File not found")


if __name__ == '__main__':
    acc = accounter.Accounter()
    acc.load_data()
    print(acc)
    print("")
    serialize(acc, 'accounter.pickle')
    acc = deserialize('accounter.pickle')
    print(acc)