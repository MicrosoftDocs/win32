---
title: CLUSCTL\_CLUSTER\_GET\_GUM\_LOCK\_OWNER control code
description: Retrieves the name of the current Global Update Manager (GUM) lock owner for a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: F16664D3-8CC1-4D12-ACA7-D3F81D7A2CF9
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_CLUSTER_GET_GUM_LOCK_OWNER control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_GET_GUM_LOCK_OWNER
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_CLUSTER\_GET\_GUM\_LOCK\_OWNER control code

Retrieves the name of the current [*Global Update Manager*](g-gly.md#-wolf-global-update-manager-gly) (GUM) lock owner for a [*cluster*](c-gly.md#-wolf-cluster-gly). Applications use this [control code](about-control-codes.md) as a [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) parameter.


```C++
ClusterControl( 
  hCluster,                               // cluster handle
  hHostNode,                              // optional node handle
  CLUSCTL_CLUSTER_GET_GUM_LOCK_OWNER,     // this control code
  NULL,                                   // input buffer (not used)
  0,                                      // input buffer size (not used)
  lpOutBuffer,                            // output buffer: GUM ID and lock owner name
  cbOutBufferSize,                        // output buffer size (bytes)
  lpcbBytesReturned                       // resulting data size (bytes)
);
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

When this method returns, contains the current GUM identifier, followed by the current GUM lock owner name.

</dd> <dt>

*lpcbBytesReturned* 
</dt> <dd>

When this method returns, contains the combined size, in bytes, of a **DWORD** and the GUM lock owner name.

</dd> </dl>

## Return value

[**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

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

When assessing a lock situation, make sure that the GUM identifier is for this control code is the same as the GUM identifier retrieved in the [CLUSCTL\_NODE\_GET\_STUCK\_NODES](clusctl-node-get-stuck-nodes.md) (0x070002B9) control code. The GUM identifiers also need to be the same for a period before assuming that a lock has occurred.

The 32 bits of CLUSCTL\_CLUSTER\_GET\_GUM\_LOCK\_OWNER are defined as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                    |
|----------------|--------------|------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_CLUSTER** (0x7)          |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)              |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)               |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)           |
| Type bit       | 20           | External (0x0)                           |
| Operation code | 0 23         | **CLCTL\_GET\_GUM\_LOCK\_OWNER** (0x2b9) |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)             |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/>      |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[CLUSCTL\_NODE\_GET\_STUCK\_NODES](clusctl-node-get-stuck-nodes.md)
</dt> <dt>

[Cluster Control Codes](cluster-control-codes.md)
</dt> <dt>

[**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master)
</dt> </dl>

 

 





