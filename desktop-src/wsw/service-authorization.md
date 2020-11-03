---
title: Service Authorization
description: An application can implement custom authorization for incoming messages on a service host .
ms.assetid: 75bcf051-3983-48fc-8121-0984ac9cdcb9
keywords:
- Service Authorization Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Service Authorization

An application can implement custom authorization for incoming messages on a service host .


A service host receives a security callback [**WS\_SERVICE\_SECURITY\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_service_security_callback) as part of the [**WS\_SERVICE\_ENDPOINT**](/windows/desktop/api/WebServices/ns-webservices-ws_service_endpoint) which is passed to the [**WsCreateServiceHost**](/windows/desktop/api/WebServices/nf-webservices-wscreateservicehost) function. This callback is invoked when the [WS\_MESSAGE](ws-message.md) is received.

The application can rely on this callback to implement custom authorization for incoming messages on the service host. If the authorization fails the security callback function returns a failure HR, and the service host aborts the channel.

See the user name over SSL example, [HttpCalculatorWithUserNameOverSslServiceExample](httpcalculatorwithusernameoversslserviceexample.md), for an example implementation.

 

 




