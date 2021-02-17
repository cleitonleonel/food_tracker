from geopy.geocoders import Nominatim
from api.ifood import IfoodAPI
import pycep_correios

zip_code = '29148613'
address = pycep_correios.get_address_from_cep(zip_code)

geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
location = geolocator.geocode(address['logradouro'] + ", " + address['cidade'] + " - " + address['bairro'])

data = {
    'latitude': location.latitude,
    'longitude': location.longitude,
    'zip_code': zip_code,
    'delivery_fee_max': '9',
    'min_price': '1.0',
    'max_price': '20.0'
}


def num(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            raise ValueError('argument is not a string of number')


i_food = IfoodAPI()
restaurants = i_food.tracker(data['latitude'],
                             data['longitude'],
                             data['zip_code'],
                             num(data['delivery_fee_max']),
                             num(data['min_price']),
                             num(data['max_price'])
                             )

print(restaurants)
