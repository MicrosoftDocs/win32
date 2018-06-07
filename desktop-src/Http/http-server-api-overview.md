---
title: HTTP Server API Overview
description: This topic identifies a typical sequence of operations that use the HTTP Server API.
ms.assetid: 1245fd98-8370-4f1b-8c86-de9be5e678bd
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HTTP Server API Overview

The following list identifies a typical sequence of operations that use the HTTP Server API:

-   Initialize the HTTP Server API by using the [**HttpInitialize**](httpinitialize.md) function.
-   Create a request queue by using the [**HttpCreateHttpHandle**](httpcreatehttphandle.md) function.
-   Register one or more URLs by using the [**HttpAddUrl**](httpaddurl.md) function.
-   Receive incoming requests directed to registered URLs by using the [**HttpReceiveHttpRequest**](httpreceivehttprequest.md) function, and send HTTP responses for these requests by using the [**HttpSendHttpResponse**](httpsendhttpresponse.md) function.
-   (Optional) When sending a response, send an additional entity body by using the [**HttpSendResponseEntityBody**](httpsendresponseentitybody.md) function.
-   Perform clean-up operations by using the [**HttpRemoveUrl**](httpremoveurl.md), [**CloseHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724211) and [**HttpTerminate**](httpterminate.md) functions.

In operations that use URLs, note that it is the processed URL contained in the **CookedUrl** member of the [**HTTP\_REQUEST\_V1**](http-request-v1.md) structure that should be used. Do not the unprocessed URL in the **pRawUrl** member, which is solely for tracking and statistical purposes.

Each application creates its own request queue. An application obtains its request queue handle from [**HttpCreateHttpHandle**](httpcreatehttphandle.md). It passes this handle to the [**HttpAddUrl**](httpaddurl.md) function to add a URL to the request queue. The application receives notification of an incoming request, and retrieves it from the request queue by calling the [**HttpReceiveHttpRequest**](httpreceivehttprequest.md) function with the request queue handle. You can use this function to receive either the request headers or both the headers and entity body. [**HttpReceiveHttpRequest**](httpreceivehttprequest.md) also returns a request identifier (RequestId) for the received request that is unique to the request handle.

> [!Note]  
> It is the application's responsibility to examine all relevant request headers, including content-negotiation headers if they are being used, and fail requests as appropriate based on header content. The HTTP Server API ensures only that each header line is properly terminated, and does not contain illegal characters.

 

Use the [**HttpReceiveRequestEntityBody**](httpreceiverequestentitybody.md) function with the request queue handle to retrieve subsequent portions of a request's entity body, if any.

> [!Note]  
> The HTTP Server API decodes chunked messages on the receive side, but does not perform chunked encoding on the send side. If chunking is required on the send side, the application must implement it. For more information about chunked encoding, see [RFC 2616](Http://go.microsoft.com/fwlink/p/?linkid=84048).

 

Use the [**HttpReceiveClientCertificate**](httpreceiveclientcertificate.md) function with applications that serve URLs by using a secure scheme ("**https**") to optionally retrieve the client's certificate information.

Responses are sent with the [**HttpSendHttpResponse**](httpsendhttpresponse.md) function. This function uses the RequestId from the corresponding request to send the response. A response can be sent in several API calls over time by calling the [**HttpSendResponseEntityBody**](httpsendresponseentitybody.md) function with the RequestId from the originally received request.

> [!Note]  
> By default, [**HttpSendHttpResponse**](httpsendhttpresponse.md) uses "Microsoft-HTTPAPI/1.0" as the "Server:" header. If an application specifies a server header in a response, that value is placed as the first part of the server header, followed by a space and then "Microsoft-HTTPAPI/1.0".

 

In general, the HTTP Server API hides details of connection management and their establishment and teardown from applications. However, an application can optionally detect termination of a connection by calling [**HttpWaitForDisconnect**](httpwaitfordisconnect.md).

Applications must clean-up by using the following steps:

-   When the application is not listening or responding to a URL, the URL is removed by using the [**HttpRemoveURL**](httpremoveurl.md) function.
-   When the application is finished using the request queue, close the request queue handle by using the [**CloseHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724211) function.
-   When the application is finished using the HTTP Server API, call the [**HttpTerminate**](httpterminate.md) function.

 

 




