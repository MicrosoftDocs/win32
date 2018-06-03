---
title: CLUSCTL\_RESOURCE\_STORAGE\_GET\_DIRTY control code
description: Retrieves a list of dirty volumes on the disk resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b1a48154-21ed-4f0f-97e7-7d9fce358504
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_STORAGE_GET_DIRTY control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_STORAGE_GET_DIRTY
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_STORAGE\_GET\_DIRTY control code

Retrieves a list of dirty volumes on the disk resource. Applications use this control code as a parameter to the [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [*ResourceControl*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) callback function.


```C++
ClusterResourceControl( hResource,               // resource handle
                        hHostNode,               // optional node handle
                        CLUSCTL_RESOURCE_STORAGE_GET_DIRTY, 
                        NULL,                    // lpInBuffer - Not used
                        0,                       // nInBufferSize - not used
                        lpOutBuffer,             // output buffer: array of dirty volume numbers
                        cbOutBufferSize,         // output buffer size (bytes)
                        lpcbBytesReturned );     // resulting data size (bytes)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol).

<dl> <dt>

*lpOutBuffer* \[out\]
</dt> <dd>

Pointer to an output buffer to receive the array of **DWORD** values containing the volume numbers of the dirty volumes on this disk resource.

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

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) returns one of the following values.

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

The 32 bits of CLUSCTL\_RESOURCE\_STORAGE\_GET\_DIRTY (0x01000219) are defined as follows.



| Component                 | Bit location     | Value                                                      |
|---------------------------|------------------|------------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>                |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                     |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                      |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                  |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                  |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_STORAGE\_STORAGE\_GET\_DIRTY** (0x219)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                    |



 

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

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol)
</dt> <dt>

[*ResourceControl*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine)
</dt> </dl>

 

 





