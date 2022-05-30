# Stor Challenge

Para este Challege la forma de solucionar el problema fue la siguiente: 

Se desarrollaron 2 lambdas en aws 

- Stori-Summary-Email
- Stori-Send-Email

La primera lambda *Stori-Summary-Email* se encarga de ir un bucket de s3 a recuperar el archivo .csv, capturar la informacion y mapear un diccionario para llenar la informacion del template de correo. Esta se encuentra desarrollada en python.

```json
{
        "balance": 39.74,
        "average_debit_amount": 35.25,
        "average_credit_amount": -15.38,
        "months": [
            {
                "name": "July",
                "number_transactions": 2
            },
            {
                "name": "August",
                "number_transactions": 2
            }
        ]
}
```

Esta lambda invoca a la segunda lambda *Stori-Send-Email* y esta se encarga de enviar el correo.
La lambda de envio de correos se encarga de ir a llamar el sdk de amazon para el envio de correos. Esta se encuentra desarrollada en Javascript
Esta recibe la siguiente informacion:

```json
{
    "templateName": "test",
    "MailTo": [
        "rafaelvega96@hotmail.com"
    ],
    "emailCC": [
        "rafaelvegacan@gmail.com"
    ],
    "data": {
        "balance": 39.74,
        "average_debit_amount": 35.25,
        "average_credit_amount": -15.38,
        "months": [
            {
                "name": "July",
                "number_transactions": 2
            },
            {
                "name": "July",
                "number_transactions": 2
            },
            {
                "name": "August",
                "number_transactions": 2
            },
            {
                "name": "August",
                "number_transactions": 2
            }
        ]
    }
}

```

Para el template de correo se utilizo el servicio de SES de amazon el cual nos permite subir un template de correo y llamarlo a traves de la lambda. En la carpeta *templateshtml* se encuentra el template puro y en la carpeta *template* el archivo que se utiliza para desplegar el template. 

## Consideraciones 

- Para desplegar las dos lambdas se utilizo el framework de serverless
- Las funciones lambdas no se encuentra expuestas a internet por un metodo http
- Debido a que la consola de aws esta en un modo sandbox, para el envio de correos se debe verificar el correo de la persona a la que se le envie el correo




