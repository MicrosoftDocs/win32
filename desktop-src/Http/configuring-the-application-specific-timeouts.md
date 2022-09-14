---
title: Configuring the Application Specific Timeouts
description: Configuring the Application Specific Timeouts
ms.assetid: 24526320-4174-4fc7-b45a-c1ec605e1666
keywords:
- Configuring the Application Specific Timeouts HTTP
ms.topic: article
ms.date: 05/31/2018
---

# Configuring the Application Specific Timeouts

The HTTP Server API-wide settings apply to all the server sessions and URL groups on the computer. These configurations can be overridden by the application by setting the application-specific timeout values. The server session timeouts override the HTTP Server API-wide timeouts and apply to all the URL groups created under them. Configuring the timeouts property on a URL group overrides the server session timeouts for all the URLs in the group.

Specifying zero for any of the timers in the [**HTTP\_TIMEOUT\_LIMIT\_INFO**](/windows/desktop/api/Http/ns-http-http_timeout_limit_info) structure for a URL group causes the HTTP Server API to revert to the server session timeouts, if they exist, or the HTTP Server API default settings if the server session timeouts do not exist. For example, when the server timeout property is present on a URL group and the **EntityBody** timer is zero, the server session timeout is used. If the timeouts property is not set on a server session, the HTTP Server API default configuration is used. To disable a timer, set the value to **MAXUSHORT**, except for the **MinSendRate** timer which is set to **MAXULONG**.

The HTTP Server API can only configure the application-specific **HeaderWait** and the **IdleConnection** timers are only effective after the first request has been received. Before the first request is received, the HTTP Server API-wide timeout values are enforced. After the first request arrives and is associated with a request queue, the application-specific **HeaderWait** and **IdleConnection** timers can be applied. The application-specific timers are applied to all subsequent requests that arrive on the request queue for a keep-alive connection.

For more information about configuring timers, see the [Configuring the URL Group](configuring-the-url-group.md) and [Configuring the Server Session](configuring-the-server-session.md) topics.

 

 




