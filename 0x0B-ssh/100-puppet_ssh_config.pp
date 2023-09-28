#!/usr/bin/env bash
#sets up your client SSH configuration fie
file_line { 'Turn_off_passwd_auth':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  }

file_line { 'Declare_identity_file':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  }
