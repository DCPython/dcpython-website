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

