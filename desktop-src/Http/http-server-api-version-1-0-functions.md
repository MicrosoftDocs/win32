---
title: HTTP Server API Version 1.0 Functions
description: The HTTP Server API provides the following functions for writing applications.
ms.assetid: 1da9907d-a09d-41e1-aca1-9a8e2b91296f
keywords:
- HTTP Server API Version 1.0 Functions
- Functions HTTP , HTTP Server API Version 1.0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HTTP Server API Version 1.0 Functions

The HTTP Server API provides the following functions for writing applications.

## General



| Function                                             | Description                                                                                                                       |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**HttpCreateHttpHandle**](/windows/win32/Http/nf-http-httpcreatehttphandle?branch=master) | Creates an HTTP request queue and returns a handle to it.                                                                         |
| [**HttpInitialize**](/windows/win32/Http/nf-http-httpinitialize?branch=master)             | Initializes the HTTP Server API for use by the calling process.                                                                   |
| [**HttpPrepareUrl**](/windows/win32/Http/nf-http-httpprepareurl?branch=master)             | Parses, analyzes, and normalizes a non-normalized Unicode or punycode URL so it is safe and valid to use in other HTTP functions. |
| [**HttpTerminate**](/windows/win32/Http/nf-http-httpterminate?branch=master)               | Directs the HTTP Server API to clean up any resources associated with a particular process.                                       |



 

## Cache Management



| Function                                                       | Description                                                                                            |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**HttpAddFragmentToCache**](/windows/win32/Http/nf-http-httpaddfragmenttocache?branch=master)       | Caches a data fragment so that it can be used to compose a dynamic response without reading from disk. |
| [**HttpFlushResponseCache**](/windows/win32/Http/nf-http-httpflushresponsecache?branch=master)       | Removes specified cached fragments from the HTTP cache.                                                |
| [**HttpReadFragmentFromCache**](/windows/win32/Http/nf-http-httpreadfragmentfromcache?branch=master) | Retrieves a specified cached response fragment.                                                        |



 

## Configuration



| Function                                                                 | Description                                                       |
|--------------------------------------------------------------------------|-------------------------------------------------------------------|
| [**HttpDeleteServiceConfiguration**](/windows/win32/Http/nf-http-httpdeleteserviceconfiguration?branch=master) | Deletes specified information from the HTTP configuration store.  |
| [**HttpQueryServiceConfiguration**](/windows/win32/Http/nf-http-httpqueryserviceconfiguration?branch=master)   | Queries the HTTP configuration store for specified information.   |
| [**HttpSetServiceConfiguration**](/windows/win32/Http/nf-http-httpsetserviceconfiguration?branch=master)       | Sets specified values in the HTTP Server API configuration store. |



 

## Input and Output



| Function                                                             | Description                                                    |
|----------------------------------------------------------------------|----------------------------------------------------------------|
| [**HttpReceiveHttpRequest**](/windows/win32/Http/nf-http-httpreceivehttprequest?branch=master)             | Retrieves an HTTP request from a specified request queue.      |
| [**HttpReceiveRequestEntityBody**](/windows/win32/Http/nf-http-httpreceiverequestentitybody?branch=master) | Retrieves entity-body data of a particular HTTP request.       |
| [**HttpSendHttpResponse**](/windows/win32/Http/nf-http-httpsendhttpresponse?branch=master)                 | Sends an HTTP response for a particular HTTP request.          |
| [**HttpSendResponseEntityBody**](/windows/win32/Http/nf-http-httpsendresponseentitybody?branch=master)     | Sends entity-body data of an HTTP response.                    |
| [**HttpWaitForDisconnect**](/windows/win32/Http/nf-http-httpwaitfordisconnect?branch=master)               | Notifies the application when an HTTP client has disconnected. |



 

## SSL



| Function                                                             | Description                                             |
|----------------------------------------------------------------------|---------------------------------------------------------|
| [**HttpReceiveClientCertificate**](/windows/win32/Http/nf-http-httpreceiveclientcertificate?branch=master) | Retrieves the client certificate for an SSL connection. |



 

## URL Registration



| Function                               | Description                                                                                     |
|----------------------------------------|-------------------------------------------------------------------------------------------------|
| [**HttpAddUrl**](/windows/win32/Http/nf-http-httpaddurl?branch=master)       | Registers a URL so that HTTP requests for it are routed to a specified request queue.           |
| [**HttpRemoveUrl**](/windows/win32/Http/nf-http-httpremoveurl?branch=master) | Unregisters a specified URL, so that requests for it are no longer routed to a specified queue. |



 

## Related topics

<dl> <dt>

[HTTP Server API Version 1.0 Structures](http-server-api-version-1-0-structures.md)
</dt> </dl>

 

 




