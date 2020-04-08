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

    # def test_get_registration_key_from_gitlab(self):
    #     registration_key = self.gitlab_service.get_registration_key()
    #     self.assertTrue(registration_key != None)
    #     self.assertEqual(len(registration_key), 20)
    #     pass

    def test_register_gitlab_runner(self):
        registration_key = self.gitlab_service.register_gitlab_runner()
        # self.assertTrue(registration_key != None)
        # self.assertEqual(len(registration_key), 20)
        pass

    # def test_get_key_from_result(self):
    #     example_result = """b'--------------------------------------------------------------------------------\n GitLab:       12.9.2 (ac5568eb5d8) FOSS\n GitLab Shell: 12.0.0\n PostgreSQL:   10.12\n--------------------------------------------------------------------------------\nLoading production environment (Rails 6.0.2)\nSwitch to inspect mode.\nGitlab::CurrentSettings.current_application_settings.runners_registration_token\n"ZRLbrraaz6bBMD5yx9pf"\n\n'"""
    #     registration_key = self.gitlab_service._get_key_from_result(result=example_result)

    #     self.assertEqual(registration_key, "ZRLbrraaz6bBMD5yx9pf")
    #     pass

if __name__ == '__main__':
    unittest.main()
