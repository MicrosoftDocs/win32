---
title: HTTP Server Tasks
description: Typically, HTTP server tasks are performed in a specific order; that is, one task must be completed and the output obtained before the next task begins.
ms.assetid: 08f8e7e9-23b9-403f-b00c-8912919d65b1
keywords:
- HTTP Server Tasks
ms.topic: article
ms.date: 05/31/2018
---

# HTTP Server Tasks

Typically, HTTP server tasks are performed in a specific order; that is, one task must be completed and the output obtained before the next task begins.

A task page is created to present sample code about specific tasks that an HTTP Server application performs. A task page links to the C extension file of the HTTP server sample. When you install the PSDK on drive C:\\ of a local computer, the complete server sample application is installed at C:\\Program Files\\Microsoft SDK\\Samples\\netds\\http\\server.

The following list identifies the HTTP Server tasks:

-   [Initialize the HTTP Service](#initialize-the-http-service)
-   [Register the URLs to Listen On](#register-the-urls-to-listen-on)
-   [Call the Routine to Receive a Request](#call-the-routine-to-receive-a-request)
-   [Receive the Request](#receive-the-request)
-   [Handle the HTTP Request](#handle-the-http-request)
-   [Send the HTTP Response](#send-the-http-response)
-   [Send the HTTP POST Response](#send-the-http-post-response)
-   [Clean Up the HTTP Server API](#clean-up-the-http-server-api)

## Initialize the HTTP Service

The HTTP service is initialized by using the [**HttpInitialize**](/windows/desktop/api/Http/nf-http-httpinitialize) function, and the handle to the request queue is created by using [**HttpCreateHttpHandle**](/windows/desktop/api/Http/nf-http-httpcreatehttphandle). The server must be initialized before any other server functions can be called. The request queue must be created before the service can register URLs to listen for incoming HTTP requests.

For more information and a code example, see [Initialize the HTTP Service](http-server-sample-application.md).

## Register the URLs to Listen On

For the HTTP Server API to listen for incoming requests, specific URLs are registered with the API by calling the [**HttpAddUrl**](/windows/desktop/api/Http/nf-http-httpaddurl) function. Incoming requests that match these URLs are routed to the request queue specified in this call.

For more information and a code example, see [Register the URLs to Listen On](http-server-sample-application.md).

## Call the Routine to Receive a Request

The DoReceiveRequest function allocates the request buffer, initializes the request ID, and starts the loop to receive requests.

For more information and a code example, see [Call the Routine to Receive a Request](http-server-sample-application.md).

## Receive the Request

The HTTP Server API supplies a request structure to store the parsed incoming request. This structure is allocated by the application, and initialized when an incoming request is received. The application calls the [**HttpReceiveHttpRequest**](/windows/desktop/api/Http/nf-http-httpreceivehttprequest) function to receive the request. If the request buffer is too small to receive the request, the application can increase the buffer size and call **HttpReceiveHttpRequest** again to receive the entire request.

For more information and a code example, see [Receive a Request](http-server-sample-application.md).

## Handle the HTTP Request

The sample application shows how to handle the HTTP GET and POST request verbs. The application sends a 503 (**NOT\_IMPLEMENTED**) error if verbs are present in the request that the application does not handle.

Note that the URL to be used in handling requests is the processed URL contained in the **CookedUrl** member of the [**HTTP\_REQUEST\_V1**](/windows/desktop/api/Http/ns-http-http_request_v1) structure. Do not the unprocessed URL in the **pRawUrl** member, which is solely for tracking and statistical purposes.

For more information and a code example, see [Handle the HTTP Request](http-server-sample-application.md).

## Send the HTTP Response

The response structure is allocated and initialized with the status code and a reason phrase in the INITIALIZE\_HTTP\_RESPONSE macro. A known HTTP header is added into the response structure in the ADD\_KNOWN\_HEADER macro, and the entity body is added to the response from a data block from memory. The [**HttpSendHttpResponse**](/windows/desktop/api/Http/nf-http-httpsendhttpresponse) function is called to send the response. In this example, the application sends a simple 200 OK response to the GET request.

For more information and a code example, see [Send an HTTP Response](http-server-sample-application.md).

## Send the HTTP POST Response

The POST request requires more processing than the GET request. The request entity body is received by calling the [**HttpReceiveRequestEntityBody**](/windows/desktop/api/Http/nf-http-httpreceiverequestentitybody) function. The application sends the response and the response entity body in separate calls to the HTTP Server API. The response headers are sent with the [**HttpSendHttpResponse**](/windows/desktop/api/Http/nf-http-httpsendhttpresponse). The entity body is sent in a data block from a file handle with the [**HttpSendResponseEntityBody**](/windows/desktop/api/Http/nf-http-httpsendresponseentitybody) function.

For more information and a code example, see [Send an HTTP POST Response](http-server-sample-application.md).

## Clean Up the HTTP Server API

The cleanup operations for the HTTP Server API include:

-   Removing all registered URLs.
-   Closing the handle to the request queue.
-   Terminating the resources created by the HTTP Server API.

The application calls the [**HttpRemoveUrl**](/windows/desktop/api/Http/nf-http-httpremoveurl) function to deregister URLs registered by the initial [**HttpAddUrl**](/windows/desktop/api/Http/nf-http-httpaddurl) function. The application also calls [**HttpTerminate**](/windows/desktop/api/Http/nf-http-httpterminate) for each call to [**HttpInitialize**](/windows/desktop/api/Http/nf-http-httpinitialize) with matching flag settings. This call terminates all resources created by the call to **HttpInitialize**.

For more information and a code example, see [Cleanup the HTTP Server API](http-server-sample-application.md).

 

 




