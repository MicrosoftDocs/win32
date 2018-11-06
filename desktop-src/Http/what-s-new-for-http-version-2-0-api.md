---
title: What's New for HTTP Server Version 2.0 API
description: The following features are available in the HTTP Server version 2.0 API.
ms.assetid: 236fdbb0-dead-4b73-9ef6-be2d502b5243
keywords:
- What's New for HTTP Server version 2.0 API
- HTTP Server version 2.0 API, What's New
ms.topic: article
ms.date: 05/31/2018
---

# What's New for HTTP Server Version 2.0 API

The HTTP Server version 2.0 API adds property configuration objects and advanced request queue management. For more information and a complete list of functions, see the [HTTP Server Version 2.0 Reference](http-server-api-version-2-0-reference.md) topic. The following features are available in the HTTP Server version 2.0 API.

## Configuration Objects

The server session and URL group configuration objects enable applications to configure the HTTP service. The server session is the top-level configuration object that overrides the HTTP Server API default settings for all the URL groups created under the session. The URL group, created under a server session, maintains a set of URLs that receive the configuration settings for the group. For more information, see the [HTTP Version 2.0 Architecture](http-version-2-0-architecture.md) topic.

## Property Configuration in Version 2.0

Configuration is performed on the server session, or URL group objects. Server-wide configurations are set on the server session configuration object. The URL groups, created under the server session, inherit the server session configurations. Configurations set on the URL group override the server session configurations. Configurations that can be set by the application include connection timeouts, connections limits, authentication, and logging. For more information, see the [Configuring Properties in HTTP Version 2.0](configuring-properties-in-http-version-2-0.md) topic.

## Process Isolation on Request Queues

The version 2.0 request queue supports process isolation, allowing multiple worker processes to perform IO on the request queue. Configuration properties set on the request queue allow applications to have more control over the service. The named request queue feature allows applications to create request queues and secure them with Access Control Lists (ACL). Applications operating under user accounts other than the account that created the request queue are able to open the request queue, receive requests, and send responses. For more information, see the [Process Isolation](process-isolation.md) topic.

## Full Kernel Mode SSL

Kernel mode SSL security is enabled by default; client certificates for mutual authentication are also supported. Performance is increased by completing SSL operations in kernel mode, thus reducing transitions between kernel and user mode. For more information, see the [Kernel Mode SSL](kernel-mode-ssl.md) topic.

## Kernel mode response cache

Responses with static content can be cached in kernel mode providing increased performance over the user mode cache. The cache policy structure is sent with the response. For more information, see the [Kernel Mode Cache in HTTP 2.0](kernel-mode-cache-in-http-2-0.md) topic.

## Authentication

The HTTP\_RESPONSE and HTTP\_REQUEST structures are updated to include authentication information. Server-side authentication is supported for the following schemes: Negotiate, NTLM, Basic, and Digest. Applications can specify the supported authentication schemes and set the order of preference for those schemes.

## Object Scoped Versioning

The HTTP Server version 1.0 API passed version information in the call to HTTPInitialize. The version was set globally for all applications in the same process. In the HTTP Server version 2.0 API, the version information is supplied when the object is created. For more information, see [Versioning in HTTP Server Version 2.0 API](versioning-in-http-2-0.md).

## Logging

Starting with version 2.0, logging is configurable through the HTTP Server API. Logging enabled on a server session serves as centralized form of logging for the service. Logging can also be enabled on a URL group for individualized log files. The application specifies the format for the log files as well as the fields that are logged for errors and successful transactions.

## Graceful Request Queue Shutdown

Applications can shut down the request queue and gracefully handle outstanding requests in the queue before terminating the request queue process. When the request queue is shutdown, the HTTP Server API stops queuing requests and re-routes outstanding requests in the request queue.

## Demand Start on a Request Queue

The demand start feature on the request queue allows the controller application to delay worker process instantiation until the first request arrives on the request queue. Thus, applications can avoid consuming resources until they are required. For more information, see the [Demand Start on Version 2.0 Request Queues](demand-start-on-version-2-0-request-queues.md) topic.

## Port Sharing

HTTP Server API-based applications automatically share the IP listen space with other non-HTTP Server API-based applications on the computer; the IP listen list is no longer required. When the application registers a URL, the HTTP Server API listens only on the specified IP address and port pair.

## ETW Support

Advanced tracing using the Event Tracing for Windows (ETW) allows applications greater diagnostic abilities. Event tracing is available for URL registrations and reservations, property configuration, cache events, authentication, and logging to name a few.

## Performance Counters

The performance counter tool allows applications to retrieve service counters and diagnose service performance. Global counters track performance for the service, site counters track URL group performance, and request queue counters track performance of the request queue.

## International Domain Names (IDN)

Internationalized host and path portions of the URL allow registration of non-ASCII domain names and paths. The HTTP Server API processes Unicode URLs to comply with IDN standards.

## NetSH Extensions

The netsh utility replaces the HttpCfg.exe tool available in Windows Server 2003 and Windows XP with Service Pack 2 (SP2). The netsh extension provides a means of managing, diagnosing, and configuring the HTTP service. Administrators can query and configure server-wide settings such as namespace registrations and SSL certificates.

 

 




