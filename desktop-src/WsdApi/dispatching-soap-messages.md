---
description: There are many ways to handle dispatching received SOAP messages to the appropriate service. The two simplest mechanisms are transport level dispatch, and address and action dispatch.
ms.assetid: 988dc505-5d1f-46df-9340-107483bb9581
title: Dispatching SOAP Messages
ms.topic: article
ms.date: 05/31/2018
---

# Dispatching SOAP Messages

There are many ways to handle dispatching received SOAP messages to the appropriate service. The two simplest mechanisms are transport level dispatch, and address and action dispatch.

## Transport level dispatch

With transport level dispatch, the underlying HTTP server (such as the [HTTP API](/windows/desktop/Http/http-api-start-page)) is used to manage routing of requests to the device and its services. The server provides a different URL for each service and for the device and different sinks are registered for each URL. This allows code to be designed such that each service is isolated from the other, either running as separate components within the same process or running as separate processes.

Transport level dispatch has a few advantages. Messages can be dispatched to the appropriate component without first parsing the SOAP envelope or message body. Also, the existing mechanism for routing messages provided by most HTTP server implementations can be reused, which means custom dispatching code is unnecessary. It also isolates the SOAP processing code between services, which provides a level of security, as secure services avoid having messages travel through common code.

## Address and action dispatch

Address and action dispatch relies on the SOAP headers to determine the appropriate service to which the message is dispatched. This model may also use additional information, such as reference parameters, to further help dispatching.

This model encourages code reuse throughout a layered messaging stack, as all code up to the SOAP processor is shared by all services. Also, distinct transport addresses for services are not required, which means that UUID addresses can be used for service endpoints. Address and action dispatch also translates more directly to a programming model. Developers can plug services and devices into a single component which manages routing, rather than having to tie into a HTTP layer or creating separate components for each service.

 

 
