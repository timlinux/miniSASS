#--------- Generic stuff all our Dockerfiles should start with so we get caching ------------
FROM ubuntu:trusty
MAINTAINER Tim Sutton<tim@kartoza.com>

RUN  export DEBIAN_FRONTEND=noninteractive
ENV  DEBIAN_FRONTEND noninteractive
RUN  dpkg-divert --local --rename --add /sbin/initctl
#RUN  ln -s /bin/true /sbin/initctl

# Use local cached debs from host (saves your bandwidth!)
# Change ip below to that of your apt-cacher-ng host
# Or comment this line out if you do not with to use caching
ADD 71-apt-cacher-ng /etc/apt/apt.conf.d/71-apt-cacher-ng

RUN apt-get -y update

#-------------Application Specific Stuff ----------------------------------------------------

RUN apt-get -y install libpq5 python-gdal python-geoip \
    python python-dev python-distribute python-pip \
    python-psycopg2 npm node rpl python-dev libjpeg8-dev \
    libpng12-dev libfreetype6-dev zlib1g-dev python-pycurl

RUN pip install --no-index -f http://dist.plone.org/thirdparty/ -U PIL

ADD REQUIREMENTS.txt /REQUIREMENTS.txt
RUN pip install -r /REQUIREMENTS.txt
RUN pip install uwsgi

ADD uwsgi.conf /uwsgi.conf
ADD uwsgi_params /uwsgi_params

# Open port 51000 as we will be running our uwsgi socket on that
EXPOSE 51002


# You could put --protocol=http as a parameter (to test it directly)
# when running e.g. docker run konektaz/healthsites --protocol=http
# or any other wsgi parameters and they will be tagged on to the
# the end of the entrypoint.

# Under normal usage you would supply no additional params and
# use nginx on the host to forward in the traffic.
ENTRYPOINT ["uwsgi", "--ini", "/home/web/docker-prod/uwsgi.conf"]
