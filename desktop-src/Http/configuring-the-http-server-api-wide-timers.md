---
title: Configuring the HTTP Server API Wide Timers
description: Configuring the HTTP Server API Wide Timers
ms.assetid: 34f80bac-a7c5-4949-9c15-ed63a3582e26
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Configuring the HTTP Server API Wide Timers

The HTTP Server API-wide **HeaderWait** and **IdleConnection** timers are configured by calling the version 1.0 [**HttpSetServiceConfiguration**](/windows/win32/Http/nf-http-httpsetserviceconfiguration?branch=master) function. The *ConfigId* parameter is set to **HttpServiceConfigTimeout** and the *pConfigInformation* parameter specifies the [**HTTP\_SERVICE\_CONFIG\_TIMEOUT\_SET**](/windows/win32/Http/ns-http-_http_service_config_timeout_set?branch=master) structure that contains the timer that is set and the value for the timer.

Configuring the HTTP Server API-wide timeouts requires administrative privileges, however querying them does not. These configurations are set for all applications on the computer and they persist when the HTTP service is restarted or the computer is restarted. To query existing HTTP Server API-wide timeouts, the application calls [**HttpQueryServiceConfiguration**](/windows/win32/Http/nf-http-httpqueryserviceconfiguration?branch=master).

 

 




