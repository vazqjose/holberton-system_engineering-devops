#create a file

$package = 'Holberton'

package {
  $package:

  ensure  => 'present',
  path    => '/tmp/holberton',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}

