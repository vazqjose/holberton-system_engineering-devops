# Install a package

$package = "puppet-lint"

package { $package:
  ensure   => 'installed',
}
