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

    def _call_register_gitlab_runner(self, registration_key):
        try:
            output = subprocess.check_output(["/app/shell-scripts/gitlab-runner-register.sh", registration_key])
            print(output)
            return output
        except subprocess.CalledProcessError as e:
            print(e.output)
            return e.output
    
    def register_gitlab_runner(self, registration_key=None):
        """
        Example result:
        'b"Runtime platform                                  
        \\x1b[0;m  arch\\x1b[0;m=amd64 os\\x1b[0;m=linux pid\\x1b[0;m=120 revision\\x1b[0;m=4c96e5ad version\\x1b[0;m=12.9.0\\r\\nRunning in system-mode.                           
        \\x1b[0;m \\r\\n                                                  \\x1b[0;m \\r\\nRegistering runner... succeeded                   
        \\x1b[0;m  runner\\x1b[0;m=ZRLbrraa\\r\\nRunner registered successfully. Feel free to start it, but if it\'s running already the config should be automatically reloaded!\\x1b[0;m \\r\\n"'
        """
        if(registration_key is None):
            registration_key = self.get_registration_key()
        result = self._call_register_gitlab_runner(registration_key=registration_key)
        return result
    
    def create_project_awesome_sause(self):
        pass
        
if __name__ == '__main__':
    # registration_key = GitlabService().get_registration_key()
    # print(registration_key)
    # print(subprocess.check_output(["cat", "/app/shell-scripts/get_runners_registration_token.sh"]))
    # print(subprocess.check_output(["/app/shell-scripts/docker_get_runners_registration_token.sh"]))
    pass

