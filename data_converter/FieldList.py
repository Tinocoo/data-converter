from . import DataConverter

class FieldList(DataConverter):

     def validatesData(self, params):

        dict_data = [
            {'key': 'name', 'type': 'string', 'len': 150},
            {'key': 'document', 'type': 'string', 'len': 35},
            {'key': 'date_of_birth', 'type': 'date', 'len': None},
            {'key': 'address_01', 'type': 'string', 'len': 150},
            {'key': 'number', 'type': 'integer', 'len': None},
            {'key': 'district', 'type': 'string', 'len': 150},
            {'key': 'city', 'type': 'string', 'len': 150},
            {'key': 'province', 'type': 'string', 'len': 50},
            {'key': 'country', 'type': 'string', 'len': 50},
            {'key': 'email_01', 'type': 'string', 'len': 150},
            {'key': 'email_02', 'type': 'string', 'len': 150},
            {'key': 'email_03', 'type': 'string', 'len': 150},
            {'key': 'prefix_01', 'type': 'string', 'len': 2},
            {'key': 'phone_01', 'type': 'string', 'len': 11},
            {'key': 'prefix_02', 'type': 'string', 'len': 2},
            {'key': 'phone_02', 'type': 'string', 'len': 11},
            {'key': 'prefix_03', 'type': 'string', 'len': 2},
            {'key': 'phone_03', 'type': 'string', 'len': 11},
            {'key': 'prefix_04', 'type': 'string', 'len': 2},
            {'key': 'phone_04', 'type': 'string', 'len': 11},
            {'key': 'prefix_05', 'type': 'string', 'len': 2},
            {'key': 'phone_05', 'type': 'string', 'len': 11},
            {'key': 'prefix_06', 'type': 'string', 'len': 2},
            {'key': 'phone_06', 'type': 'string', 'len': 11},
            {'key': 'prefix_07', 'type': 'string', 'len': 2},
            {'key': 'phone_07', 'type': 'string', 'len': 11},
            {'key': 'prefix_08', 'type': 'string', 'len': 2},
            {'key': 'phone_08', 'type': 'string', 'len': 11},
            {'key': 'prefix_09', 'type': 'string', 'len': 2},
            {'key': 'phone_09', 'type': 'string', 'len': 11},
            {'key': 'prefix_10', 'type': 'string', 'len': 2},
            {'key': 'phone_10', 'type': 'string', 'len': 11},
            {'key': 'prefix_11', 'type': 'string', 'len': 2},
            {'key': 'phone_11', 'type': 'string', 'len': 11},
            {'key': 'prefix_12', 'type': 'string', 'len': 2},
            {'key': 'phone_12', 'type': 'string', 'len': 11},
            {'key': 'prefix_13', 'type': 'string', 'len': 2},
            {'key': 'phone_13', 'type': 'string', 'len': 11},
            {'key': 'prefix_14', 'type': 'string', 'len': 2},
            {'key': 'phone_14', 'type': 'string', 'len': 11},
            {'key': 'prefix_15', 'type': 'string', 'len': 2},
            {'key': 'phone_15', 'type': 'string', 'len': 11},
            {'key': 'id_facebook', 'type': 'string', 'len': 50},
            {'key': 'id_telegram', 'type': 'string', 'len': 30},
            {'key': 'string_01', 'type': 'string', 'len': 255},
            {'key': 'string_02', 'type': 'string', 'len': 255},
            {'key': 'string_03', 'type': 'string', 'len': 255},
            {'key': 'string_04', 'type': 'string', 'len': 255},
            {'key': 'string_05', 'type': 'string', 'len': 255},
            {'key': 'string_06', 'type': 'string', 'len': 255},
            {'key': 'string_07', 'type': 'string', 'len': 255},
            {'key': 'string_08', 'type': 'string', 'len': 255},
            {'key': 'string_09', 'type': 'string', 'len': 255},
            {'key': 'string_10', 'type': 'string', 'len': 255},
            {'key': 'date_01', 'type': 'date', 'len': None},
            {'key': 'date_02', 'type': 'date', 'len': None},
            {'key': 'date_03', 'type': 'date', 'len': None},
            {'key': 'date_04', 'type': 'date', 'len': None},
            {'key': 'date_05', 'type': 'date', 'len': None},
            {'key': 'date_06', 'type': 'date', 'len': None},
            {'key': 'date_07', 'type': 'date', 'len': None},
            {'key': 'date_08', 'type': 'date', 'len': None},
            {'key': 'date_09', 'type': 'date', 'len': None},
            {'key': 'date_10', 'type': 'date', 'len': None},
            {'key': 'money_01', 'type': 'float', 'len': None},
            {'key': 'money_02', 'type': 'float', 'len': None},
            {'key': 'money_03', 'type': 'float', 'len': None},
            {'key': 'money_04', 'type': 'float', 'len': None},
            {'key': 'money_05', 'type': 'float', 'len': None},
            {'key': 'money_06', 'type': 'float', 'len': None},
            {'key': 'money_07', 'type': 'float', 'len': None},
            {'key': 'money_08', 'type': 'float', 'len': None},
            {'key': 'money_09', 'type': 'float', 'len': None},
            {'key': 'money_10', 'type': 'float', 'len': None},
            {'key': 'valid_lead', 'type': 'datetime', 'len': None},
            {'key': 'score_lead', 'type': 'integer', 'len': None},
            {'key': 'created_at', 'type': 'datetime', 'len': None},
            {'key': 'updated_at', 'type': 'datetime', 'len': None},
            {'key': 'status', 'type': 'integer', 'len': None}
        ]
        
        return self.converter(params, dict_data)
