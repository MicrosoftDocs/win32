---
title: CLUSCTL\_NODE\_GET\_STUCK\_NODES control code
description: Retrieves the bitmap that represents the set of nodes that the current Global Update Manager (GUM) lock owner is waiting for.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 329D7411-9953-4CAF-8040-5EADCF3DAE49
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_NODE_GET_STUCK_NODES control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_NODE_GET_STUCK_NODES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_NODE\_GET\_STUCK\_NODES control code

Retrieves the bitmap that represents the set of [nodes](nodes.md) that the current [*Global Update Manager*](g-gly.md#-wolf-global-update-manager-gly) (GUM) lock owner is waiting for. Applications use this [control code](about-control-codes.md) as a [**ClusterNodeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternodecontrol?branch=master) parameter.


```C++
ClusterNodeControl( 
  hNode,                        // node handle
  hHostNode,                    // optional host node
  CLUSCTL_NODE_GET_STUCK_NODES, // this control code
  NULL,                         // input buffer (not used)
  0,                            // input buffer size (not used)
  lpOutBuffer,                  // output buffer: GUM ID and stuck node bitmap
  cbOutBufferSize,              // allocated buffer size (bytes)
  lpcbBytesReturned );          // actual size of resulting data (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterNodeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternodecontrol?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

When this method returns, contains the current GUM identifier, followed by the bitmap of stuck nodes.

</dd> <dt>

*lpcbBytesReturned* 
</dt> <dd>

When this method returns, contains the combined size, in bytes, of a **DWORD** and an **int64**.

</dd> </dl>

## Return value

[**ClusterNodeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternodecontrol?branch=master) returns one of the following values.

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

When assessing a lock situation, make sure that the GUM identifier is for this control code is the same as the GUM identifier retrieved in the [CLUSCTL\_CLUSTER\_GET\_GUM\_LOCK\_OWNER](clusctl-cluster-get-gum-lock-owner.md) control code. The GUM identifiers also need to be the same for a period before assuming that a lock has occurred.

The 32 bits of CLUSCTL\_NODE\_GET\_STUCK\_NODES are defined as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                |
|----------------|--------------|--------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_NODE** (0x4)         |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)          |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)           |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)       |
| Type bit       | 20           | External (0x0)                       |
| Operation code | 0 23         | **CLCTL\_GET\_STUCK\_NODES** (0x2bd) |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)         |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/>      |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Node Control Codes](node-control-codes.md)
</dt> <dt>

[CLUSCTL\_CLUSTER\_GET\_GUM\_LOCK\_OWNER](clusctl-cluster-get-gum-lock-owner.md)
</dt> <dt>

[**ClusterNodeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternodecontrol?branch=master)
</dt> </dl>

 

 





