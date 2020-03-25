from data_converter import FieldList


if __name__ == "__main__":
    
    params = {
        'key': 'status',
        'value': 10
    }
    
    fl = FieldList()

    print(fl.validatesData(params))
