---
title: CLUSCTL\_RESOURCE\_GET\_STATE\_CHANGE\_TIME control code
description: Retrieves the time of last state change for a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'CCF30722-0159-412E-ACEF-8FF662ED5587'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_GET_STATE_CHANGE_TIME control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_STATE_CHANGE_TIME
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_GET\_STATE\_CHANGE\_TIME control code

Retrieves the time of last state change for a resource. Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](clusterresourcecontrol.md) parameter.


```C++
ClusterResourceControl( 
  hResource,                       // resource handle
  hHostNode,                       // optional node handle
  CLUSCTL_RESOURCE_GET_STATE_CHANGE_TIME,   // this control code
  lpInBuffer,                      // input buffer
  cbInBufferSize,                  // input buffer size (bytes)
  lpOutBuffer,                     // output buffer
  cbOutBufferSize,                 // output buffer size (bytes)
  lpcbBytesReturned );             // resulting data size (bytes)
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md) or [**ResourceControl**](resourcecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) that contains the retrieved time data.

</dd> </dl>

## Return value

[**ClusterResourceControl**](clusterresourcecontrol.md) returns one of the following values.

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

Implementations of [**ResourceControl**](resourcecontrol.md) can return the above values or the following value.

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Incorrect function. Requests that the Resource Monitor perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_STATE\_CHANGE\_TIME (0x01002D5C) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                       |
|----------------|--------------|-------------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>                 |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                      |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                       |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                   |
| Type bit       | 20           | External (0x0)<br/>                                   |
| Operation code | 0–23         | **CLCTL\_GET\_STATE\_CHANGE\_TIME** (0x00002D5D)<br/> |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                     |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[Control Codes](about-control-codes.md)
</dt> </dl>

 

 





