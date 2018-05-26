---
title: CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX2 control code
description: Retrieves extended information about a storage class resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: FA742D78-D89D-472D-B5C9-6C8D95883CD1
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_STORAGE_GET_DISK_INFO_EX2 control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_STORAGE_GET_DISK_INFO_EX2
api_location:
- ClusAPI.h
- MSClus.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX2 control code

Retrieves extended information about a [*storage class resource*](s-gly.md#-wolf-storage-class-resource-gly).

Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) callback function.

This control code uses **CLUSPROP\_PARTITION\_INFO\_EX2** structures to provide more information than the [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX](clusctl-resource-storage-get-disk-info-ex.md) control code.


```C++
ClusterResourceControl( hResource,                                 // resource handle
                        hHostNode,                                 // optional host node
                        CLUSCTL_RESOURCE_STORAGE_GET_DISK_INFO_EX2, // this control code
                        NULL,                                      // not used
                        0,                                         // not used
                        lpOutBuffer,                               // output buffer: value list
                        cbOutBufferSize,                           // allocated buffer size (bytes)
                        lpcbBytesReturned );                       // size of output data (bytes)
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) or [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [value list](value-lists.md) that describes the storage class resource. The value list is made up of **CLUSPROP\_PARTITION\_INFO\_EX2** structures.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values:

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

Implementations of [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) can return the above values or the following value:

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Requests that the Resource Monitor perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX2 (0x010001F9) as follows.



| Component                 | Bit location     | Value                                                       |
|---------------------------|------------------|-------------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>                 |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                      |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                       |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                   |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                   |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_STORAGE\_GET\_DISK\_INFO\_EX2** (0x1F9)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                     |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h; </dt> <dt>MSClus.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[Control Codes](about-control-codes.md)
</dt> </dl>

 

 





