---
title: Implementing Pending Operations
description: If your Online or Offline entry point functions require more than 300 milliseconds, it is recommended that you use a worker thread to perform the operation asynchronously.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0934f698-8de4-489d-b2e7-0781c0a9a89f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- entry point functions Failover Cluster ,implementing pending operations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Implementing Pending Operations

If your [**Online**](/windows/previous-versions/ResApi/nc-resapi-ponline_routine?branch=master) or [**Offline**](/windows/previous-versions/ResApi/nc-resapi-poffline_routine?branch=master) entry point functions require more than 300 milliseconds, it is recommended that you use a worker thread to perform the operation asynchronously.

The following steps are all required:

**To Implement a Pending Operation**

1.  In your [**Online**](/windows/previous-versions/ResApi/nc-resapi-ponline_routine?branch=master) or [**Offline**](/windows/previous-versions/ResApi/nc-resapi-poffline_routine?branch=master) entry point function, call [**ClusWorkerCreate**](/windows/previous-versions/ResApi/nc-resapi-pclusapi_clus_worker_create?branch=master) to start a worker thread and return **ERROR\_IO\_PENDING** immediately.
2.  Have the thread perform the necessary online or offline tasks.
3.  Periodically call [**ClusWorkerCheckTerminate**](/windows/previous-versions/ResApi/nc-resapi-pclusapiclusworkercheckterminate?branch=master) to see if the [**Terminate**](/windows/previous-versions/ResApi/nc-resapi-pterminate_routine?branch=master) entry point function has been called.
4.  Use the [**SetResourceStatus**](/windows/previous-versions/ResApi/nc-resapi-pset_resource_status_routine?branch=master) function pointer obtained from the [**Startup**](/windows/previous-versions/ResApi/nc-resapi-pstartup_routine?branch=master) entry point function to report status information to the [Resource Monitor](resource-monitor.md).

If the [resource](resources.md) does not transition within the time specified by the resource's [**PendingTimeout**](resources-pendingtimeout.md) property, the Resource Monitor calls the [**Terminate**](/windows/previous-versions/ResApi/nc-resapi-pterminate_routine?branch=master) entry point function.

## Example

See [Resource DLL Examples](https://msdn.microsoft.com/library/aa370474).

 

 




