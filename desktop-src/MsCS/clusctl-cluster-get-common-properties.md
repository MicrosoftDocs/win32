---
title: CLUSCTL\_CLUSTER\_GET\_COMMON\_PROPERTIES control code
description: Retrieves the read/write cluster common properties for a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8b4d68b5-01f5-438a-93d7-853f19bad1d4
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_CLUSTER_GET_COMMON_PROPERTIES control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_GET_COMMON_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_CLUSTER\_GET\_COMMON\_PROPERTIES control code

Retrieves the read/write cluster [common properties](common-properties.md) for a cluster. Applications use this [control code](about-control-codes.md) as a [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) parameter.


```C++
ClusterControl( 
  hCluster,                               // cluster handle
  hHostNode,                              // optional node handle
  CLUSCTL_CLUSTER_GET_COMMON_PROPERTIES,  // this control code
  NULL,                                   // input buffer (not used)
  0,                                      // input buffer size (not used)
  lpOutBuffer,                            // output buffer: property list
  cbOutBufferSize,                        // output buffer size (bytes)
  lpcbBytesReturned                       // resulting data size (bytes)
);
```



## Parameters

For complete parameter descriptions, see [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master). The following control code function parameter is specific to the CLUSCTL\_CLUSTER\_GET\_COMMON\_PROPERTIES control code.

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) containing the specified cluster's read/write cluster [common properties](cluster-common-properties.md).

</dd> </dl>

## Return value

When an application uses CLUSCTL\_CLUSTER\_GET\_COMMON\_PROPERTIES as a parameter for [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master), **ClusterControl** returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. This value is returned if the *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

More data is available. This value is returned if the output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_CLUSTER\_GET\_COMMON\_PROPERTIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                     |
|----------------|--------------|-------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_CLUSTER** (0x7)           |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)               |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)            |
| Type bit       | 20           | External (0x0)                            |
| Operation code | 0 23         | **CLCTL\_GET\_COMMON\_PROPERTIES** (0x59) |
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

 

 





