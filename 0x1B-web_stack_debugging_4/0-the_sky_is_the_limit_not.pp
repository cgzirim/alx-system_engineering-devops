# Increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'fix-Nginx_failed_requests':
        command => 'sed -i s/15/500/g /etc/default/nginx',
        path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
-> exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d'
}
