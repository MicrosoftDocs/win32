---
title: HTTP Server API Overview
description: This topic identifies a typical sequence of operations that use the HTTP Server API.
ms.assetid: 1245fd98-8370-4f1b-8c86-de9be5e678bd
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HTTP Server API Overview

The following list identifies a typical sequence of operations that use the HTTP Server API:

-   Initialize the HTTP Server API by using the [**HttpInitialize**](/windows/win32/Http/nf-http-httpinitialize?branch=master) function.
-   Create a request queue by using the [**HttpCreateHttpHandle**](/windows/win32/Http/nf-http-httpcreatehttphandle?branch=master) function.
-   Register one or more URLs by using the [**HttpAddUrl**](/windows/win32/Http/nf-http-httpaddurl?branch=master) function.
-   Receive incoming requests directed to registered URLs by using the [**HttpReceiveHttpRequest**](/windows/win32/Http/nf-http-httpreceivehttprequest?branch=master) function, and send HTTP responses for these requests by using the [**HttpSendHttpResponse**](/windows/win32/Http/nf-http-httpsendhttpresponse?branch=master) function.
-   (Optional) When sending a response, send an additional entity body by using the [**HttpSendResponseEntityBody**](/windows/win32/Http/nf-http-httpsendresponseentitybody?branch=master) function.
-   Perform clean-up operations by using the [**HttpRemoveUrl**](/windows/win32/Http/nf-http-httpremoveurl?branch=master), [**CloseHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724211) and [**HttpTerminate**](/windows/win32/Http/nf-http-httpterminate?branch=master) functions.

In operations that use URLs, note that it is the processed URL contained in the **CookedUrl** member of the [**HTTP\_REQUEST\_V1**](/windows/win32/Http/ns-http-_http_request_v1?branch=master) structure that should be used. Do not the unprocessed URL in the **pRawUrl** member, which is solely for tracking and statistical purposes.

Each application creates its own request queue. An application obtains its request queue handle from [**HttpCreateHttpHandle**](/windows/win32/Http/nf-http-httpcreatehttphandle?branch=master). It passes this handle to the [**HttpAddUrl**](/windows/win32/Http/nf-http-httpaddurl?branch=master) function to add a URL to the request queue. The application receives notification of an incoming request, and retrieves it from the request queue by calling the [**HttpReceiveHttpRequest**](/windows/win32/Http/nf-http-httpreceivehttprequest?branch=master) function with the request queue handle. You can use this function to receive either the request headers or both the headers and entity body. [**HttpReceiveHttpRequest**](/windows/win32/Http/nf-http-httpreceivehttprequest?branch=master) also returns a request identifier (RequestId) for the received request that is unique to the request handle.

> [!Note]  
> It is the application's responsibility to examine all relevant request headers, including content-negotiation headers if they are being used, and fail requests as appropriate based on header content. The HTTP Server API ensures only that each header line is properly terminated, and does not contain illegal characters.

 

Use the [**HttpReceiveRequestEntityBody**](/windows/win32/Http/nf-http-httpreceiverequestentitybody?branch=master) function with the request queue handle to retrieve subsequent portions of a request's entity body, if any.

> [!Note]  
> The HTTP Server API decodes chunked messages on the receive side, but does not perform chunked encoding on the send side. If chunking is required on the send side, the application must implement it. For more information about chunked encoding, see [RFC 2616](Http://go.microsoft.com/fwlink/p/?linkid=84048).

 

Use the [**HttpReceiveClientCertificate**](/windows/win32/Http/nf-http-httpreceiveclientcertificate?branch=master) function with applications that serve URLs by using a secure scheme ("**https**") to optionally retrieve the client's certificate information.

Responses are sent with the [**HttpSendHttpResponse**](/windows/win32/Http/nf-http-httpsendhttpresponse?branch=master) function. This function uses the RequestId from the corresponding request to send the response. A response can be sent in several API calls over time by calling the [**HttpSendResponseEntityBody**](/windows/win32/Http/nf-http-httpsendresponseentitybody?branch=master) function with the RequestId from the originally received request.

> [!Note]  
> By default, [**HttpSendHttpResponse**](/windows/win32/Http/nf-http-httpsendhttpresponse?branch=master) uses "Microsoft-HTTPAPI/1.0" as the "Server:" header. If an application specifies a server header in a response, that value is placed as the first part of the server header, followed by a space and then "Microsoft-HTTPAPI/1.0".

 

In general, the HTTP Server API hides details of connection management and their establishment and teardown from applications. However, an application can optionally detect termination of a connection by calling [**HttpWaitForDisconnect**](/windows/win32/Http/nf-http-httpwaitfordisconnect?branch=master).

Applications must clean-up by using the following steps:

-   When the application is not listening or responding to a URL, the URL is removed by using the [**HttpRemoveURL**](/windows/win32/Http/nf-http-httpremoveurl?branch=master) function.
-   When the application is finished using the request queue, close the request queue handle by using the [**CloseHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724211) function.
-   When the application is finished using the HTTP Server API, call the [**HttpTerminate**](/windows/win32/Http/nf-http-httpterminate?branch=master) function.

 

 




