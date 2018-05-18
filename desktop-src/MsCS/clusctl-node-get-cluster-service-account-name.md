---
title: CLUSCTL\_NODE\_GET\_CLUSTER\_SERVICE\_ACCOUNT\_NAME control code
description: Retrieves the user account name under which the cluster service is running on a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e4210af5-d11f-4c23-abdd-746d4b662cdb'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_NODE_GET_CLUSTER_SERVICE_ACCOUNT_NAME control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_NODE_GET_CLUSTER_SERVICE_ACCOUNT_NAME
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_NODE\_GET\_CLUSTER\_SERVICE\_ACCOUNT\_NAME control code

Retrieves the user account name under which the cluster service is running on a [node](nodes.md). Applications use this [control code](about-control-codes.md) as a [**ClusterNodeControl**](clusternodecontrol.md) parameter.


```C++
ClusterNodeControl( 
  hNode,                                             // node handle
  hHostNode,                                         // optional host node
  CLUSCTL_NODE_GET_CLUSTER_SERVICE_ACCOUNT_NAME,     // this control code
  NULL,                                              // input buffer (not used)
  0,                                                 // input buffer size (not used)
  lpOutBuffer,                                       // output buffer: string
  cbOutBufferSize,                                   // allocated buffer size (bytes)
  lpcbBytesReturned );                               // actual size of resulting data (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterNodeControl**](clusternodecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a null-terminated Unicode string containing the user account name.

</dd> </dl>

## Return value

[**ClusterNodeControl**](clusternodecontrol.md) returns one of the following values.

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

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_NODE\_GET\_CLUSTER\_SERVICE\_ACCOUNT\_NAME as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                             |
|----------------|--------------|-------------------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_NODE** (0x4)<br/>                           |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                            |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                             |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                         |
| Type bit       | 20           | External (0x0)<br/>                                         |
| Operation code | 0–23         | **CLCTL\_GET\_CLUSTER\_SERVICE\_ACCOUNT\_NAME** (0x41)<br/> |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                           |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Node Control Codes](node-control-codes.md)
</dt> <dt>

[**ClusterNodeControl**](clusternodecontrol.md)
</dt> <dt>

[Control Code Architecture](control-code-architecture.md)
</dt> </dl>

 

 





