#!/usr/bin/env bash
#using puppet to connect without password

file { 'etc/ssh/ssh_config':
     ensure => present,
}

file_line { 'Turn off password auth':
 path    => 'etc/ssh/ssh_config',
 line    => 'PasswordAuthentication n',
 match   => '^#PasswordAuthentication',
}

file_line {'Declare identity file',
 path    => 'etc/ssh/ssh_config',
 line    => 'IdentifyFile ~/.ssh/school',
 match   => 'IdentityfFile',
}
