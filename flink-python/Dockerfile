FROM flink:1.19.0

RUN apt-get update -y && \
apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libffi-dev && \
wget https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tgz && \
tar -xvf Python-3.11.9.tgz && \
cd Python-3.11.9 && \
./configure --without-tests --enable-shared && \
make -j6 && \
make install && \
ldconfig /usr/local/lib && \
cd .. && rm -f Python-3.11.9.tgz && rm -rf Python-3.11.9 && \
ln -s /usr/local/bin/python3 /usr/local/bin/python && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

# install PyFlink
RUN pip3 install apache-flink-libraries==1.19.0 && pip3 install apache-flink==1.19.0