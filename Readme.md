## Korrekter Abruf mit Jquery

````
var settings = {
  "url": "https://infovis.skoerner.com/custom",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({"1":"Mont Blanc","2":"Großglockner","3":"Finsteraarhorn","4":"Wildspitze","5":"Piz Bernina"}),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});

````


## Setup 

### Lokal
```
pip install pipenv
```

```
pipenv install
```
```
pipenv run python app.py
```


### Docker + Let's Encrpyt
````
$ sudo certbot certonly -d infovis.skoerner.com -n --standalone
$ mkdir /home/stefan/certs
$ sudo cp /etc/letsencrypt/live/infovis.skoerner.com/fullchain.pem /home/stefan/certs/
$ sudo cp /etc/letsencrypt/live/infovis.skoerner.com/privkey.pem /home/stefan/certs/
$ sudo chown stefan:stefan /home/stefan/certs/
$ docker build -t infovis .
$ docker run -dit --name infovis -p 443:443 --mount type=bind,source=/home/stefan/certs,target=/certs infovis
````
