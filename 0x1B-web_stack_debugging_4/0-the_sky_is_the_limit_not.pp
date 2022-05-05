# Fix Nginx error: failed (24: Too many open files)

exec { "fix-Nginx_failed_requests":
        command => 'sed -i s/UNLIMIT="-n 15"/UNLIMIT="-n 500"/g /etc/default/nginx',
        path    => '/usr/local/bin/:/bin/'
}
