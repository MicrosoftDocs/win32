---
title: CLUSCTL\_CLUSTER\_GET\_FQDN control code
description: Retrieves the fully qualified domain name (FQDN) of a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ba8a9445-b955-481a-9c6c-7457fa38a746'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_CLUSTER_GET_FQDN control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_GET_FQDN
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_CLUSTER\_GET\_FQDN control code

Retrieves the fully qualified domain name (FQDN) of a [*cluster*](c-gly.md#-wolf-cluster-gly). Applications use this [control code](about-control-codes.md) as a [**ClusterControl**](clustercontrol.md) parameter.


```C++
ClusterControl( 
  hCluster,                               // cluster handle
  hHostNode,                              // optional node handle
  CLUSCTL_CLUSTER_GET_FQDN,               // this control code
  NULL,                                   // input buffer (not used)
  0,                                      // input buffer size (not used)
  lpOutBuffer,                            // output buffer: string
  cbOutBufferSize,                        // output buffer size (bytes)
  lpcbBytesReturned                       // resulting data size (bytes)
);
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterControl**](clustercontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a null-terminated Unicode string specifying the FQDN of the cluster.

</dd> </dl>

## Return value

[**ClusterControl**](clustercontrol.md) returns one of the following values.

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

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_CLUSTER\_GET\_FQDN as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                      |
|----------------|--------------|--------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_CLUSTER** (0x7)<br/> |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>     |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>      |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>  |
| Type bit       | 20           | External (0x0)<br/>                  |
| Operation code | 0–23         | **CLCTL\_GET\_FQDN** (0x3d)<br/>     |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)<br/>    |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Cluster Control Codes](cluster-control-codes.md)
</dt> <dt>

[**ClusterControl**](clustercontrol.md)
</dt> </dl>

 

 





