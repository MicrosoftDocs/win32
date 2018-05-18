---
title: CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_IS\_CSV\_FILE control code
description: Queries whether a file is stored on a CSV that is accessible to all nodes in the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '552de342-159d-4f3a-bb59-0953f022dad2'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_TYPE_STORAGE_IS_CSV_FILE control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_STORAGE_IS_CSV_FILE
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_IS\_CSV\_FILE control code

Queries whether a file is stored on a cluster shared volume (CSV) that is accessible to all nodes in the cluster. Applications use this control code as a parameter to the [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](resourcetypecontrol.md) callback function.


```C++
ClusterResourceTypeControl( hCluster,                                  // cluster handle
                            lpszResTypeName,                           // resource type name
                            hHostNode,                                 // optional host node
                            CLUSCTL_RESOURCE_TYPE_STORAGE_IS_CSV_FILE, // this control code
                            lpInBuffer,                                // input buffer: path to file
                            cbInBufferSize,                            // input buffer size
                            NULL,                                      // lpOutBuffer not used
                            0,                                         // cbOutBufferSize not used
                            NULL );                                    // lpcbBytesReturned not used
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) or [**ResourceTypeControl**](resourcetypecontrol.md).

<dl> <dt>

*lpInBuffer* \[in\]
</dt> <dd>

Pointer to null-terminated Unicode string containing the path to a file.

</dd> <dt>

*nInBufferSize* \[in\]
</dt> <dd>

Number of bytes in the buffer pointed to by *lpInBuffer*.

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The specified file is on a CSV.

</dd> <dt>

**ERROR\_CLUSTER\_NOT\_SHARED\_VOLUME**
</dt> <dd>

5945 (0x1739)

The specified file is not on a CSV.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed.

</dd> </dl>

## Remarks

The 32 bits of CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_IS\_CSV\_FILE (0x01000229) are defined as follows.



| Component                 | Bit location     | Value                                                |
|---------------------------|------------------|------------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>          |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>               |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>            |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                            |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_STORAGE\_IS\_CSV\_FILE** (0x229)<br/> |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>              |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/>      |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Type Control Codes](external-resource-type-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> <dt>

[*ResourceControl*](resourcecontrol.md)
</dt> </dl>

 

 





