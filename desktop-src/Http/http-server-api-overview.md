---
title: HTTP Server API Overview
description: This topic identifies a typical sequence of operations that use the HTTP Server API.
ms.assetid: 1245fd98-8370-4f1b-8c86-de9be5e678bd
ms.topic: article
ms.date: 05/31/2018
---

# HTTP Server API Overview

The following list identifies a typical sequence of operations that use the HTTP Server API:

-   Initialize the HTTP Server API by using the [**HttpInitialize**](/windows/desktop/api/Http/nf-http-httpinitialize) function.
-   Create a request queue by using the [**HttpCreateHttpHandle**](/windows/desktop/api/Http/nf-http-httpcreatehttphandle) function.
-   Register one or more URLs by using the [**HttpAddUrl**](/windows/desktop/api/Http/nf-http-httpaddurl) function.
-   Receive incoming requests directed to registered URLs by using the [**HttpReceiveHttpRequest**](/windows/desktop/api/Http/nf-http-httpreceivehttprequest) function, and send HTTP responses for these requests by using the [**HttpSendHttpResponse**](/windows/desktop/api/Http/nf-http-httpsendhttpresponse) function.
-   (Optional) When sending a response, send an additional entity body by using the [**HttpSendResponseEntityBody**](/windows/desktop/api/Http/nf-http-httpsendresponseentitybody) function.
-   Perform clean-up operations by using the [**HttpRemoveUrl**](/windows/desktop/api/Http/nf-http-httpremoveurl), [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) and [**HttpTerminate**](/windows/desktop/api/Http/nf-http-httpterminate) functions.

In operations that use URLs, note that it is the processed URL contained in the **CookedUrl** member of the [**HTTP\_REQUEST\_V1**](/windows/desktop/api/Http/ns-http-http_request_v1) structure that should be used. Do not use the unprocessed URL in the **pRawUrl** member, which is solely for tracking and statistical purposes.

Each application creates its own request queue. An application obtains its request queue handle from [**HttpCreateHttpHandle**](/windows/desktop/api/Http/nf-http-httpcreatehttphandle). It passes this handle to the [**HttpAddUrl**](/windows/desktop/api/Http/nf-http-httpaddurl) function to add a URL to the request queue. The application receives notification of an incoming request, and retrieves it from the request queue by calling the [**HttpReceiveHttpRequest**](/windows/desktop/api/Http/nf-http-httpreceivehttprequest) function with the request queue handle. You can use this function to receive either the request headers or both the headers and entity body. [**HttpReceiveHttpRequest**](/windows/desktop/api/Http/nf-http-httpreceivehttprequest) also returns a request identifier (RequestId) for the received request that is unique to the request handle.

> [!Note]  
> It is the application's responsibility to examine all relevant request headers, including content-negotiation headers if they are being used, and fail requests as appropriate based on header content. The HTTP Server API ensures only that each header line is properly terminated, and does not contain illegal characters.

 

Use the [**HttpReceiveRequestEntityBody**](/windows/desktop/api/Http/nf-http-httpreceiverequestentitybody) function with the request queue handle to retrieve subsequent portions of a request's entity body, if any.

> [!Note]  
> The HTTP Server API decodes chunked messages on the receive side, but does not perform chunked encoding on the send side. If chunking is required on the send side, the application must implement it. For more information about chunked encoding, see [RFC 2616](https://www.ietf.org/rfc/rfc2616.txt).

 

Use the [**HttpReceiveClientCertificate**](/windows/desktop/api/Http/nf-http-httpreceiveclientcertificate) function with applications that serve URLs by using a secure scheme ("**https**") to optionally retrieve the client's certificate information.

Responses are sent with the [**HttpSendHttpResponse**](/windows/desktop/api/Http/nf-http-httpsendhttpresponse) function. This function uses the RequestId from the corresponding request to send the response. A response can be sent in several API calls over time by calling the [**HttpSendResponseEntityBody**](/windows/desktop/api/Http/nf-http-httpsendresponseentitybody) function with the RequestId from the originally received request.

> [!Note]  
> By default, [**HttpSendHttpResponse**](/windows/desktop/api/Http/nf-http-httpsendhttpresponse) uses "Microsoft-HTTPAPI/1.0" as the "Server:" header. If an application specifies a server header in a response, that value is placed as the first part of the server header, followed by a space and then "Microsoft-HTTPAPI/1.0".

 

In general, the HTTP Server API hides details of connection management and their establishment and teardown from applications. However, an application can optionally detect termination of a connection by calling [**HttpWaitForDisconnect**](/windows/desktop/api/Http/nf-http-httpwaitfordisconnect).

Applications must clean-up by using the following steps:

-   When the application is not listening or responding to a URL, the URL is removed by using the [**HttpRemoveURL**](/windows/desktop/api/Http/nf-http-httpremoveurl) function.
-   When the application is finished using the request queue, close the request queue handle by using the [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) function.
-   When the application is finished using the HTTP Server API, call the [**HttpTerminate**](/windows/desktop/api/Http/nf-http-httpterminate) function.

 

 
