import config
from api.login import LoginAPI
from api.course import CourseAPI
from api.contract import ContractAPI

class TestContractBusiness:
    token: str = None
    file_name: str = None
    # 前置处理
    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        self.contract_api = ContractAPI()

    # 后置处理
    def teardown_method(self):
        pass

    def test_login_success(self):
        # 获取验证码
        res_v = self.login_api.get_verify_code()
        assert res_v.status_code == 200
        assert res_v.json().get('msg') == '操作成功'

        # 登录
        login_data = {"username": "admin", "password": "HM_2023_test", "code":"2",
                      "uuid": res_v.json().get('uuid')
                      }
        res_l = self.login_api.login(test_data=login_data)
        assert res_l.status_code == 200
        assert res_l.json().get('msg') == '操作成功'
        TestContractBusiness.token = res_l.json().get('token')

    def test_add_course(self):
        course_data = {
                        "name": "测试开发提升课02",
                        "subject": "6",
                        "price": 899,
                        "applicablePerson": "7",
                        "info": "测试开发提升课02"
                        }
        res_a = self.course_api.add_course(test_data=course_data, token=TestContractBusiness.token)
        assert res_a.status_code == 200
        assert res_a.json().get('msg') == '操作成功'

    def test_upload_contract(self):
        f = open(config.BASE_PATH+'/data/1.txt','rb')
        res_u = self.contract_api.upload_contract(test_data=f, token=TestContractBusiness.token)
        assert res_u.status_code == 200
        assert res_u.json().get('msg') == '操作成功'
        TestContractBusiness.file_name = res_u.json().get('fileName')

    def test_add_contract(self):
        contract_data = {
                        "name": "测试888",
                        "phone": "13612341888",
                        "contractNo": "NT1001200401",
                        "subject": "6",
                        "courseId": 99,
                        "channel": "0",
                        "activityId": 77,
                        "fileName": TestContractBusiness.file_name
                        }
        res_a = self.contract_api.add_contract(test_data=contract_data, token=TestContractBusiness.token)
        assert res_a.status_code == 200
        assert res_a.json().get('msg') == '操作成功'