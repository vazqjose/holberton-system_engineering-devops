#create a file

class createfile {
file { '0-create_a_file.pp':
  ensure  => 'present',
  path    => '/tmp/holberton',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
   }
}

