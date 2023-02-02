import os
import sys
import requests


def get_coords(req):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={'+'.join(req.split())}&format=json"

    response = requests.get(geocoder_request)
    try:
        json_response = response.json()

        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        dolg1, shir1 = toponym['boundedBy']['Envelope']['lowerCorner'].split(' ')
        dolg2, shir2 = toponym['boundedBy']['Envelope']['upperCorner'].split(' ')
        del_dolg = float(dolg2) - float(dolg1)
        del_shir = float(shir2) - float(shir1)
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        toponym_coodrinates = toponym["Point"]["pos"]
        return {'coords': list(map(float, toponym_coodrinates.split(' '))), 
                'adress': toponym_address,
                'del_dolg': del_dolg,
                'del_shir': del_shir}
    except IndexError:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

def get_image(top_coordinates: tuple, scale):
    dolg, shir = top_coordinates
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={dolg},{shir}&spn={scale[0]},{scale[1]}&l=sat,skl"
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


if __name__ == '__main__':
    print(get_coords('Мельбурн'))