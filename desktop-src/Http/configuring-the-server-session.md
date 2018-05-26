---
title: Configuring the Server Session
description: .
ms.assetid: 1e4e9440-8d70-44df-90a7-2d5e25b2f680
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Configuring the Server Session

The server session ID is created with the [**HttpCreateServerSession**](/windows/win32/Http/nf-http-httpcreateserversession?branch=master) function, and used in the call to [**HttpSetServerSessionProperty**](/windows/win32/Http/nf-http-httpsetserversessionproperty?branch=master). The *pPropertyInformation* parameter points to the configuration structure for the property type that is set. The *PropertyInformationLength* parameter specifies the size, in bytes, of the configuration structure. For example, when setting the **HttpServerTimeoutsProperty** the **pPropertyInformation** parameter must point to a buffer that is at least the size of the [**HTTP\_TIMEOUT\_LIMIT\_INFO**](/windows/win32/Http/ns-http-_http_timeout_limit_info?branch=master) structure.

Typically an HTTP application creates a single server session and may set application wide properties such as global bandwidth throttling limit or enable centralized logging on this server session. [**HttpSetServerSessionProperty**](/windows/win32/Http/nf-http-httpsetserversessionproperty?branch=master) overrides the HTTP Server API configurations for the calling application; it does not affect the HTTP Server API-wide properties. The server session configurations are queried by calling [**HttpQueryServerSessionProperty**](/windows/win32/Http/nf-http-httpqueryserversessionproperty?branch=master).

 

 




