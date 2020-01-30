#!/bin/bash

set -x

echo username=$PYPI_USER

cat > /root/.pypirc <<EOF
[distutils]
index-servers = pypi

[pypi]
# repository: https://alienvault.jfrog.io/alienvault/api/pypi/otxb-core
username: ${PYPI_USER}
password: ${PYPI_PASS}
EOF

cat /root/.pypirc

pyb -v install_dependencies package install upload