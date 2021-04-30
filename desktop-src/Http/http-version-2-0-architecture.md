---
title: Architecture (HTTP Server API)
description: The server session, request queue, and URL group configuration objects enable applications to configure the HTTP service.
ms.assetid: 05a2d689-fd10-4065-85fc-2057bee42fbc
ms.topic: article
ms.date: 05/31/2018
---

# Architecture (HTTP Server API)

The server session, request queue, and URL group configuration objects enable applications to configure the HTTP service. The properties set on these objects override the HTTP Server API wide default configurations.

-   Server Session: The top-level configuration object that defines configurations for all the URL groups created under the session.
-   URL Group: The URL group, created under the server session, contains a set of URLs that inherit the configurations set on the server session. The URL group configurations override the server session configurations when set by the application. The URL group defines a portion of the namespace that the application is listening on and configures that portion of the namespace.
-   Request Queue: This object configures settings specific to the request queue. These configurations are applied to all the URLs in the groups associated with the request queue.

The diagram below shows the relationship between the configuration objects and the application. Typically, a single server session is created for each application with one or more URL groups created under it. The request queues are created independent of the URL group or server session. URL groups must be associated with a request queue to receive requests.

![relationship between the configuration objects and the application](images/architecture.png)

The named request queue feature of the HTTP Server version 2.0 API allows multiple worker processes to receive requests on a request queue. The request queue is created by a controller process that identifies the worker processes granted access to the request queue. For more information, see the [Named Request Queue](named-request-queue.md) topic

## Property Configuration

For more information about setting properties on the configuration objects, see the following topics:

-   [Configuring the Request Queue](configuring-the-request-queue.md)
-   [Configuring the Server Session](configuring-the-server-session.md)
-   [Configuring the URL Group](configuring-the-url-group.md)

The following table lists properties that are set on the configuration objects. For more information about property configurations, see the [Configuring Properties in HTTP Version 2.0](configuring-properties-in-http-version-2-0.md) topic.



| Name           | Property                                                                                                                                                                                                                                                                      |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Server Session | HttpServerStateProperty<br/> HttpServerLoggingProperty<br/> HttpServerBandwidthProperty<br/> HttpServerTimeoutsProperty<br/> HttpServerAuthenticatonProperty<br/>                                                                               |
| URL Group      | HttpServerStateProperty<br/> HttpServerAuthenticatonProperty<br/> HttpServerLoggingProperty<br/> HttpServerConnectionsProperty<br/> HttpServerBandwidthProperty<br/> HttpServerBindingProperty<br/> HttpServerTimeoutsProperty<br/> |
| Request Queue  | HttpServerStateProperty<br/> HttpServerQueueLengthProperty<br/> HttpServer503VerbosityProperty<br/>                                                                                                                                                         |



 

 

 





