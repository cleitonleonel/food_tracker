import requests
import timeit

ACCESS_KEY = '69f181d5-0046-4221-b7b2-deef62bd60d5'
SECRET_KEY = '9ef4fb4f-7a1d-4e0d-a9b1-9b82873297d8'

BASE_IFOOD_URL = 'https://www.ifood.com.br/delivery'
BASE_AVATAR_URL = 'https://static-images.ifood.com.br/image/upload/f_auto,t_high/logosgde'
BASE_URL = 'https://marketplace.ifood.com.br/v1'
BASE_WS_URL = 'https://wsloja.ifood.com.br/ifood-ws-v3'


class Browser(object):

    def __init__(self):
        self.response = None
        self.current_page = None
        self.session = requests.Session()

    def headers(self):
        base_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'identity;q=1',
            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection': 'keep-alive',
            'TE': 'Trailers',
            'Upgrade-Insecure-Requests': '1',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            'secret_key': SECRET_KEY,
            'access_key': ACCESS_KEY
        }
        return base_headers

    def send_request(self, method, url, **kwargs):
        response = self.session.request(method, url, **kwargs)
        if response.status_code == 200:
            return response

        return None


class IfoodAPI(Browser):

    def __init__(self):
        super().__init__()
        self.host_marketplace = 'marketplace.ifood.com.br'
        self.host_api = 'www.ifood.com.br'
        self.headers = self.headers()

    def start_request(self):
        return timeit.default_timer()

    def end_request(self):
        return timeit.default_timer()

    def get_json(self, method, url, headers):
        response = self.send_request(method, url, headers=headers)
        json_resp = response.json()
        return json_resp

    def parse_avatar(self, item):
        avatar = ''
        for resource in item:
            if resource == 'logoUrl':
                avatar = item['logoUrl']
        if avatar:
            return '/'.join([BASE_AVATAR_URL, avatar])
        return avatar

    def get_merchants(self, latitude, longitude, zip_code, delivery_fee_max):
        self.headers['host'] = 'marketplace.ifood.com.br'
        return self.get_json('GET',
                             f'{BASE_URL}/merchants?latitude={latitude}&longitude={longitude}&zip_code={zip_code}'
                             f'&page=0&channel=IFOOD&size=50&delivery_fee_from=0&delivery_fee_to={delivery_fee_max}',
                             self.headers)['merchants']

    def get_restaurant_info(self, uuid):
        self.headers['host'] = 'wsloja.ifood.com.br'
        return self.get_json('GET', f'{BASE_WS_URL}/restaurants/{uuid}', self.headers)['data']['restaurant']

    def get_restaurant_menu(self, uuid):
        self.headers['host'] = 'wsloja.ifood.com.br'
        return self.get_json('GET', f'{BASE_WS_URL}/restaurants/{uuid}/menu', self.headers)['data']['menu']

    def get_restaurant_flat_items(self, uuid, min_price, max_price):
        flat_menu = []
        for menu_group in self.get_restaurant_menu(uuid):
            for item in menu_group['itens']:
                cleaned_item = {
                    'name': item['description'],
                    'price': item.get('unitMinPrice', item.get('unitPrice', 'NaN'))
                }
                if min_price <= cleaned_item['price'] <= max_price:
                    flat_menu.append(cleaned_item)
        flat_menu.sort(key=lambda items: items['price'])
        return flat_menu

    def tracker(self, latitude, longitude, zip_code, delivery_fee_max, min_price, max_price):
        print('Serching....\nWait Please!!!')
        start = self.start_request()
        merchants = self.get_merchants(latitude, longitude, zip_code, delivery_fee_max)
        merchants_full_info = list(map(lambda merchant: self.get_restaurant_info(merchant['id']), merchants))
        filtered_restaurants_with_items = []
        for index, restaurant in enumerate(merchants_full_info):
            logo = self.parse_avatar(restaurant)
            if not restaurant['closed'] and not restaurant['unavailable'] and restaurant['minimunOrder'] <= max_price:
                filtered_restaurants_with_items.append({
                    'avatar': logo,
                    'name': restaurant['name'],
                    'minimunOrder': restaurant['minimunOrder'],
                    'distance': merchants[index]['distance'],
                    'category': merchants[index]['mainCategory']['name'],
                    'items': self.get_restaurant_flat_items(restaurant['uuid'], min_price, max_price)
                })

        filtered_restaurants_with_items.sort(key=lambda rest: rest['minimunOrder'])
        stop = self.end_request()
        # print('Duração: %f' % (stop - start))

        return filtered_restaurants_with_items
