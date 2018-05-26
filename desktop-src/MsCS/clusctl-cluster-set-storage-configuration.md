---
title: CLUSCTL\_CLUSTER\_SET\_STORAGE\_CONFIGURATION control code
description: Updates a storage configuration for a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 428FF672-F46C-40FD-99DF-3C1DFD7BEB98
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_CLUSTER_SET_STORAGE_CONFIGURATION control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_SET_STORAGE_CONFIGURATION
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_CLUSTER\_SET\_STORAGE\_CONFIGURATION control code

Updates a storage configuration for a cluster. Applications use this [control code](about-control-codes.md) as a [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) parameter.


```C++
ClusterControl( 
  hCluster,                               // cluster handle
  hHostNode,                              // optional node handle
  CLUSCTL_CLUSTER_SET_STORAGE_CONFIGURATION,  // this control code
  lpInBuffer,                             // input buffer (not used)
  nOutBufferSize,                         // input buffer size (not used)
  lpOutBuffer,                            // output buffer: property list
  nOutBufferSize,                         // output buffer size (bytes)
  lpBytesReturned                         // resulting data size (bytes)
);
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

A pointer to a [property list](property-lists.md) that contains the new values for the storage configuration.

</dd> </dl>

## Return value

[**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) returns one of the following values.

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

ClusAPI.h defines the 32 bits of this control code (0x074002E2) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component                 | Bit location     | Value                                                        |
|---------------------------|------------------|--------------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_CLUSTER** (0x7)<br/>                   |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                       |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>                            |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                    |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                    |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_SET\_STORAGE\_CONFIGURATION** (0x4002E2)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                     |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Cluster Control Codes](cluster-control-codes.md)
</dt> <dt>

[**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master)
</dt> </dl>

 

 





