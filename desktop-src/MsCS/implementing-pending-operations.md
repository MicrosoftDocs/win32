---
title: Implementing Pending Operations
description: If your Online or Offline entry point functions require more than 300 milliseconds, it is recommended that you use a worker thread to perform the operation asynchronously.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0934f698-8de4-489d-b2e7-0781c0a9a89f'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["entry point functions Failover Cluster ,implementing pending operations"]
---

# Implementing Pending Operations

If your [**Online**](online.md) or [**Offline**](offline.md) entry point functions require more than 300 milliseconds, it is recommended that you use a worker thread to perform the operation asynchronously.

The following steps are all required:

**To Implement a Pending Operation**

1.  In your [**Online**](online.md) or [**Offline**](offline.md) entry point function, call [**ClusWorkerCreate**](clusworkercreate.md) to start a worker thread and return **ERROR\_IO\_PENDING** immediately.
2.  Have the thread perform the necessary online or offline tasks.
3.  Periodically call [**ClusWorkerCheckTerminate**](clusworkercheckterminate.md) to see if the [**Terminate**](terminate.md) entry point function has been called.
4.  Use the [**SetResourceStatus**](setresourcestatus.md) function pointer obtained from the [**Startup**](startup.md) entry point function to report status information to the [Resource Monitor](resource-monitor.md).

If the [resource](resources.md) does not transition within the time specified by the resource's [**PendingTimeout**](resources-pendingtimeout.md) property, the Resource Monitor calls the [**Terminate**](terminate.md) entry point function.

## Example

See [Resource DLL Examples](https://msdn.microsoft.com/library/aa370474).

 

 




