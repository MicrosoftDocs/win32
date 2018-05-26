---
title: CLUSCTL\_RESOURCE\_STORAGE\_SET\_DRIVELETTER control code
description: Modifies the drive letter associated with the designated storage-class resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b13e8664-6fe0-4a06-8859-fd9eea879d44
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_STORAGE_SET_DRIVELETTER control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_STORAGE_SET_DRIVELETTER
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_STORAGE\_SET\_DRIVELETTER control code

Modifies the drive letter associated with the designated storage-class resource. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) function.


```C++
ClusterResourceControl( hResource,                                // resource handle
                        hHostNode,                                // optional node handle
                        CLUSCTL_RESOURCE_STORAGE_SET_DRIVELETTER, // control code
                        lpInBuffer,                               // input buffer: drive letter
                        cbInBufferSize,                           // input buffer size
                        NULL,                                     // output buffer (not used)
                        0,                                        // output buffer size (not used)
                        NULL);                                    // returned data size (not used)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Pointer to a [**CLUS\_STORAGE\_SET\_DRIVELETTER**](/windows/previous-versions/ClusAPI/ns-clusapi-_clus_storage_set_driveletter?branch=master) structure specifying the drive letter.

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

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_STORAGE\_SET\_DRIVELETTER (0x014001ea) as follows.



| Component      | Bit location | Value                                           |
|----------------|--------------|-------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)                |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                     |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)                          |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)                  |
| Type bit       | 20           | External (0x0)                                  |
| Operation code | 0 23         | **CLCTL\_STORAGE\_SET\_DRIVELETTER** (0x4001ea) |
| Access code    | 0 1          | **CLUS\_ACCESS\_WRITE** (0x2)                   |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> </dl>

 

 





