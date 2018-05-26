---
title: CLUSCTL\_RESOURCE\_REMOVE\_OWNER control code
description: Used by the Cluster service to notify a resource DLL that a node is being removed from the list of possible owner nodes for a resource managed by the DLL.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: db2d179f-7bf7-48d8-83c8-fc38e6935250
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_REMOVE_OWNER control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_REMOVE_OWNER
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_REMOVE\_OWNER control code

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that a [node](nodes.md) is being removed from the list of [*possible owner*](p-gly.md#-wolf-possible-owner-gly) nodes for a [resource](resources.md) managed by the DLL. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_REMOVE\_OWNER as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                          |
|----------------|--------------|------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>    |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>         |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>              |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>      |
| Type bit       | 20           | Internal (0x1)<br/>                      |
| Operation code | 0 23         | **CLCTL\_REMOVE\_OWNER** (0x50001e)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_WRITE** (0x2)<br/>       |



 

### Resource DLL Support

Optional. Support the CLUSCTL\_RESOURCE\_REMOVE\_OWNER control code if the resource needs to retrieve or update properties or perform other tasks in response to the removed node. Otherwise, return **ERROR\_INVALID\_FUNCTION** to let the [Resource Monitor](resource-monitor.md) process the control code.

For more information on the [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) entry point, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master)
</dt> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> </dl>

 

 





