# add stable version of nginx
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# update software packages list
exec { 'update packages':
  command => 'sudo apt update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# install nginx
package { 'nginx':
  ensure => 'installed',
}

# Adding the header to config file
file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content => "\
  server {
        listen 80 default_server;
        listen [::]:80 default_server;

        # Add Custom HTTP Response Header
        add_header X-Served-By $HOSTNAME;
        
        server_name _;
        }
}"
}

# restart nginx
exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}
