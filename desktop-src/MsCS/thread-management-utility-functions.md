---
title: Thread Management Utility Functions
description: The thread management utility functions manage worker threads for resource DLLs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 47436aab-a513-423b-8287-e467954e1dc1
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- thread management utility functions Failover Cluster
- cluster utility functions Failover Cluster ,thread management utility functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Thread Management Utility Functions

The thread management utility functions manage worker threads for [resource DLLs](resource-dlls.md).

## In this section

<dl> <dt>

[*ClusWorkerCheckTerminate*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pclusapiclusworkercheckterminate)
</dt> <dd>

Determines whether a worker thread should exit as soon as possible. The **PCLUSAPIClusWorkerCheckTerminate** type defines a pointer to this function.

</dd> <dt>

[*ClusWorkerCreate*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pclusapi_clus_worker_create)
</dt> <dd>

Creates a worker thread. The **PCLUSAPI\_CLUS\_WORKER\_CREATE** type defines a pointer to this function.

</dd> <dt>

[**ClusWorkersTerminate**](/previous-versions/windows/desktop/api/Resapi/nf-resapi-clusworkersterminate)
</dt> <dd>

Waits for multiple worker threads to terminate up to the specified timeout.

</dd> <dt>

[*ClusWorkerTerminate*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pclusapi_clus_worker_terminate)
</dt> <dd>

Terminates a worker thread. The **PCLUSAPI\_CLUS\_WORKER\_TERMINATE** type defines a pointer to this function.

</dd> <dt>

[**ClusWorkerTerminateEx**](/previous-versions/windows/desktop/api/Resapi/nf-resapi-clusworkerterminateex)
</dt> <dd>

Waits for a worker thread to terminate up to the specified timeout.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Utility Functions](cluster-utility-functions.md)
</dt> </dl>

 

 




