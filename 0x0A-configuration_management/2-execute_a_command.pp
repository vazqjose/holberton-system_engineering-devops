# Kill a process with exec

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}
