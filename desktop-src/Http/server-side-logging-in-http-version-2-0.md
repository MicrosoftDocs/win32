---
title: Server-Side Logging
description: Server-side logging is available on a URL group or server session.
ms.assetid: e1fcd87f-382a-42bf-b53f-1e1cb1dbbfc5
ms.topic: article
ms.date: 05/31/2018
---

# Server-Side Logging

Server-side logging is available on a URL group or server session. When logging is enabled on a server session, it functions as centralized form of logging for all the URL groups under the server session. When logging is enabled on a URL group, logging is performed only on requests that are routed to the URL Group. The following types of logging are supported by the HTTP Server API:

-   [W3C logging](w3c-logging.md): Available on the server session and URL group.
-   [NCSA logging](ncsa-logging.md): Available on the URL group.
-   [IIS logging](iis-logging.md): Available on the URL group.
-   [Centralized binary logging](centralized-binary-logging.md): Available on the server session.

To take advantage of the HTTP logging feature, the application enables and configures one type of logging on the server session or URL group. For more information, see [Configuring and Enabling Server Side Logging](configuring-and-enabling-server-side-logging.md)

 

 




