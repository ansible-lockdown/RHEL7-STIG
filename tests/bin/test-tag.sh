#!/bin/bash -xe

rm Dockerfile || true
cp Dockerfile.centos Dockerfile
docker kill rhel7-stig-local || true
docker rm rhel7-stig-local || true
docker build -t rhel7-stig-local .
docker run -id --privileged --name rhel7-stig-local -v /sys/fs/cgroup:/sys/fs/cgroup:ro --cap-add SYS_ADMIN --cap-add AUDIT_CONTROL rhel7-stig-local
ansible-playbook ../molecule/default/playbook-local.yml -i docker.py --tags $@

rm Dockerfile
