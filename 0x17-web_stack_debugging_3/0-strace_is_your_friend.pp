#fixes some phpp errors

file { '/var/www/html/wp-settings.php':
  content => file('/var/www/html/wp-settings.php')
    .content
    .gsub('phpp', 'php'),
}
