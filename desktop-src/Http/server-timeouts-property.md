---
title: Server Timeouts Property
description: Server Timeouts Property
ms.assetid: 5525c226-3786-41c4-86a2-3e077682313d
keywords:
- Server Timeouts Property HTTP
ms.topic: article
ms.date: 05/31/2018
---

# Server Timeouts Property

The HTTP Server API enables applications to set the server connection timeout limits on a server session or a URL group. The HTTP timeouts property is used to set all timeouts on an application-specific basis. The **IdleConnection** and **HeaderWait** timers can also be configured HTTP Server API-wide. When the timers are configured HTTP Server API-wide, they apply to all the HTTP Server API applications on the computer and the settings persist when the service is restarted.

For more information about configuring timers, see [Configuring the Application Specific Timeouts](configuring-the-application-specific-timeouts.md).

When the timers are not configured for a URL group or server session, the HTTP Server API default configurations apply.

The order of timeout enforcement is as follows:

1.  The HTTP Server API-wide defaults apply to all the HTTP Server API applications on the computer.
2.  The Server Session timeouts override the HTTP Server API-wide settings, when set.
3.  The URL group settings override the server session configurations, when set.

The following table lists the default connection timeout limits



| Timer           | Definition                                                                                                        | HTTP Server API default | Configurable as HTTP Server API wide | Configurable as Application specific |
|-----------------|-------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------|--------------------------------------|
| IdleConnection  | The connection expired while staying idle.                                                                        | 120 Sec                 | Yes                                  | Limited                              |
| HeaderWait      | The connection expired while waiting for the HTTP Server API to parse the header.                                 | 120 Sec                 | Yes                                  | Limited                              |
| EntityBody      | The connection expired while waiting for the request entity body to arrive.                                       | 120 Sec                 | No                                   | Yes                                  |
| DrainEntityBody | The connection expired while waiting for the HTTP Server API to drain the entity body on a Keep-Alive connection. | 120 Sec                 | No                                   | Yes                                  |
| MinSendRate     | The connection expired because the response send rate was slower than the default of 150 bytes/sec.               | 150 Sec                 | No                                   | Yes                                  |
| RequestQueue    | The connection expired because the request remained in the request queue before the application picked it up.     | 120 Bytes/Sec           | No                                   | Yes                                  |



 

 

 




