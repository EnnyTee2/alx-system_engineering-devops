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
  ensure     => 'installed',
}

exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
}

# change folder rights
exec { 'chmod www folder':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# create index file
file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

# create index file
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

# add redirection and error page
file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
"server {
        listen 80 default_server;
        listen [::]:80 default_server;
        # Add Custom HTTP Response Header
        add_header "X-Served-By" $HOSTNAME;

        root /var/www/html;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location /redirect_me {
        return 301 http://google.com/;
        }

        error_page 404 /404.html;

        location /404 {
          root /var/www/html;
          internal;
        }
}
",
}
# restart nginx
exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# ensure nginx running
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
