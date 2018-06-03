---
title: CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE1 control code
description: An internal control code that indicates that the Cluster service is starting on one of the cluster nodes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3a66a48c-ddd3-464c-8254-bf842dd174b2
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_TYPE_STARTING_PHASE1 control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_STARTING_PHASE1
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE1 control code

An [internal control code](internal-control-codes.md) that indicates that the [Cluster service](cluster-service.md) is starting on one of the [*cluster*](https://www.bing.com/search?q=*cluster*) nodes. [Resource DLLs](resource-dlls.md) receive this [control code](about-control-codes.md) through the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point function, which is called once for every resource type supported by the DLL.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

The [Cluster API](cluster-api.md) will be unavailable to the node on which the Cluster service is starting until your DLL receives the [CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE2](clusctl-resource-type-starting-phase2.md) control code.

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE1 as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                             |
|----------------|--------------|---------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/> |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>            |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>                 |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>         |
| Type bit       | 20           | Internal (0x1)<br/>                         |
| Operation code | 0 23         | **CLCTL\_STARTING\_PHASE1** (0x500036)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>           |



 

### Resource DLL Support

Optional. Support the CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE1 control code if you have any tasks that must be performed while the Cluster service is starting on a node.

The Resource Monitor provides no default processing.

For more information on the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point, see [Implementing ResourceTypeControl](implementing-resourcetypecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**CLUS\_STARTING\_PARAMS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_starting_params)
</dt> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE2](clusctl-resource-type-starting-phase2.md)
</dt> <dt>

[**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine)
</dt> </dl>

 

 





