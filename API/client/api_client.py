from API.api.pet_api import PetApi
from API.api.store_api import StoreApi


class ApiClient:

    def __init__(self):
        self.pet: PetApi = PetApi()
        self.store: StoreApi = StoreApi()
