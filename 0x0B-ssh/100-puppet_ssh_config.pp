# Modifies client configuration file.

file_line { 'Disable passwd auth':
  ensure  => present,
  path    => '/etc/ssh/sshd_config',
  line    => 'PasswordAuthentication no',
  replace => true,
}

file_line { 'Declare identity file':
  ensure  => present,
  path    => '/etc/ssh/sshd_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}
