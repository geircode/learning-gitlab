import unittest
import datetime
from gitlab.GitlabService import GitlabService

class TestGitlabService(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.gitlab_service = GitlabService()
        pass 
        
    def setUp(self):
        print(datetime.datetime.now())   

    def test_get_registration_key_from_gitlab(self):
        registration_key = self.gitlab_service.get_registration_key()
        self.assertTrue(registration_key != None)
        self.assertTrue(len(registration_key) == 20)
        pass

if __name__ == '__main__':
    unittest.main()
