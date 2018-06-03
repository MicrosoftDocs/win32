---
title: CLUSCTL\_RESOURCE\_EVICT\_NODE control code
description: Used by the Cluster service to notify a resource DLL that a node is being permanently removed from the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8be7828a-cda5-4e61-83b9-8ff8f52437ff
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_EVICT_NODE control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_EVICT_NODE
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_EVICT\_NODE control code

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that a [node](nodes.md) is being permanently removed from the [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly). Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) parameter. Because the control code is internal, applications cannot use it in a control code function.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_EVICT\_NODE as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                        |
|----------------|--------------|----------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>  |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>       |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>            |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>    |
| Type bit       | 20           | Internal (0x1)<br/>                    |
| Operation code | 0 23         | **CLCTL\_EVICT\_NODE** (0x50000e)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_WRITE** (0x2)<br/>     |



 

### Resource DLL Support

Optional. Support the CLUSCTL\_RESOURCE\_EVICT\_NODE control code if your resource stores node-localized or node-specific data. By handling this code, you can remove this data and perform any other necessary cleanup tasks. The Resource Monitor provides no default processing.

For more information on the [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) entry point function, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine)
</dt> <dt>

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol)
</dt> <dt>

[**EvictClusterNode**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_evict_cluster_node)
</dt> </dl>

 

 





