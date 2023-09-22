file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'root',
  group   => 'root',
  content => 'I love Puppet',
}
