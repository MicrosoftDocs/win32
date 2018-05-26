---
title: Implementing Terminate
description: The Terminate entry point function is used to immediately end a process that does not shut down gracefully when the Offline function is called.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: df6edc61-d325-46a5-b486-079a52dfaf77
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- entry point functions Failover Cluster ,implementing Terminate
- Terminate Failover Cluster ,implementing
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Implementing Terminate

The [**Terminate**](/windows/previous-versions/ResApi/nc-resapi-pterminate_routine?branch=master) entry point function is used to immediately end a process that does not shut down gracefully when the [**Offline**](/windows/previous-versions/ResApi/nc-resapi-poffline_routine?branch=master) function is called.

**To implement Terminate**

1.  Required: The [**Terminate**](/windows/previous-versions/ResApi/nc-resapi-pterminate_routine?branch=master) entry point function can be called concurrently with the [**IsAlive**](/windows/previous-versions/ResApi/nc-resapi-pis_alive_routine?branch=master), [**LooksAlive**](/windows/previous-versions/ResApi/nc-resapi-plooks_alive_routine?branch=master), [**Offline**](/windows/previous-versions/ResApi/nc-resapi-poffline_routine?branch=master), [**Online**](/windows/previous-versions/ResApi/nc-resapi-ponline_routine?branch=master), [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master), and [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) entry point functions. Any resources that are accessed by these entry points must be properly guarded.

2.  Recommended: For optimal performance, return within 300 milliseconds. However, the [Cluster service](cluster-service.md) handles the situation properly if this time limit is exceeded.

## Example

See [Resource DLL Examples](https://msdn.microsoft.com/library/aa370474).

 

 




