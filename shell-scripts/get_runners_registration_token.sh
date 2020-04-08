#!/bin/bash
echo "Gitlab::CurrentSettings.current_application_settings.runners_registration_token" |
      gitlab-rails console --environment=production