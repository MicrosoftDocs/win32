---
title: CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE2 control code
description: An internal control code that indicates that a node in the cluster has just completed a startup of the Cluster service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5187e72c-2838-487b-a897-0b4f99f6f9df'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_TYPE_STARTING_PHASE2 control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_STARTING_PHASE2
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE2 control code

An [internal control code](internal-control-codes.md) that indicates that a node in the [*cluster*](c-gly.md#-wolf-cluster-gly) has just completed a startup of the [*Cluster service*](c-gly.md#-wolf-cluster-service-gly). [Resource DLLs](resource-dlls.md) receive this [control code](about-control-codes.md) through the [**ResourceTypeControl**](resourcetypecontrol.md) entry point function, which is called once for every [*resource type*](r-gly.md#-wolf-resource-type-gly) supported by the DLL.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

Once your DLL receives the CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE2 control code, the Cluster API is available to the node on which the Cluster service has started.

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE2 as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                             |
|----------------|--------------|---------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/> |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>            |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>                 |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>         |
| Type bit       | 20           | Internal (0x1)<br/>                         |
| Operation code | 0–23         | **CLCTL\_STARTING\_PHASE2** (0x50003a)<br/> |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)<br/>           |



 

### Resource DLL Support

Optional. Support the CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE2 control code if you have any tasks that must be performed after the Cluster service has started on the node. The Resource Monitor provides no default processing.

For more information on the [**ResourceTypeControl**](resourcetypecontrol.md) entry point, see [Implementing ResourceTypeControl](implementing-resourcetypecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**CLUS\_STARTING\_PARAMS**](clus-starting-params.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE1](clusctl-resource-type-starting-phase1.md)
</dt> <dt>

[**ResourceTypeControl**](resourcetypecontrol.md)
</dt> </dl>

 

 





