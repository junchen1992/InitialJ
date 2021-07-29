#!/bin/bash

# Ref: https://blog.csdn.net/qq_31396185/article/details/81179492



yum update -y && \
yum install git -y && \
yum install -y python-setuptools && \
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py && \
python get-pip.py && \
pip install git+https://github.com/shadowsocks/shadowsocks.git@master


yum -y groupinstall "Development Tools"
yum -y install wget
wget https://github.com/jedisct1/libsodium/releases/download/1.0.11/libsodium-1.0.11.tar.gz
tar xf libsodium-1.0.11.tar.gz && cd libsodium-1.0.11
./configure && make -j2 && make install
echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf
ldconfig


sudo ssserver -p 443 -k A1b2c3d4 -m aes-256-gcm --user nobody -d start

# Show logs
# sudo less /var/log/shadowsocks.log

# To stop the server
# sudo ssserver -d stop
