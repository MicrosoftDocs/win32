---
title: CLUSCTL\_RESOURCE\_TYPE\_FIXUP\_ON\_UPGRADE control code
description: Internal.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 22235f19-c1d0-4211-a008-710622d5ea68
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_TYPE_FIXUP_ON_UPGRADE control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_FIXUP_ON_UPGRADE
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_TYPE\_FIXUP\_ON\_UPGRADE control code

[Internal](internal-control-codes.md). Indicates that a [node](nodes.md) in the [*cluster*](https://www.bing.com/search?q=*cluster*) has just completed an upgrade of the [Cluster service](cluster-service.md). [Resource DLLs](resource-dlls.md) receive this [control code](about-control-codes.md) through the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point function, which is called once for every resource type supported by the DLL.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_FIXUP\_ON\_UPGRADE as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                               |
|----------------|--------------|-----------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/>   |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>              |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>                   |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>           |
| Type bit       | 20           | Internal (0x1)<br/>                           |
| Operation code | 0 23         | **CLCTL\_FIXUP\_ON\_UPGRADE** (0x500032)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>             |



 

### Resource DLL Support

Optional. Support the CLUSCTL\_RESOURCE\_TYPE\_FIXUP ON UPGRADE control code if your resource type needs to make adjustments in response to the change.

For more information on the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point, see [Implementing ResourceTypeControl](implementing-resourcetypecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine)
</dt> <dt>

[**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol)
</dt> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_EVICT\_NODE](clusctl-resource-type-evict-node.md)
</dt> <dt>

[**EvictClusterNode**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_evict_cluster_node)
</dt> </dl>

 

 





