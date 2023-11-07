import configuration
import requests
import data

# POST-запрос на создание нового заказа:
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
    json = data.order_body)

# GET-запрос на получение заказа по номеру трека:
def get_order_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO_TO_TRACK,
                        params = {"t": track_number})