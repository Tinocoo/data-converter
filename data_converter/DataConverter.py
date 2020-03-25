from datetime import datetime
from json import loads


class DataConverter(object):

    def __init__(self):
        self.type_data = {
            'absolute': lambda value: abs(value),
            'boolean': lambda value: bool(value),
            'date': lambda value: datetime.strptime(value, '%Y-%m-%d'),
            'datetime': lambda value: datetime.strptime(value, '%Y-%m-%d %H:%M:%S'),
            'float': lambda value: float(value),
            'integer': lambda value: int(value),
            'json': lambda value: loads(value),
            'list': lambda value: list(value),
            'round': lambda value: round(value),
            'string': lambda value: str(value),
            'time': lambda value: datetime.strptime(value, '%H:%M:%S').time()
        }

    def converter(self, params, dict_data):
        
        config_data = list(filter(lambda d: d['key'] == params['key'], dict_data))
        
        try:
            #Tamanho da variavel
            len_data = config_data[0]['len']
            
            #Criando objeto para tipagem de dados
            converter = self.type_data.get(config_data[0]['type'])
            
            #Valor convertido da variavel
            if params['value'] is None or params['value'] == None:
                value = params['value']
            else:
                value = converter(params['value'])
            
            result , message = 'ok', 'success'
            if len_data is not None:
                if   len(value) > len_data:
                    result, message = 'error', 'field size exceeded'
                
            data = {'result': result, 'data':value, 'message': message}

        except Exception as error:
            data = {'result': 'error', 'data':None, 'message': str(error)}
        
        return data 
