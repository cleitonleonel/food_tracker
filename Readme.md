# Food_Tracker

![QRCode Doação](https://raw.githubusercontent.com/cleitonleonel/food_tracker/master/tracker.svg)

### Sobre:

Food_Tracker faz o que o nome propriamente diz, rastreia sua comida, hahaha, defina sua área
passando o CEP da rua, um valor mínimo e outro máximo que corresponde ao valor limite dos produtos
que deseja procurar em estabelecimentos parceiros do IFOOD e essa lib encontra os melhores locais e
produtos de acordo com os filtros aplicados.

### Instalação:
pip install git+https://github.com/cleitonleonel/food_tracker.git

### Uso:
```python
from api.ifood import IfoodAPI


data = {
    'latitude': '-23878787',
    'longitude': '-40757574',
    'zip_code': '12345678',
    'delivery_fee_max': '9',
    'min_price': '1.0',
    'max_price': '20.0'
}

i_food = IfoodAPI()
restaurants = i_food.tracker(data['latitude'],
                             data['longitude'],
                             data['zip_code'],
                             int(data['delivery_fee_max']),
                             int(data['min_price']),
                             int(data['max_price'])
                             )

print(restaurants)

```

### Resultado:
```json
[
    {
        "avatar":"https://static-images.ifood.com.br/image/upload/f_auto,t_high/logosgde/55dfa66c-6a2f-4b5a-86c2-382ff3939af6/202004021825_mKTb_i.png",
        "name":"Love Burger (lanches - Açaí - Porções)",
        "minimunOrder":6,
        "distance":2.18,
        "category":"Lanches",
        "items":[
            {
                "name":"Água",
                "price":2.5
            },
            {
                "name":"Coca-Cola",
                "price":3.0
            },
            {
                "name":"Guaraná Antártica",
                "price":3.0
            },
            {
                "name":"Batata-Frita",
                "price":5.0
            },
            {
                "name":"Cervejas Latão",
                "price":5.0
            },
            {
                "name":"Sucos",
                "price":5.5
            },
            {
                "name":"Guaraná Uai",
                "price":7.0
            },
            {
                "name":"Cervejas Long Neck Geladas",
                "price":8.0
            },
            {
                "name":"Hambúrguer",
                "price":10.0
            },
            {
                "name":"Hambúrguer Especial",
                "price":12.0
            },
            {
                "name":"Açaí Tradicional",
                "price":13.5
            },
            {
                "name":"X-Egg",
                "price":13.5
            },
            {
                "name":"Sorvetes",
                "price":14.0
            },
            {
                "name":"Frango a Passarinho",
                "price":14.0
            },
            {
                "name":"Açaí Gourmet",
                "price":15.0
            },
            {
                "name":"X-Egg Burguer",
                "price":15.0
            },
            {
                "name":"X-Egg Bacon",
                "price":16.0
            },
            {
                "name":"Kids - Mini Burguer + Batata",
                "price":16.0
            },
            {
                "name":"Kids - Mini Egg + Batata",
                "price":16.0
            },
            {
                "name":"Classic Salada",
                "price":17.0
            },
            {
                "name":"X-Tudo",
                "price":17.0
            },
            {
                "name":"Kids - Mini Egg Burguer + Batata",
                "price":17.0
            },
            {
                "name":"Fritas com Bacon e Cheddar",
                "price":17.5
            },
            {
                "name":"Classic Egg",
                "price":18.5
            }
        ]
    },
    {
        "avatar":"https://static-images.ifood.com.br/image/upload/f_auto,t_high/logosgde/cfc336a9-faa7-49fa-927d-9b8fe0e54d12/202101251215_V3p6_.jpeg",
        "name":"Cozinha do Sabor",
        "minimunOrder":9,
        "distance":10.35,
        "category":"Lanches",
        "items":[
            {
                "name":"Trident melancia",
                "price":10.03
            },
            {
                "name":"Trident canela",
                "price":10.04
            },
            {
                "name":"Heineken",
                "price":15.5
            }
        ]
    },
    {
        "avatar":"https://static-images.ifood.com.br/image/upload/f_auto,t_high/logosgde/0cc90301-663f-4a54-9dc3-dae6e5b7e147/202008171716_AbpU_i.jpg",
        "name":"Açaí Daqui",
        "minimunOrder":10,
        "distance":1.7,
        "category":"Açaí",
        "items":[
            {
                "name":"Açaí 300ml",
                "price":10.0
            },
            {
                "name":"Açaí 500ml",
                "price":13.0
            },
            {
                "name":"Açaí 700ml",
                "price":15.0
            },
            {
                "name":"Açaí 1 Litro (Promoção Do Dia)",
                "price":20.0
            }
        ]
    },
    {
        "avatar":"https://static-images.ifood.com.br/image/upload/f_auto,t_high/logosgde/aa3056dd-9906-43e1-8e06-2502246f402f/202006081920_iAID_i.jpg",
        "name":"Lobinh Fast Food lanches, acai e pizza",
        "minimunOrder":15,
        "distance":0.45,
        "category":"Lanches",
        "items":[
            
        ]
    }
]
```

### Esta lib ajudou você?

Se esta lib permitir que você fique à vontade para fazer uma doação =), pode ser R $ 0,50 hahahaha. Para isso, basta ler o qrcode abaixo.

![QRCode Doação](https://github.com/cleitonleonel/pypix/blob/master/qrcode.png?raw=true)

### Autor:
cleiton.leonel@gmail.com