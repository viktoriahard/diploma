# import pytest
#
# from API.api.pet_api import PetApi
# from API.enums.common import Status
# from itertools import combinations
#
#
# def test_enum():
#     print(Status.Available.value)
#
#
# @pytest.mark.parametrize("status", list(Status))
# def test_enum_1(status):
#     print(f"{status.value}")
#
#
# def test_enum_iter():
#     print(list(combinations(list(Status), 2)))
#
#
# def test_api():
#     api = PetApi()
#     resp = api.get_pet_by_id(1)
#

# def test_api_framework(api_client):
#     response1 = api_client.pet.get_pet_by_id(1)
#     assert response1.status_code == 200
#     response2 = api_client.store.get_store_inventory()
#     assert response2.status_code == 200
