---
title: CLUSCTL\_NODE\_GET\_COMMON\_PROPERTIES control code
description: Retrieves the read/write common properties for a node. Applications use this control code as a ClusterNodeControl parameter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5eec9b3b-7f6f-4e28-a0b1-1d5d7db2a9af
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_NODE_GET_COMMON_PROPERTIES control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_NODE_GET_COMMON_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_NODE\_GET\_COMMON\_PROPERTIES control code

Retrieves the read/write [common properties](common-properties.md) for a [node](nodes.md). Applications use this [control code](about-control-codes.md) as a [**ClusterNodeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternodecontrol?branch=master) parameter.


```C++
ClusterNodeControl( 
  hNode,                                             // node handle
  hHostNode,                                         // optional host node
  CLUSCTL_NODE_GET_COMMON_PROPERTIES,                // this control code
  NULL,                                              // input buffer (not used)
  0,                                                 // input buffer size (not used)
  lpOutBuffer,                                       // output buffer: property list
  cbOutBufferSize,                                   // allocated buffer size (bytes)
  lpcbBytesReturned );                               // actual size of resulting data (bytes)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterNodeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternodecontrol?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) containing the specified node's read/write [common node properties](node-common-properties.md).

</dd> </dl>

## Return value

[**ClusterNodeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternodecontrol?branch=master) returns one of the following values:

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

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_NODE\_GET\_COMMON\_PROPERTIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                |
|----------------|--------------|------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_NODE** (0x4)<br/>              |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>               |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>            |
| Type bit       | 20           | External (0x0)<br/>                            |
| Operation code | 0 23         | **CLCTL\_GET\_COMMON\_PROPERTIES** (0x59)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>              |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ClusterNodeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternodecontrol?branch=master)
</dt> </dl>

 

 





