---
title: CLUSCTL\_RESOURCE\_SET\_CSV\_MAINTENANCE\_MODE control code
description: Enables or disables maintenance mode for the specified cluster shared volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '12c35048-660d-47d3-b35c-24eea5627ffb'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_SET_CSV_MAINTENANCE_MODE control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_SET_CSV_MAINTENANCE_MODE
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_SET\_CSV\_MAINTENANCE\_MODE control code

Enables or disables [*maintenance mode*](m-gly.md#-mscs-maintenance-mode-gly) for the specified cluster shared volume (CSV). Applications use this control code as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [*ResourceControl*](resourcecontrol.md) callback function.


```C++
ClusterResourceControl( hResource,               // resource handle
                        hHostNode,               // optional node handle
                        CLUSCTL_RESOURCE_SET_CSV_MAINTENANCE_MODE, 
                        lpInBuffer,              // input buffer: maintenence info
                        nInBufferSize,           // input buffer size (bytes)
                        NULL,                    // output buffer (not used)
                        0,                       // output buffer size (not used)
                        NULL );                  // resulting data size (not used)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Points to a [**CLUS\_CSV\_MAINTENANCE\_MODE\_INFO**](clus-csv-maintenance-mode-info.md) structure containing the maintenance mode. The **VolumeName** field must be set to a unique volume identifier. Set the **InMaintenance** field to **TRUE** to enable or **FALSE** to disable volume maintenance mode for the designated cluster shared volume.

</dd> </dl>

## Return value

[**ClusterResourceControl**](clusterresourcecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

The 32 bits of CLUSCTL\_RESOURCE\_SET\_CSV\_MAINTENANCE\_MODE (0x00400296) are defined as follows.



| Component                 | Bit location     | Value                                                        |
|---------------------------|------------------|--------------------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>                  |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                       |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>                            |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                    |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                    |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_SET\_CSV\_MAINTENANCE\_MODE** (0x400296)<br/> |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                     |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/>      |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> <dt>

[*ResourceControl*](resourcecontrol.md)
</dt> <dt>

[**CLUS\_CSV\_MAINTENANCE\_MODE\_INFO**](clus-csv-maintenance-mode-info.md)
</dt> </dl>

 

 





