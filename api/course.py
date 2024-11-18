import requests
import config


class CourseAPI:
    def __init__(self):
        self.url_add_course = config.BASE_URL + '/api/clues/course/'

    def add_course(self, test_data: dict, token: str):
        return requests.post(url=self.url_add_course, json=test_data, headers={'Authorization': token})