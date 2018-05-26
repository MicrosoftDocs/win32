---
title: CLUSCTL\_CLUSTER\_GET\_CLUSDB\_TIMESTAMP control code
description: Retrieves a cluster database timestamp for a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2F0A7F5C-9A7C-4BB9-90EC-406862A129FF
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_CLUSTER_GET_CLUSDB_TIMESTAMP control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_GET_CLUSDB_TIMESTAMP
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_CLUSTER\_GET\_CLUSDB\_TIMESTAMP control code

Retrieves a cluster database timestamp for a cluster. Applications use this [control code](about-control-codes.md) as a [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) parameter.


```C++
ClusterControl( 
  hCluster,                                 // cluster handle
  hHostNode,                                // optional node handle
  CLUSCTL_CLUSTER_GET_CLUSDB_TIMESTAMP,     // this control code
  lpInBuffer,                               // input buffer
  nInBufferSize,                            // input buffer size
  lpOutBuffer,                              // output buffer: array of strings
  nOutBufferSize,                           // output buffer size
  lpBytesReturned                           // resulting data size
);
```



## Parameters

For complete parameter descriptions, see [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master). The following control code function parameter is specific to this control code.

<dl> <dt>

*hCluster* \[in\]
</dt> <dd>

A handle to the cluster that is identified in the cluster database timestamp.

</dd> <dt>

*hHostNode* \[in, optional\]
</dt> <dd>

A handle to the node that is to perform the operation. If **NULL**, the local node performs the operation.

</dd> <dt>

*lpInBuffer* \[in, optional\]
</dt> <dd>

A pointer to the input buffer that contains the data for the operation, or **NULL** if no information is needed.

</dd> <dt>

*nInBufferSize* \[in\]
</dt> <dd>

The allocated size of of the *lpInBuffer* parameter, in bytes.

</dd> <dt>

*lpOutBuffer* \[out, optional\]
</dt> <dd>

A pointer to the output buffer that receives the data retrieved by the operation, or **NULL** if no data will is retrieved.

</dd> <dt>

*nOutBufferSize* \[in\]
</dt> <dd>

The allocated size of of the *lpOutBuffer* parameter, in bytes.

</dd> <dt>

*lpBytesReturned* \[out, optional\]
</dt> <dd>

The actual size of the data retrieved by the operation, in bytes.

</dd> </dl>

## Return value

When an application uses CLUSCTL\_CLUSTER\_GET\_CLUSDB\_TIMESTAMP as a parameter for [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master), **ClusterControl** returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. This value is returned if the *lpBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

More data is available. This value is returned if the buffer for *lpOutBuffer* was not large enough to hold the data that was returned by the operation.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation was not successful. If the operation required an output buffer, the value specified by *lpBytesReturned* (if not NULL on input) is unreliable.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_CLUSTER\_GET\_CLUSDB\_TIMESTAMP (0x070002A9) as follows. For more information, see [Control Code Architecture](control-code-architecture.md).



| Component      | Bit location | Value                                     |
|----------------|--------------|-------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_CLUSTER** (0x7)           |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)               |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)            |
| Type bit       | 20           | External (0x0)                            |
| Operation code | 0 23         | **CLCTL\_GET\_CLUSDB\_TIMESTAMP** (0x2A9) |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)              |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Cluster Control Codes](cluster-control-codes.md)
</dt> <dt>

[**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master)
</dt> </dl>

 

 





