FROM centos:7

RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs
RUN yum -y update; yum clean all; \
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*; \
rm -f /etc/systemd/system/*.wants/*; \
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*; \
rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN yum -y install openssh-server audit authconfig initscripts
RUN yum clean all

# Fix for Travis docker containers
RUN ssh-keygen -f /etc/ssh/ssh_host_ed25519_key -N '' -t ed25519
RUN mkdir /var/log/audit; chmod 700 /var/log/audit;

VOLUME ["/sys/fs/cgroup", "/var/log/audit"]

CMD ["/usr/sbin/init"]
