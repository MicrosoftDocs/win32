---
title: CLUSCTL\_RESOURCE\_GET\_OPERATION\_CONTEXT control code
description: Used by the Cluster service to notify a resource DLL that an operation context is being retrieved.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'BCB58D8A-5FF6-46BD-8144-919C6DB44593'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_GET_OPERATION_CONTEXT control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_OPERATION_CONTEXT
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_GET\_OPERATION\_CONTEXT control code

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that an operation context is being retrieved.

Resource DLLs receive this [control code](about-control-codes.md) as a parameter to the [**ResourceControl**](resourcecontrol.md) callback function. Because the control code is internal, applications cannot use it in a control code function.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_OPERATION\_CONTEXT (0x011020E9) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component                 | Bit location     | Value                                                    |
|---------------------------|------------------|----------------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>              |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                   |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>                        |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                |
| Type bit<br/>       | 20<br/>    | Internal (0x1)<br/>                                |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_GET\_OPERATION\_CONTEXT** (0x1020E9)<br/> |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                 |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Internal Resource Control Codes](internal-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> </dl>

 

 





