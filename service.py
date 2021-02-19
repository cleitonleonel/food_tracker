import sys
import pycep_correios
from geopy.geocoders import Nominatim
from api.ifood import IfoodAPI


def num(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            raise ValueError('argument is not a string of number')


def main(**kwargs):
    address = ''
    zip_code = ''
    for item in kwargs:
        if item == 'zip_code':
            zip_code = kwargs[item]
            get_address = pycep_correios.get_address_from_cep(zip_code)
            address = f"{get_address['logradouro']},{get_address['cidade']}-{get_address['bairro']}"
        elif item == 'formatted_address':
            address = kwargs[item]
    geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    location = geolocator.geocode(address)

    data = {
        'latitude': location.latitude,
        'longitude': location.longitude,
        'zip_code': zip_code,
        'delivery_fee_max': '9',
        'min_price': '1.0',
        'max_price': '20.0'
    }

    i_food = IfoodAPI()
    restaurants = i_food.tracker(data['latitude'],
                                 data['longitude'],
                                 data['zip_code'],
                                 num(data['delivery_fee_max']),
                                 num(data['min_price']),
                                 num(data['max_price'])
                                 )

    print(restaurants)


if __name__ == '__main__':
    args = sys.argv
    parameter = {}
    if len(args) > 0:
        arg = ' '.join(args[1:])
        if arg.isalnum():
            parameter['zip_code'] = arg
        else:
            parameter['formatted_address'] = arg
        main(**parameter)
