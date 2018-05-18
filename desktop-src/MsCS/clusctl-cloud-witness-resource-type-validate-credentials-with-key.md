---
title: CLUSCTL\_CLOUD\_WITNESS\_RESOURCE\_TYPE\_VALIDATE\_CREDENTIALS\_WITH\_KEY control code
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'F7286058-6CA2-40DE-A2F6-DB82F98F13FE'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_CLOUD_WITNESS_RESOURCE_TYPE_VALIDATE_CREDENTIALS_WITH_KEY control code Failover Cluster"]
---

# CLUSCTL\_CLOUD\_WITNESS\_RESOURCE\_TYPE\_VALIDATE\_CREDENTIALS\_WITH\_KEY control code

TBD


```C++
ClusterResourceTypeControl( 
  hCluster,                  // cluster handle
  lpszResourceTypeName,      // resource type name
  hHostNode,                 // optional host node
  CLUSCTL_CLOUD_WITNESS_RESOURCE_TYPE_VALIDATE_CREDENTIALS_WITH_KEY,  // this control code
  lpInBuffer,                // input buffer
  nInBufferSize,             // input buffer size (not used)
  lpOutBuffer,               // output buffer
  cbOutBufferSize,           // allocated buffer size
  lpcbBytesReturned );       // size of returned data
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) or [**ResourceTypeControl**](resourcetypecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

TBD

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) returns TBD:

Implementations of [**ResourceTypeControl**](resourcetypecontrol.md) can return the above values or the following value:

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Requests that the Resource Monitor perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_CLOUD\_WITNESS\_RESOURCE\_TYPE\_VALIDATE\_CREDENTIALS\_WITH\_KEY (0x020020f1) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                                                           |
|----------------|--------------|-------------------------------------------------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/>                                               |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                                                          |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                                                           |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                                                       |
| Type bit       | 20           | External (0x0)<br/>                                                                       |
| Operation code | 0–23         | **CLCTL\_CLOUD\_WITNESS\_RESOURCE\_TYPE\_VALIDATE\_CREDENTIALS\_WITH\_KEY** (0x20F1)<br/> |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                                                         |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Type Control Codes](external-resource-type-control-codes.md)
</dt> <dt>

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md)
</dt> <dt>

[Control Codes](about-control-codes.md)
</dt> </dl>

 

 





