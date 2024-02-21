#Ирина Сурикова, 13-я когорта — Финальный проект. Инженер по тестированию плюс

import create_order_request
def get_track_number_of_order():
    track_number = create_order_request.post_new_order()
    return track_number.json()["track"]


def test_create_and_track_order():
    track_number = get_track_number_of_order()
    get_response = create_order_request.get_order_info(track_number)
    assert get_response.status_code == 200
