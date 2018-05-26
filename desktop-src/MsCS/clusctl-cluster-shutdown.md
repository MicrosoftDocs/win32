---
title: CLUSCTL\_CLUSTER\_SHUTDOWN control code
description: Instructs the server to inform every active node in the cluster to stop participating in the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ebf8820a-109e-47fe-94ed-4fb1377597d5
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_CLUSTER_SHUTDOWN control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_SHUTDOWN
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_CLUSTER\_SHUTDOWN control code

Instructs the server to inform every active node in the cluster to stop participating in the cluster. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) function.


```C++
ClusterControl( hCluster,                 // cluster handle
                hHostNode,                // optional node handle
                CLUSCTL_CLUSTER_SHUTDOWN, // this control code
                lpInBuffer,               // input buffer: 0
                nInBufferSize,            // input buffer size (bytes)
                lpOutBuffer,              // output buffer: NULL
                cbOutBufferSize,          // output buffer size (bytes)
                lpcbBytesReturned );      // returned data size (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

After successful completion of the method, no data should be written to the buffer that *lpOutBuffer* points to.

</dd> </dl>

## Return value

[**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successful. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

More data is available. The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_CLUSTER\_SHUTDOWN (0x0700004d) as follows.



| Component      | Bit location | Value                                 |
|----------------|--------------|---------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_CLUSTER** (0x7)       |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)           |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)            |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)        |
| Type bit       | 20           | External (0x0)                        |
| Operation code | 0 23         | **CLCTL\_CHECK\_VOTER\_EVICT** (0x45) |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)          |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Cluster Control Codes](cluster-control-codes.md)
</dt> <dt>

[**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master)
</dt> </dl>

 

 





