---
title: WinRM Plug-in API
description: The WinRM Plug-in application programming interface (API) provides functionality that enables a user to write plug-ins by implementing certain APIs for supported resource URIs and operations.
ms.assetid: d3e103c1-221b-441b-8bcb-883e3f2a4c1a
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# WinRM Plug-in API

Windows Remote Management plug-ins are native dynamic-link libraries (DLLs) that plug into and extend the functionality of WinRM. The WinRM Plug-in application programming interface (API) provides functionality that enables a user to write plug-ins by implementing certain APIs for supported [*resource URIs*](windows-remote-management-glossary.md) and operations. After the plug-ins are configured for either the WinRM service or Internet Information Services (IIS), they are loaded into the WinRM host or IIS host, respectively. Remote requests are routed to these plug-in entry points to carry out operations.

The WinRM Plug-in API reference section contains detailed information about the following API elements:

-   [Authorization Plug-in Entry Points](authorization-plug-in-entry-points.md)
-   [Authorization Plug-in Methods](authorization-plug-in-methods.md)
-   [Operations Plug-in Entry Points](operations-plug-in-entry-points.md)
-   [Operations Plug-in Methods](operations-plug-in-methods.md)
-   [Structures](winrm-plug-in-api-structures.md)

 

 




