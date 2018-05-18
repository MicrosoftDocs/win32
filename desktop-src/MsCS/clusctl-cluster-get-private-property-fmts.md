---
title: CLUSCTL\_CLUSTER\_GET\_PRIVATE\_PROPERTY\_FMTS control code
description: The CLUSCTL\_CLUSTER\_GET\_PRIVATE\_PROPERTY\_FMTS \ 32;control code is not supported and fails with ERROR\_INVALID\_FUNCTION.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c92d8fc4-44e4-4026-9e67-58c4ad5cfaf0'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_CLUSTER_GET_PRIVATE_PROPERTY_FMTS control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_GET_PRIVATE_PROPERTY_FMTS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_CLUSTER\_GET\_PRIVATE\_PROPERTY\_FMTS control code

The CLUSCTL\_CLUSTER\_GET\_PRIVATE\_PROPERTY\_FMTS [control code](about-control-codes.md) is not supported and fails with **ERROR\_INVALID\_FUNCTION**.


```C++
ClusterControl( hCluster,                               // cluster handle
                hHostNode,                              // optional node handle
                CLUSCTL_CLUSTER_GET_PRIVATE_PROPERTY_FMTS, // this control code
                NULL,                                   // input buffer (not used)
                0,                                      // input buffer size (not used)
                NULL,                                   // output buffer: (not used)
                0,                                      // output buffer size (not used)
                lpcbBytesReturned );                    // resulting data size (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterControl**](clustercontrol.md).

<dl></dl>

## Return value

[**ClusterControl**](clustercontrol.md) returns **ERROR\_INVALID\_FUNCTION**.

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Incorrect function. The [CLUSCTL\_CLUSTER\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-cluster-get-private-property-fmts.md) control code is not supported.

</dd> </dl>

## Remarks

By default, failover clusters do not define any private cluster properties. CLUSCTL\_CLUSTER\_GET\_PRIVATE\_PROPERTY\_FMTS does not retrieve information about unknown properties.

ClusAPI.h defines the 32 bits of CLUSCTL\_CLUSTER\_GET\_PRIVATE\_PROPERTY\_FMTS as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component                 | Bit location     | Value                                                     |
|---------------------------|------------------|-----------------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_CLUSTER** (0x7)<br/>                |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                    |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                     |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                 |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                 |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_GET\_PRIVATE\_PROPERTY\_FMTS** (0x8d)<br/> |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                   |



 

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

 

 





