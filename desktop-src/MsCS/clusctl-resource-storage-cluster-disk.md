---
title: CLUSCTL\_RESOURCE\_STORAGE\_CLUSTER\_DISK control code
description: TBD. Applications use this control code as a parameter to the ClusterResourceControl function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 80a156ad-babb-4067-ade7-d4596a45c21b
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_STORAGE_CLUSTER_DISK control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_STORAGE_CLUSTER_DISK
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_STORAGE\_CLUSTER\_DISK control code

\[The CLUSCTL\_RESOURCE\_STORAGE\_CLUSTER\_DISK control code is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

TBD. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) function.


```C++
ClusterResourceControl( hResource,                             // cluster handle
                        hHostNode,                             // optional node handle
                        CLUSCTL_RESOURCE_STORAGE_CLUSTER_DISK, // this control code
                        lpInBuffer,                            // input buffer: TBD
                        nInBufferSize,                         // input buffer size (bytes)
                        lpOutBuffer,                           // output buffer: TBD
                        cbOutBufferSize,                       // output buffer size (bytes)
                        lpcbBytesReturned );                   // resulting data size (bytes)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master).

<dl></dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

The operation was successful. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_STORAGE\_CLUSTER\_DISK (0x01c00212) as follows:



| Component                 | Bit location     | Value                                                    |
|---------------------------|------------------|----------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>              |
| Global bit<br/>     | 23<br/>    | **CLUS\_GLOBAL** (0x1)<br/>                        |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>                        |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_NETNAME\_SET\_PWD\_INFO** (0xc00212)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                 |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>       |
| End of client support<br/>    | None supported<br/>                                                       |
| End of server support<br/>    | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[Cluster Control Codes](cluster-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> </dl>

 

 





