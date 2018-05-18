---
title: HTTP Server API Version 1.0 Functions
description: The HTTP Server API provides the following functions for writing applications.
ms.assetid: '1da9907d-a09d-41e1-aca1-9a8e2b91296f'
keywords: ["HTTP Server API Version 1.0 Functions", "Functions HTTP , HTTP Server API Version 1.0"]
---

# HTTP Server API Version 1.0 Functions

The HTTP Server API provides the following functions for writing applications.

## General



| Function                                             | Description                                                                                                                       |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**HttpCreateHttpHandle**](httpcreatehttphandle.md) | Creates an HTTP request queue and returns a handle to it.                                                                         |
| [**HttpInitialize**](httpinitialize.md)             | Initializes the HTTP Server API for use by the calling process.                                                                   |
| [**HttpPrepareUrl**](httpprepareurl.md)             | Parses, analyzes, and normalizes a non-normalized Unicode or punycode URL so it is safe and valid to use in other HTTP functions. |
| [**HttpTerminate**](httpterminate.md)               | Directs the HTTP Server API to clean up any resources associated with a particular process.                                       |



 

## Cache Management



| Function                                                       | Description                                                                                            |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**HttpAddFragmentToCache**](httpaddfragmenttocache.md)       | Caches a data fragment so that it can be used to compose a dynamic response without reading from disk. |
| [**HttpFlushResponseCache**](httpflushresponsecache.md)       | Removes specified cached fragments from the HTTP cache.                                                |
| [**HttpReadFragmentFromCache**](httpreadfragmentfromcache.md) | Retrieves a specified cached response fragment.                                                        |



 

## Configuration



| Function                                                                 | Description                                                       |
|--------------------------------------------------------------------------|-------------------------------------------------------------------|
| [**HttpDeleteServiceConfiguration**](httpdeleteserviceconfiguration.md) | Deletes specified information from the HTTP configuration store.  |
| [**HttpQueryServiceConfiguration**](httpqueryserviceconfiguration.md)   | Queries the HTTP configuration store for specified information.   |
| [**HttpSetServiceConfiguration**](httpsetserviceconfiguration.md)       | Sets specified values in the HTTP Server API configuration store. |



 

## Input and Output



| Function                                                             | Description                                                    |
|----------------------------------------------------------------------|----------------------------------------------------------------|
| [**HttpReceiveHttpRequest**](httpreceivehttprequest.md)             | Retrieves an HTTP request from a specified request queue.      |
| [**HttpReceiveRequestEntityBody**](httpreceiverequestentitybody.md) | Retrieves entity-body data of a particular HTTP request.       |
| [**HttpSendHttpResponse**](httpsendhttpresponse.md)                 | Sends an HTTP response for a particular HTTP request.          |
| [**HttpSendResponseEntityBody**](httpsendresponseentitybody.md)     | Sends entity-body data of an HTTP response.                    |
| [**HttpWaitForDisconnect**](httpwaitfordisconnect.md)               | Notifies the application when an HTTP client has disconnected. |



 

## SSL



| Function                                                             | Description                                             |
|----------------------------------------------------------------------|---------------------------------------------------------|
| [**HttpReceiveClientCertificate**](httpreceiveclientcertificate.md) | Retrieves the client certificate for an SSL connection. |



 

## URL Registration



| Function                               | Description                                                                                     |
|----------------------------------------|-------------------------------------------------------------------------------------------------|
| [**HttpAddUrl**](httpaddurl.md)       | Registers a URL so that HTTP requests for it are routed to a specified request queue.           |
| [**HttpRemoveUrl**](httpremoveurl.md) | Unregisters a specified URL, so that requests for it are no longer routed to a specified queue. |



 

## Related topics

<dl> <dt>

[HTTP Server API Version 1.0 Structures](http-server-api-version-1-0-structures.md)
</dt> </dl>

 

 




