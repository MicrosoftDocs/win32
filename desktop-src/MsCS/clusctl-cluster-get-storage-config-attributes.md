---
title: CLUSCTL\_CLUSTER\_GET\_STORAGE\_CONFIG\_ATTRIBUTES control code
description: Retrieves the storage configuration attributes for a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: BB4D7E65-147E-4B2F-A21F-CB59AEB0F895
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_CLUSTER_GET_STORAGE_CONFIG_ATTRIBUTES control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_GET_STORAGE_CONFIG_ATTRIBUTES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_CLUSTER\_GET\_STORAGE\_CONFIG\_ATTRIBUTES control code

Retrieves the storage configuration attributes for a cluster. Applications use this [control code](about-control-codes.md) as a [**ClusterControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustercontrol) parameter.


```C++
ClusterControl( 
  hCluster,                               // cluster handle
  hHostNode,                              // optional node handle
  CLUSCTL_CLUSTER_GET_STORAGE_CONFIG_ATTRIBUTES,  // this control code
  lpInBuffer,                             // input buffer (not used)
  nOutBufferSize,                         // input buffer size (not used)
  lpOutBuffer,                            // output buffer: property list
  nOutBufferSize,                         // output buffer size (bytes)
  lpBytesReturned                         // resulting data size (bytes)
);
```



## Parameters

For complete parameter descriptions, see [**ClusterControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustercontrol). The following control code function parameter is specific to the this control code.

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) that contains the specified cluster's storage configuration attributes.

</dd> </dl>

## Return value

When an application uses this control code as a parameter for [**ClusterControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustercontrol), **ClusterControl** returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. This value is returned if the *lpBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

More data is available. This value is returned if the output buffer pointed to by *lpOutBuffer* was not large enough to hold the data for the operation. The *lpBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, the operation failed. The value of *lpBytesReturned* is unreliable.

</dd> </dl>

## Remarks

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of this control code (0x070002E9) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                               |
|----------------|--------------|-----------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_CLUSTER** (0x7)                     |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                         |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                          |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)                      |
| Type bit       | 20           | External (0x0)                                      |
| Operation code | 0 23         | **CLCTL\_GET\_STORAGE\_CONFIG\_ATTRIBUTES** (0x2E9) |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)                        |



 

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

[**ClusterControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustercontrol)
</dt> </dl>

 

 





