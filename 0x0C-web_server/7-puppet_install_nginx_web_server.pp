# configure nginx

class { 'nginx':
  listen_port => 80,
}

nginx::resource::vhost { 'default':
  ensure     => present,
  listen_opt => 'default_server',
  proxy      => 'http://localhost:8080',
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => '<html><body>Hello World!</body></html>',
}

