import config
from common.utils import build_data
from api.login import LoginAPI
import pytest



class TestLoginAPI:
    uuid: str = None

    def setup_method(self):
        self.login_api = LoginAPI()
        response = self.login_api.get_verify_code()
        TestLoginAPI.uuid = response.json().get('uuid')

    def teardown_method(self):
        pass

    @pytest.mark.parametrize('username,password,status,code,msg', build_data(config.BASE_PATH +'/data/login.json'))
    def test_login_success(self,username,password,status,code,msg):
        test_data = {
            "username": username,
            "password": password,
            "code": 2,
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(test_data)
        assert response.status_code == status
        assert response.json().get('code') == code
        assert msg in response.json().get('msg')






