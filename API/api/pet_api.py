import json

import allure

from API.api.base_api import BaseApi
from API.enums.common import Status


class PetApi(BaseApi):
    PATH = "/v2/pet"
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "dog"
        },
        "name": "Asia",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    update_payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "dog"
        },
        "name": "Asia2",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    def get_pet_by_id(self, pet_id: int):
        with allure.step('Get a pet'):
            return self.get(path=f'/{pet_id}')

    def post_add_pet(self):
        with allure.step('Post a pet'):
            payload = self.payload
            return self.post(path="", json_data=payload, headers={"Content-Type": "application/json"})

    def update_pet(self):
        with allure.step('Update (PUT method) a pet'):
            update_payload = self.update_payload
            return self.put(path="", json_data=update_payload, headers={"Content-Type": "application/json"})

    def get_pet_by_status(self):
        with allure.step('Get a pet by status'):
            return self.get(path=f'/findByStatus',
                            params={"status": Status.Available})

    def post_add_pet_by_id(self, pet_id: int):
        with allure.step('Post a pet by id'):
            return self.post(path=f'/{pet_id}')

    def delete_pet_by_id(self, pet_id: int):
        with allure.step('Delete a pet by id'):
            return self.delete(path=f'/{pet_id}')

    def check_delete_pet(self, pet_id: int):
        with allure.step('Check pet is deleted'):
            return self.get(path=f'/{pet_id}')

    def upload_pet_image(self, pet_id: int):
        with allure.step('A try to upload an image of a pet'):
            file_path = 'C:/Users/vikto/PycharmProjects/diploma/API/api/dog.png'
            headers = {'Content-Type': 'multipart/form-data'}
            return self.post(path=f'/{pet_id}/uploadImage',
                             files={'file': open(file_path, 'rb')})
