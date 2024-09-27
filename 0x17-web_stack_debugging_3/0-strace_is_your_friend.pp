# 0-strace_is_your_friend.pp
# This manifest ensures that the mistyped .phpp is renamed to .php.

exec { 'fix-wordpress-server-error':
    command => 'sed -i s/phpp/php/g var/www/html/wp-settings.php',
    path    => 'usr/bin/:/bin/',
}
