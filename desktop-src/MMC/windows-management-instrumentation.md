---
title: Windows Management Instrumentation
description: Introduces WMI.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f7fa75c6-1b11-425d-a792-94afeb0d39c9'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Windows Management Instrumentation

WMI is the Microsoft implementation of the Web-Based Enterprise Management (WBEM) standard.

WBEM is an industry initiative, overseen by the Distributed Management Task Force (DMTF), to develop a standardized, nonproprietary means for accessing and sharing management information in an enterprise network. It is intended to alleviate the problems usually associated with collecting management and diagnostic data that can include different types of hardware, protocols, operating systems, and distributed applications.

In the context of MMC and snap-ins, WMI offers a simple interface to management data that includes:

-   A rich and consistent model of the Windows operating system's behavior, configuration, and status.
-   A COM API that supplies a single point of access to all management information.
-   Interoperability with other Windows management services.
-   A flexible architecture that enables vendors to extend the information model to cover new devices, applications, and services.
-   A rich query language that enables SQL-based queries of the information model.
-   A scriptable API that allows seamless local and remote system administration.

Snap-in developers can use WMI as the interface to local and remote managed objects. The underlying WBEM technology ensures access to virtually all objects in an enterprise network.

For more information about WMI, see the [Windows Management Instrumentation](https://msdn.microsoft.com/library/aa394582) main page.

 

 




