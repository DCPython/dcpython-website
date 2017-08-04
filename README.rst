DC Python Website
=================

Created at the Q3 2017 Bethesda Sprint (https://www.meetup.com/dcpython/events/240449405/). Based on `previous <https://github.com/dcpython/dcpython-website-save>`_ `incarnations <https://github.com/dcpython/dcpython-django>`_.

AWS
---

::

    Ubuntu 16.04.1 LTS

::

    sudo add-apt-repository ppa:certbot/certbot
    sudo apt-get update
    sudo apt-get install aptitude awscli graphviz graphviz-dev jq letsencrypt \
        libpq-dev libxml2 libxml2-dev libxslt-dev make nginx pkg-config       \
        libgdal-dev \
        postgresql python python-pip python3 python3-pip python-virtualenv    \
        python3-virtualenv python-dev -y
    sudo aptitude upgrade -y


GitHub Deploy Key
-----------------

::

    ssh-keygen -t rsa -b 4096 -C aclark@dcpython.org


HTTPS
-----

::

    ubuntu@ip-172-31-28-151:/srv/dcpython-website$ sudo certbot certonly
    Saving debug log to /var/log/letsencrypt/letsencrypt.log

    How would you like to authenticate with the ACME CA?
    -------------------------------------------------------------------------------
    1: Spin up a temporary webserver (standalone)
    2: Place files in webroot directory (webroot)
    -------------------------------------------------------------------------------
    Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 1
    Please enter in your domain name(s) (comma and/or space separated)  (Enter 'c'
    to cancel):dcpython.org
    Obtaining a new certificate
    Performing the following challenges:
    tls-sni-01 challenge for dcpython.org
    Waiting for verification...
    Cleaning up challenges

    IMPORTANT NOTES:
     - Congratulations! Your certificate and chain have been saved at
       /etc/letsencrypt/live/dcpython.org/fullchain.pem. Your cert will
       expire on 2017-11-02. To obtain a new or tweaked version of this
       certificate in the future, simply run certbot again. To
       non-interactively renew *all* of your certificates, run "certbot
       renew"
     - If you like Certbot, please consider supporting our work by:

       Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
       Donating to EFF:                    https://eff.org/donate-le


