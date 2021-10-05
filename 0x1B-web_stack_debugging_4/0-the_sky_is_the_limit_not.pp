# Puppet script to optimize the Nginx server capacity

exec { 'set limit to 2000':
  command => 'sed -i "s/15/2000/" /etc/default/nginx',
  path    => '/bin'
} ->

# Restart Nginx server
exec { 'nginx-restart':
  command => '/usr/sbin/service nginx restart'
}
