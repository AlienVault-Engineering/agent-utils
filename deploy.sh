#!/bin/bash

set -x

cat > /root/.pypirc <<EOF
[distutils]
index-servers = pypi

[pypi]
username: ${PYPI_USER}
password: ${PYPI_PASS}
EOF

cat /root/.pypirc

pyb -v install_dependencies package install upload