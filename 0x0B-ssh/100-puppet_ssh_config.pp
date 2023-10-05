#!/usr/bin/env bash
# sets up your client SSH configuration file

file { "ect/ssh/ssh_config":
	ensure => present,

content =>"

	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
