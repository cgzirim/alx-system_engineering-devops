# Increases open file limits for the user, holberton

# Increase holberton's open file soft limit to 30,000.
exec { 'increase-open-file-soft-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/30000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase holberton's open file hard limit to 40,000.
exec { 'increase-open-file-hard-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/40000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
