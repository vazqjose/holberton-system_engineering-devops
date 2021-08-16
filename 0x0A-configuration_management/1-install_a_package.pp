# Install a package

$package = 'puppet-lint'

package { $package:
  ensure   => '1.1.0',
  provider => 'gem',
}
