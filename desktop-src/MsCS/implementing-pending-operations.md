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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Pending Operations

If your [**Online**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-ponline_routine) or [**Offline**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-poffline_routine) entry point functions require more than 300 milliseconds, it is recommended that you use a worker thread to perform the operation asynchronously.

The following steps are all required:

**To Implement a Pending Operation**

1.  In your [**Online**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-ponline_routine) or [**Offline**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-poffline_routine) entry point function, call [**ClusWorkerCreate**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pclusapi_clus_worker_create) to start a worker thread and return **ERROR\_IO\_PENDING** immediately.
2.  Have the thread perform the necessary online or offline tasks.
3.  Periodically call [**ClusWorkerCheckTerminate**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pclusapiclusworkercheckterminate) to see if the [**Terminate**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pterminate_routine) entry point function has been called.
4.  Use the [**SetResourceStatus**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pset_resource_status_routine) function pointer obtained from the [**Startup**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pstartup_routine) entry point function to report status information to the [Resource Monitor](resource-monitor.md).

If the [resource](resources.md) does not transition within the time specified by the resource's [**PendingTimeout**](resources-pendingtimeout.md) property, the Resource Monitor calls the [**Terminate**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pterminate_routine) entry point function.

## Example

See [Resource DLL Examples](https://msdn.microsoft.com/library/aa370474).

 

 




