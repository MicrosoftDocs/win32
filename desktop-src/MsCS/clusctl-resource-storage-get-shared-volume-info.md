---
title: CLUSCTL\_RESOURCE\_STORAGE\_GET\_SHARED\_VOLUME\_INFO control code
description: Retrieves information on the specified shared volume. Applications use this control code as a parameter to the ClusterResourceControl function, and resource DLLs receive the control code as a parameter to the ResourceControl callback function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cd16d307-e6e5-494f-9f2e-c9f67992a768
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_STORAGE_GET_SHARED_VOLUME_INFO control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_STORAGE_GET_SHARED_VOLUME_INFO
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_STORAGE\_GET\_SHARED\_VOLUME\_INFO control code

Retrieves information on the specified shared volume. Applications use this control code as a parameter to the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [*ResourceControl*](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) callback function.


```C++
ClusterResourceControl( hResource,                        // resource handle
                        hHostNode,                        // optional node handle
                        CLUSCTL_RESOURCE_STORAGE_GET_SHARED_VOLUME_INFO, 
                        NULL,                             // input buffer (not used)
                        0,                                // input buffer size (not used)
                        lpOutBuffer,                      // output buffer: value list
                        cbOutBufferSize,                  // output buffer size (bytes)
                        lpcbBytesReturned );              // resulting data size (bytes)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

Pointer to a [value list](value-lists.md) of [**CLUSPOP\_BINARY**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_binary?branch=master) structures. Each binary structure, in turn, contains a CLUS\_CSV\_VOLUME\_INFO structure describing each cluster shared volume associated with the designated resource.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values.

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

The 32 bits of CLUSCTL\_RESOURCE\_STORAGE\_GET\_SHARED\_VOLUME\_INFO (0x01000225) are defined as follows.



| Component                 | Bit location     | Value                                                            |
|---------------------------|------------------|------------------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>                      |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                           |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                            |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                        |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                        |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_STORAGE\_GET\_SHARED\_VOLUME\_INFO** (0x225)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                          |



 

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
</dt> </dl>

 

 





