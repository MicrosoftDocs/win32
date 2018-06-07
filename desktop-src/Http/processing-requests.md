---
title: Processing Requests
description: Processing requests includes four steps.
ms.assetid: fb170d73-c26d-4bec-abed-b614b7dad322
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Processing Requests

Processing requests includes four steps:

-   Receiving a request
-   Handling the request
-   Sending the response
-   Canceling requests that cannot be processed

![](images/processloop.png)

## Receiving a Request

The HTTP Server API supplies a request structure to store the parsed incoming request. This structure is allocated by the application, and initialized when an incoming request is received. The application calls the [**HttpReceiveHttpRequest**](httpreceivehttprequest.md) function to receive the request. If the request buffer is too small to receive the request, the application can increase the buffer size and call **HttpReceiveHttpRequest** again to receive the entire request.

If the request includes entity body data to be received, the applications calls [**HttpReceiveRequestEntityBody**](httpreceiverequestentitybody.md) with the request ID returned in the *pRequestBuffer* parameter during the call to [**HttpReceiveHttpRequest**](httpreceivehttprequest.md).

## Handling the Request

The application performs application-specific processing of the request and formulates a response. The HTTP Server API imposes no timeout on this process.

## Sending the Response

When the application is finished handling the request and formulating the response, it calls the [**HttpSendHttpResponse**](httpsendhttpresponse.md) function to send the response. If the response includes entity body data to send, the application also calls [HttpSendResponseEntityBody](httpsendresponseentitybody.md).

## Canceling Requests

After the application has received a request ID from its call to [**HttpReceiveHttpRequest**](httpreceivehttprequest.md), it can at any time cancel the request by calling [HttpCancelHttpRequest](httpcancelhttprequest.md).

 

 




