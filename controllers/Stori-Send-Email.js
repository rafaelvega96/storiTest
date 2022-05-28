var AWS = require('aws-sdk');
AWS.config.update({ region: 'us-east-1' });
const fs = require('fs');

exports.notification = async function (event) {
    console.log('Event:', event);
    let req;
    try {
        if (event.headers === undefined) {
            req = event;
        } else {
            req = JSON.parse(event.body);
        }
        console.log('Request:' + JSON.stringify(req));
        
        const toAddresses = req.MailTo;
        const toCcAddresses = req.emailCC;
        let data;
        data = JSON.stringify(req.data);
        console.log("data:", data);

        let params = {
            Destination: {
                ToAddresses: toAddresses,
                CcAddresses: toCcAddresses,
            },
            Source: "rafaelvega96@hotmail.com",
            Template: req.templateName,
            TemplateData: data
        };

        var sendPromise = new AWS.SES({ apiVersion: '2010-12-01' }).sendTemplatedEmail(params).promise();

        return sendPromise.then(
            function (data) {
                let response = {
                    "data": data,
                    "message": "The email has been sent correctly",
                    "status": 200,
                };

                console.log(data);
                return {
                    statusCode: 200,
                    body: JSON.stringify(response)
                };
            }).catch(
                function (err) {
                    let response = {
                        "data": null,
                        "message": err.message,
                        "status": 500
                    };
                    console.error(err, err.stack);
                    return {
                        statusCode: 500,
                        body: JSON.stringify(response)
                    };
                });
    } catch (e) {
        console.log('Error en handler: ' + JSON.stringify(e));
        let error = e.body || e;
        return {
            statusCode: e.statusCode || 500,
            body: JSON.stringify(error)
        }
    }
};