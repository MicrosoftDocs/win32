---
title: CLUSCTL\_RESOURCE\_CLUSTER\_VERSION\_CHANGED control code
description: Internal.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '799d148e-10ef-4bae-9bac-8389c92a032f'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_CLUSTER_VERSION_CHANGED control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_CLUSTER_VERSION_CHANGED
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_CLUSTER\_VERSION\_CHANGED control code

Internal. Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that the cluster version has changed. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](resourcecontrol.md) parameter. Because the control code is internal, applications cannot use it in a control code function.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_CLUSTER\_VERSION\_CHANGED as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                      |
|----------------|--------------|------------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>                |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                     |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>                          |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                  |
| Type bit       | 20           | Internal (0x1)<br/>                                  |
| Operation code | 0–23         | **CLCTL\_CLUSTER\_VERSION\_CHANGED** (0x50002e)<br/> |
| Access code    | 0–1          | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                   |



 

### Resource DLL Support

Optional. Support the CLUSCTL\_RESOURCE\_CLUSTER\_VERSION\_CHANGED control code if your resource DLL needs to perform operations in response to the version change (for an overview of the versioning process, see [Version Compatibility](version-compatibility.md)). The [Resource Monitor](resource-monitor.md) does not provide any default processing.

For more information on the [**ResourceControl**](resourcecontrol.md) entry point, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> <dt>

[**ResourceControl**](resourcecontrol.md)
</dt> </dl>

 

 





