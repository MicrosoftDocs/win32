---
title: CLUSCTL\_CLUSTER\_GET\_SHARED\_VOLUME\_ID control code
description: Verifies that a path is on a CSV and returns the resource identifier of the CSV and the volume offset of the specific volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0e470934-f1c1-40b2-93b7-10a9b3de3032'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_CLUSTER_GET_SHARED_VOLUME_ID control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_GET_SHARED_VOLUME_ID
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_CLUSTER\_GET\_SHARED\_VOLUME\_ID control code

Verifies that a path is on a cluster shared volume (CSV) and returns the [resource identifier](resource-identifiers.md) of the CSV and the volume offset of the specific volume (partition). Applications use this control code as a parameter to the [**ClusterControl**](clustercontrol.md) function


```C++
ClusterControl( hCluster,                             // cluster handle
                hHostNode,                            // optional node handle
                CLUSCTL_CLUSTER_GET_SHARED_VOLUME_ID, // this control code
                lpInBuffer,                           // input buffer: Unicode path
                cbInBufferSize,                       // input buffer size (bytes)
                lpOutBuffer,                          // output buffer: Unicode string ResID:PartOffset
                cbOutBufferSize,                      // output buffer size (bytes)
                lpcbBytesReturned );                  // resulting data size (bytes)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md).

<dl> <dt>

*lpInBuffer* \[in\]
</dt> <dd>

Pointer to null-terminated Unicode string containing a path.

</dd> <dt>

*nInBufferSize* \[in\]
</dt> <dd>

Number of bytes in the buffer pointed to by *lpInBuffer*.

</dd> <dt>

*lpOutBuffer* \[out\]
</dt> <dd>

Pointer to an output buffer to receive the Unicode string containing the [resource identifier](resource-identifiers.md) of the CSV, a colon ':', and the offset (in decimal) of the volume (partition). For example "2936f4ed-f55d-4fa9-bec2-108469342c6a:129761280".

</dd> <dt>

*cbOutBufferSize* \[in\]
</dt> <dd>

The allocated size (in bytes) of the output buffer.

</dd> <dt>

*lpBytesReturned* \[out\]
</dt> <dd>

Returns the actual size (in bytes) of the data resulting from the operation.

</dd> </dl>

## Return value

[**ClusterResourceControl**](clusterresourcecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**ERROR\_CLUSTER\_NOT\_SHARED\_VOLUME**
</dt> <dd>

5945 (0x1739)

The specified path is not on a CSV.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed.

</dd> </dl>

## Remarks

The 32 bits of CLUSCTL\_CLUSTER\_GET\_SHARED\_VOLUME\_ID (0x07000291) are defined as follows.



| Component                 | Bit location     | Value                                                 |
|---------------------------|------------------|-------------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_CLUSTER** (0x7)<br/>            |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                 |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>             |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                             |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_GET\_SHARED\_VOLUME\_ID** (0x291)<br/> |
| Access code<br/>    | 0–1<br/>   | **CLUS\_NO\_MODIFY** (0x0)<br/>                 |



 

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
</dt> </dl>

 

 





