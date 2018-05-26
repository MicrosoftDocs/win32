---
title: CLUSCTL\_RESOURCE\_DISABLE\_SHARED\_VOLUME\_DIRECTIO control code
description: Disables higher performance I/O on the cluster shared volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9353135b-fbdc-4d75-92a6-eaad7c92ea28
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_DISABLE_SHARED_VOLUME_DIRECTIO control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_DISABLE_SHARED_VOLUME_DIRECTIO
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_DISABLE\_SHARED\_VOLUME\_DIRECTIO control code

Disables higher performance I/O on the cluster shared volume. Applications use this control code as a parameter to the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [*ResourceControl*](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) callback function.


```C++
ClusterResourceControl( hResource,               // resource handle
                        hHostNode,               // optional node handle
                        CLUSCTL_RESOURCE_DISABLE_SHARED_VOLUME_DIRECTIO, 
                        lpInBuffer,              // input buffer: CSV name
                        nInBufferSize,           // input buffer size (bytes)
                        lpOutBuffer,             // output buffer: CSV GUID path
                        cbOutBufferSize,         // output buffer size (bytes)
                        lpcbBytesReturned );     // resulting data size (bytes)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master).

<dl> <dt>

*lpInBuffer* \[in, optional\]
</dt> <dd>

Pointer to a null-terminated Unicode string containing the name of the shared volume. The name provided can be either the cluster-assigned friendly name or the volume GUID path of the form "\\\\?\\Volume{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}\\".

</dd> <dt>

*cbInBufferSize* \[in\]
</dt> <dd>

The allocated size (in bytes) of the input buffer.

</dd> <dt>

*lpOutBuffer* \[out, optional\]
</dt> <dd>

Pointer to an output buffer to receive a null-terminated Unicode string containing the volume GUID path. The buffer must be at least 102 bytes (51 characters).

</dd> <dt>

*cbOutBufferSize* \[in\]
</dt> <dd>

The allocated size (in bytes) of the output buffer.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

The resource is not a cluster shared volume.

</dd> <dt>

**ERROR\_INVALID\_PARAMETER**
</dt> <dd>

87 (0x57)

The resource is not a cluster shared volume.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**ERROR\_RESOURCE\_NOT\_ONLINE**
</dt> <dd>

5004 (0x138C)

The resource is not online on any cluster node.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

The 32 bits of CLUSCTL\_RESOURCE\_DISABLE\_SHARED\_VOLUME\_DIRECTIO (0x0140028e) are defined as follows.



| Component                 | Bit location     | Value                                                              |
|---------------------------|------------------|--------------------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>                        |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                             |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>                                  |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                          |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                          |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_DISABLE\_SHARED\_VOLUME\_DIRECTIO** (0x40028e)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                           |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/>      |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> <dt>

[*ResourceControl*](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master)
</dt> <dt>

[CLUSCTL\_RESOURCE\_ENABLE\_SHARED\_VOLUME\_DIRECTIO](clusctl-resource-enable-shared-volume-directio.md)
</dt> </dl>

 

 





