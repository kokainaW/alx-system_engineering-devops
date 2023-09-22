# install puppet-lint -v 4.2.0

exec { 'puppet-lint':
  command => '/usr/bin/apt-get -y install puppet-lint -v 4.2.0',
}
