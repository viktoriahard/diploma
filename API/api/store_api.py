from API.api.base_api import BaseApi


class StoreApi(BaseApi):
    PATH = '/v2/store'

    def get_store_inventory(self):
        return self._get(path=f'/inventory')