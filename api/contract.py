import requests
import config


class ContractAPI:
    def __init__(self):
        self.url_contract_upload = config.BASE_URL + '/api/common/upload'
        self.url_contract_add = config.BASE_URL + '/api/contract'

    def upload_contract(self, test_data, token: str):
        return requests.post(self.url_contract_upload, files={'file': test_data}, headers={'Authorization': token})

    def add_contract(self,test_data: dict, token: str):
        return requests.post(self.url_contract_add, json=test_data, headers={'Authorization': token})