---
title: CLUSCTL\_NODE\_INTRODUCE\_GEM\_REPAIR\_DELAY control code
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'F202CC42-5E49-4BA2-8A00-A5AB24E66F62'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_NODE_INTRODUCE_GEM_REPAIR_DELAY control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_NODE_INTRODUCE_GEM_REPAIR_DELAY
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_NODE\_INTRODUCE\_GEM\_REPAIR\_DELAY control code

TBD. Applications use this [control code](about-control-codes.md) as a [**ClusterNodeControl**](clusternodecontrol.md) parameter.


```C++
ClusterNodeControl(
  hNode,               // node handle
  hHostNode,           // optional host node
  CLUSCTL_NODE_INTRODUCE_GEM_REPAIR_DELAY,  // this control code
  lpInBuffer,          // input buffer
  nInBufferSize,       // input buffer size
  lpOutBuffer,         // output buffer: string
  cbOutBufferSize,     // allocated buffer size (bytes)
  lpcbBytesReturned ); // resulting data size (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterNodeControl**](clusternodecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

A pointer to an output buffer that receives the data for the operation, or **NULL**.

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

More data is available. The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_NODE\_INTRODUCE\_GEM\_REPAIR\_DELAY (0x040002C5) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                       |
|----------------|--------------|-------------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_NODE** (0x4)<br/>                     |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                      |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                       |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                   |
| Type bit       | 20           | External (0x0)<br/>                                   |
| Operation code | 0–23         | **CLCTL\_INTRODUCE\_GEM\_REPAIR\_DELAY** (0x2C5)<br/> |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                     |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                    |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Node Control Codes](node-control-codes.md)
</dt> <dt>

[**ClusterNodeControl**](clusternodecontrol.md)
</dt> </dl>

 

 





