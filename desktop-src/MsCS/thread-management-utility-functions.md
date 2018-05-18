---
title: Thread Management Utility Functions
description: The thread management utility functions manage worker threads for resource DLLs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '47436aab-a513-423b-8287-e467954e1dc1'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["thread management utility functions Failover Cluster", "cluster utility functions Failover Cluster ,thread management utility functions"]
---

# Thread Management Utility Functions

The thread management utility functions manage worker threads for [resource DLLs](resource-dlls.md).

## In this section

<dl> <dt>

[*ClusWorkerCheckTerminate*](clusworkercheckterminate.md)
</dt> <dd>

Determines whether a worker thread should exit as soon as possible. The **PCLUSAPIClusWorkerCheckTerminate** type defines a pointer to this function.

</dd> <dt>

[*ClusWorkerCreate*](clusworkercreate.md)
</dt> <dd>

Creates a worker thread. The **PCLUSAPI\_CLUS\_WORKER\_CREATE** type defines a pointer to this function.

</dd> <dt>

[**ClusWorkersTerminate**](clusworkersterminate.md)
</dt> <dd>

Waits for multiple worker threads to terminate up to the specified timeout.

</dd> <dt>

[*ClusWorkerTerminate*](clusworkerterminate.md)
</dt> <dd>

Terminates a worker thread. The **PCLUSAPI\_CLUS\_WORKER\_TERMINATE** type defines a pointer to this function.

</dd> <dt>

[**ClusWorkerTerminateEx**](clusworkerterminateex.md)
</dt> <dd>

Waits for a worker thread to terminate up to the specified timeout.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Utility Functions](cluster-utility-functions.md)
</dt> </dl>

 

 




