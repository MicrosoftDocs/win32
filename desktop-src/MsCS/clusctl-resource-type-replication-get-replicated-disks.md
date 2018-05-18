---
title: CLUSCTL\_RESOURCE\_TYPE\_REPLICATION\_GET\_REPLICATED\_DISKS control code
description: Retrieves the replicated disks in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7E3B3EA0-0058-4799-AC98-3DBC05807F80'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_TYPE_REPLICATION_GET_REPLICATED_DISKS control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_REPLICATION_GET_REPLICATED_DISKS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_TYPE\_REPLICATION\_GET\_REPLICATED\_DISKS control code

Retrieves the replicated disks in a cluster. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](resourcetypecontrol.md) callback function.


```C++
ClusterResourceTypeControl( 
  hCluster,                  // cluster handle
  lpszResourceTypeName,      // resource type name
  hHostNode,                 // optional host node
  CLUSCTL_RESOURCE_TYPE_REPLICATION_GET_REPLICATED_DISKS,  // this control code
  lpInBuffer,                // input buffer
  nInBufferSize,             // input buffer size (not used)
  lpOutBuffer,               // output buffer
  cbOutBufferSize,           // allocated buffer size
  lpcbBytesReturned );       // size of returned data
```



## Parameters

For complete parameter descriptions, see [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) or [**ResourceTypeControl**](resourcetypecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a value list that contains the [**SR\_RESOURCE\_TYPE\_REPLICATED\_DISKS\_RESULT**](sr-resource-type-replicated-disks-result.md) structure that represents the retrieved disks.

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful.

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

Implementations of [**ResourceTypeControl**](resourcetypecontrol.md) can return the above values or the following value:

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Requests that the Resource Monitor perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_REPLICATION\_GET\_REPLICATED\_DISKS (x02002155) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                                 |
|----------------|--------------|-----------------------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/>                     |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                                |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                                 |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                             |
| Type bit       | 20           | External (0x1)<br/>                                             |
| Operation code | 0–23         | **CLCTL\_REPLICATION\_GET\_REPLICATED\_DISKS** (x00002155)<br/> |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                               |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Type Control Codes](external-resource-type-control-codes.md)
</dt> <dt>

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md)
</dt> <dt>

[Control Codes](about-control-codes.md)
</dt> </dl>

 

 





