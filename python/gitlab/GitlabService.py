import subprocess, re

class GitlabService:

    def _get_docker_get_runners_registration_token(self):
        return subprocess.check_output(["/app/shell-scripts/docker_get_runners_registration_token.sh"])
    
    def _get_key_from_result(self, result):
        """
        Example result:
        b'--------------------------------------------------------------------------------\n GitLab:       
        12.9.2 (ac5568eb5d8) FOSS\n GitLab Shell: 12.0.0\n PostgreSQL:   10.12\n--------------------------------------------------------------------------------\n
        Loading production environment (Rails 6.0.2)\nSwitch to inspect mode.
        \nGitlab::CurrentSettings.current_application_settings.runners_registration_token\n"ZRLbrraaz6bBMD5yx9pf"\n\n'
        """
        regex_result = re.search("\"(.*)\"", result)

        return regex_result.group(1)


    def get_registration_key(self):
        result = self._get_docker_get_runners_registration_token()
        key = self._get_key_from_result(result=str(result))
        return key
        
if __name__ == '__main__':
    # registration_key = GitlabService().get_registration_key()
    # print(registration_key)
    # print(subprocess.check_output(["cat", "/app/shell-scripts/get_runners_registration_token.sh"]))
    print(subprocess.check_output(["/app/shell-scripts/docker_get_runners_registration_token.sh"]))
    pass

