
echo "Building python module for nginx"

tempDir="$(mktemp -d)"
chmod 777 "$tempDir"
savedAptMark="$(apt-mark showmanual)"

cd $tempDir
apt-src install nginx=${NGINX_VERSION}

echo "Grabbing python nginx module"
git clone https://github.com/arut/nginx-python-module

# hmm, getting the version/path
cd nginx-1.13.12

# build the module
./configure --with-compat --add-dynamic-module=../nginx-python-module
make modules

cp -a objs /tmp/objs
