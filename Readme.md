## Setup 
````
$ sudo certbot certonly -d infovis.skoerner.com -n --standalone
$ mkdir /home/stefan/certs
$ sudo cp /etc/letsencrypt/live/infovis@skoerner.com/fullchain.pem /home/stefan/certs/
$ sudo cp /etc/letsencrypt/live/infovis@skoerner.com/privkey.pem /home/stefan/certs/
$ sudo chown stefan:stefan /home/stefan/certs/
$ docker build -t sample-app .
$ docker run -dit --name infovis -p 443:443 --mount type=bind,source=/home/stefan/certs,target=/certs infovis
````