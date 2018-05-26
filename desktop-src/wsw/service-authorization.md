---
title: Service Authorization
description: An application can implement custom authorization for incoming messages on a service host .
ms.assetid: 75bcf051-3983-48fc-8121-0984ac9cdcb9
keywords:
- Service Authorization Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Service Authorization

An application can implement custom authorization for incoming messages on a service host .

## 

A service host receives a security callback [**WS\_SERVICE\_SECURITY\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_service_security_callback?branch=master) as part of the [**WS\_SERVICE\_ENDPOINT**](/windows/win32/WebServices/ns-webservices-_ws_service_endpoint?branch=master) which is passed to the [**WsCreateServiceHost**](/windows/win32/WebServices/nf-webservices-wscreateservicehost?branch=master) function. This callback is invoked when the [WS\_MESSAGE](ws-message.md) is received.

The application can rely on this callback to implement custom authorization for incoming messages on the service host. If the authorization fails the security callback function returns a failure HR, and the service host aborts the channel.

See the user name over SSL example, [HttpCalculatorWithUserNameOverSslServiceExample](httpcalculatorwithusernameoversslserviceexample.md), for an example implementation.

 

 




