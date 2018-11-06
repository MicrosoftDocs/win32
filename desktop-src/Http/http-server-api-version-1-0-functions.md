---
title: HTTP Server API Version 1.0 Functions
description: The HTTP Server API provides the following functions for writing applications.
ms.assetid: 1da9907d-a09d-41e1-aca1-9a8e2b91296f
keywords:
- HTTP Server API Version 1.0 Functions
- Functions HTTP , HTTP Server API Version 1.0
ms.topic: article
ms.date: 05/31/2018
---

# HTTP Server API Version 1.0 Functions

The HTTP Server API provides the following functions for writing applications.

## General



| Function                                             | Description                                                                                                                       |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**HttpCreateHttpHandle**](/windows/desktop/api/Http/nf-http-httpcreatehttphandle) | Creates an HTTP request queue and returns a handle to it.                                                                         |
| [**HttpInitialize**](/windows/desktop/api/Http/nf-http-httpinitialize)             | Initializes the HTTP Server API for use by the calling process.                                                                   |
| [**HttpPrepareUrl**](/windows/desktop/api/Http/nf-http-httpprepareurl)             | Parses, analyzes, and normalizes a non-normalized Unicode or punycode URL so it is safe and valid to use in other HTTP functions. |
| [**HttpTerminate**](/windows/desktop/api/Http/nf-http-httpterminate)               | Directs the HTTP Server API to clean up any resources associated with a particular process.                                       |



 

## Cache Management



| Function                                                       | Description                                                                                            |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**HttpAddFragmentToCache**](/windows/desktop/api/Http/nf-http-httpaddfragmenttocache)       | Caches a data fragment so that it can be used to compose a dynamic response without reading from disk. |
| [**HttpFlushResponseCache**](/windows/desktop/api/Http/nf-http-httpflushresponsecache)       | Removes specified cached fragments from the HTTP cache.                                                |
| [**HttpReadFragmentFromCache**](/windows/desktop/api/Http/nf-http-httpreadfragmentfromcache) | Retrieves a specified cached response fragment.                                                        |



 

## Configuration



| Function                                                                 | Description                                                       |
|--------------------------------------------------------------------------|-------------------------------------------------------------------|
| [**HttpDeleteServiceConfiguration**](/windows/desktop/api/Http/nf-http-httpdeleteserviceconfiguration) | Deletes specified information from the HTTP configuration store.  |
| [**HttpQueryServiceConfiguration**](/windows/desktop/api/Http/nf-http-httpqueryserviceconfiguration)   | Queries the HTTP configuration store for specified information.   |
| [**HttpSetServiceConfiguration**](/windows/desktop/api/Http/nf-http-httpsetserviceconfiguration)       | Sets specified values in the HTTP Server API configuration store. |



 

## Input and Output



| Function                                                             | Description                                                    |
|----------------------------------------------------------------------|----------------------------------------------------------------|
| [**HttpReceiveHttpRequest**](/windows/desktop/api/Http/nf-http-httpreceivehttprequest)             | Retrieves an HTTP request from a specified request queue.      |
| [**HttpReceiveRequestEntityBody**](/windows/desktop/api/Http/nf-http-httpreceiverequestentitybody) | Retrieves entity-body data of a particular HTTP request.       |
| [**HttpSendHttpResponse**](/windows/desktop/api/Http/nf-http-httpsendhttpresponse)                 | Sends an HTTP response for a particular HTTP request.          |
| [**HttpSendResponseEntityBody**](/windows/desktop/api/Http/nf-http-httpsendresponseentitybody)     | Sends entity-body data of an HTTP response.                    |
| [**HttpWaitForDisconnect**](/windows/desktop/api/Http/nf-http-httpwaitfordisconnect)               | Notifies the application when an HTTP client has disconnected. |



 

## SSL



| Function                                                             | Description                                             |
|----------------------------------------------------------------------|---------------------------------------------------------|
| [**HttpReceiveClientCertificate**](/windows/desktop/api/Http/nf-http-httpreceiveclientcertificate) | Retrieves the client certificate for an SSL connection. |



 

## URL Registration



| Function                               | Description                                                                                     |
|----------------------------------------|-------------------------------------------------------------------------------------------------|
| [**HttpAddUrl**](/windows/desktop/api/Http/nf-http-httpaddurl)       | Registers a URL so that HTTP requests for it are routed to a specified request queue.           |
| [**HttpRemoveUrl**](/windows/desktop/api/Http/nf-http-httpremoveurl) | Unregisters a specified URL, so that requests for it are no longer routed to a specified queue. |



 

## Related topics

<dl> <dt>

[HTTP Server API Version 1.0 Structures](http-server-api-version-1-0-structures.md)
</dt> </dl>

 

 




