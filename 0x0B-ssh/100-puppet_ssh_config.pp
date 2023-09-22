# edit the config file

file { '/home/iyasu2/.ssh/config':
  ensure  => present,
  content => "Host 100.24.74.170\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}
