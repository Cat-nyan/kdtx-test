import config
from api.login import LoginAPI
from api.course import CourseAPI
import pytest
from common.utils import build_data

class TestCourseAPI:
    token: str

    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        self.uuid = self.login_api.get_verify_code().json().get('uuid')
        login_data = {
            'username':'admin',
            'password':'HM_2023_test',
            'code':2,
            'uuid':self.uuid
        }
        TestCourseAPI.token = self.login_api.login(login_data).json().get('token')


    def teardown_method(self):
        pass

    @pytest.mark.parametrize('name,subject,price,applicablePerson,info,status,code,msg',build_data(config.BASE_PATH + '/data/course.json'))
    def test_course_add(self,name,subject,price,applicablePerson,info,status,code,msg):
        test_data = {
            "name": name,
            "subject": subject,
            "price": price,
            "applicablePerson": applicablePerson,
            "info": info
        }
        response = self.course_api.add_course(test_data, TestCourseAPI.token)
        assert response.status_code == status
        assert response.json().get('code') == code
        assert msg in response.json().get('msg')