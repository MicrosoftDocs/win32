---
title: CLUSCTL\_NODE\_GET\_PRIVATE\_PROPERTIES control code
description: Retrieves the read/write private properties for a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b22f281d-d88d-41bb-ab49-e7168e6e9f95'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_NODE_GET_PRIVATE_PROPERTIES control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_NODE_GET_PRIVATE_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_NODE\_GET\_PRIVATE\_PROPERTIES control code

Retrieves the read/write [private properties](private-properties.md) for a [node](nodes.md). Applications use this [control code](about-control-codes.md) as a [**ClusterNodeControl**](clusternodecontrol.md) parameter.


```C++
ClusterNodeControl( 
  hNode,                                             // node handle
  hHostNode,                                         // optional host node
  CLUSCTL_NODE_GET_PRIVATE_PROPERTIES,               // this control code
  NULL,                                              // input buffer (not used)
  0,                                                 // input buffer size (not used)
  lpOutBuffer,                                       // output buffer: property list
  cbOutBufferSize,                                   // allocated buffer size (bytes)
  lpcbBytesReturned );                               // actual size of resulting data (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterNodeControl**](clusternodecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) containing the specified node's read/write node private properties.

</dd> </dl>

## Return value

[**ClusterNodeControl**](clusternodecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

By default, failover clusters do not define any private properties for nodes.

ClusAPI.h defines the 32 bits of CLUSCTL\_NODE\_GET\_PRIVATE\_PROPERTIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                      |
|----------------|--------------|--------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_NODE** (0x4)               |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                 |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)             |
| Type bit       | 20           | External (0x0)                             |
| Operation code | 0–23         | **CLCTL\_GET\_PRIVATE\_PROPERTIES** (0x81) |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)               |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Node Control Codes](node-control-codes.md)
</dt> <dt>

[**ClusterNodeControl**](clusternodecontrol.md)
</dt> </dl>

 

 





