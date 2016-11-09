var eventosUrl = 'http://localhost:9000/api/eventos/';

var config = {

    eventosUrl: eventosUrl,


};

app

    .value('configEventos', config);

app.constant('ROUTERS2', {
    "xxx": {
        "url": "/xxx",
        "templateUrl": "templates/xxx.html"
    },
    "eventos": {
        "url": "/eventos",
        "views": {
            "": {
                "templateUrl": "app/views/layout.html"
            },
            "aside": {
                "templateUrl": "app/views/aside.html"
            },
            "content": {
                "templateUrl": "app/views/content.html"
            }
        }
    },