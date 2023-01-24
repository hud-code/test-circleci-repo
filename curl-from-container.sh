#!/bin/bash
set -eu -o pipefail

apt update
apt install curl -y
sleep 5
curl web:80