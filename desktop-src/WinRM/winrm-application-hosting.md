---
title: Infrastructure for Managing Hosted Services
description: Windows Remote Management 2.0 (WinRM) introduces a hosting framework. To use the framework, WinRM plug-ins are written that expose management data of an application within the WinRM infrastructure.
ms.assetid: 924dcc70-9a29-45a6-99a2-5681235e4574
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Infrastructure for Managing Hosted Services

Windows Remote Management 2.0 (WinRM) introduces a hosting framework. To use the framework, WinRM plug-ins are written that expose management data of an application within the WinRM infrastructure. Two hosting models are supported. One is Internet Information Services (IIS)â€“based and the other is WinRMâ€“service based. The WinRM-based model uses HTTP.sys and does not depend on IIS.

The following sections describe the hosting models:

-   [WinRM IIS Extension Hosting Model](#winrm-iis-extension-hosting-model)
    -   [Load Balancing in the WinRM IIS Extension Hosting Model](#load-balancing-in-the-winrm-iis-extension-hosting-model)
    -   [HTTP Redirection in the WinRM IIS Extension Hosting Model](#http-redirection-in-the-winrm-iis-extension-hosting-model)
-   [WinRM Service Hosting Model](#winrm-service-hosting-model)

## WinRM IIS Extension Hosting Model

The WinRM IIS extension module is an optional component that is installed using the **Server Manager**. The WinRM IIS extension module is used to create WinRMâ€“enabled endpoints from within the IIS service. This module can be enabled at either the website or virtual directory level. It works by intercepting and redirecting incoming requests to the associated website or virtual directory. The requests are redirected to a WinRM module that analyzes the content and then determines which WinRM plug-in is configured to handle each request. For more information, see [IIS Host Plug-in Configuration](iis-host-plug-in-configuration.md).

The WinRM IIS extension hosting model is designed to handle a large volume of requests. If the IIS-based model is used as the hosting framework, the following features are available:

-   The standard IIS authentication modules.
-   The IIS application pool process for hosting all plug-ins.
-   Quota management for throttling heavy users of the system. For more information, see [Quota Management for Remote Shells](quotas.md).
-   A shell plug-in model. See [WinRM Client Shell API](client-shell-api.md).
-   A flexible authorization model. See [WinRM Plugin API](winrm-plugin-api.md).

### Load Balancing in the WinRM IIS Extension Hosting Model

Most load balancers (LBs) support a cookie-based stickiness model. The LB inserts a cookie into the response to the first request from the client. For all subsequent requests, the cookie is transmitted in the request and the LB uses the cookie to route the request to the appropriate server.

In environments where WinRM 2.0 is hosted behind an LB, the LB should be configured to prefix MS-WSMAN to the name of the cookie. In addition, the LB needs to be configured to allow the lifetime of the cookie to be infinite, because the WinRM client should control how long the cookie is valid.

The following is an example of a cookie name:

``` syntax
MS-WSMAN=2046820362.20480.0000; path=/
```

### HTTP Redirection in the WinRM IIS Extension Hosting Model

WinRM 2.0 can handle HTTP redirection. It is recommended that all redirection use Secure Sockets Layer (SSL), and that all applications validate the redirected URI before creating a new session.

## WinRM Service Hosting Model

The WinRM service-based model runs on top of HTTP.sys. The WinRM service is a network facing service that handles requests from WinRM clients. The service determines whether the request is routed to a plug-in that runs in the main service or is routed through a host where the third-party plug-in is run. This model is intended for scenarios where the load on the managed node is low. Moreover, this model is intended for scenarios where IIS hosting is not an option. For more information, see [WinRM Service Plug-in Configuration](wsman-service-plug-in-configuration.md).

 

 




