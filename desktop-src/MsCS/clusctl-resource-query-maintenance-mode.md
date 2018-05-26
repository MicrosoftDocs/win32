---
title: CLUSCTL\_RESOURCE\_QUERY\_MAINTENANCE\_MODE control code
description: Queries the maintenance mode state of the specified disk resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ceaaf124-bc66-4e5b-b5c3-2cae7f7c5a14
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_QUERY_MAINTENANCE_MODE control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_QUERY_MAINTENANCE_MODE
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_QUERY\_MAINTENANCE\_MODE control code

Queries the [*maintenance mode*](m-gly.md#-mscs-maintenance-mode-gly) state of the specified disk resource. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) function.


```C++
ClusterResourceControl( hResource,                               // resource handle
                        hHostNode,                               // host node
                        CLUSCTL_RESOURCE_QUERY_MAINTENANCE_MODE, // this control code
                        NULL,                                    // not used
                        0,                                       // not used
                        lpOutBuffer,                             // output buffer: string
                        cbOutBufferSize,                         // allocated buffer size (bytes)
                        lpcbBytesReturned );                     // size of returned data (bytes)
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [**CLUS\_MAINTENANCE\_MODE\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_maintenance_mode_info?branch=master) structure containing the current maintenance mode state of the disk resource.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The disk resource DLL supports maintenance mode and the function request was completed successfully.

</dd> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

The disk resource DLL does not support maintenance mode.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

Output buffer size is too small to return the requested data.

</dd> <dt>

**ERROR\_INVALID\_STATE**
</dt> <dd>

1369 (0x559)

The disk resource is offline.

</dd> <dt>

**ERROR\_HOST\_NODE\_NOT\_RESOURCE\_OWNER**
</dt> <dd>

5015 (0x1397)

A disk resource not owned by the hosting node cannot be queried for maintenance mode status.

</dd> <dt>

**ERROR\_CLUSTER\_INVALID\_REQUEST**
</dt> <dd>

5048 (0x13B8)

A quorum resource cannot be queried for maintenance mode status.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

Only disk resources support maintenance mode.

A resource must be online and not identified as the quorum resource in order to be placed in maintenance mode.

The calling application must direct the maintenance mode resource control codes to the node hosting the resource.

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_QUERY\_MAINTENANCE\_MODE (0x010001e1) as follows:



| Component                 | Bit location     | Value                                                  |
|---------------------------|------------------|--------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>            |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                 |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                  |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>              |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                              |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_QUERY\_MAINTENANCE\_MODE** (0x1e1)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 Datacenter with SP1, Windows Server 2008 Enterprise with SP1<br/> |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl>        |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[Maintaining Physical Disk Resources](maintaining-physical-disk-resources.md)
</dt> <dt>

[**CLUS\_MAINTENANCE\_MODE\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_maintenance_mode_info?branch=master)
</dt> <dt>

[CLUSCTL\_RESOURCE\_SET\_MAINTENANCE\_MODE](clusctl-resource-set-maintenance-mode.md)
</dt> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> </dl>

 

 





