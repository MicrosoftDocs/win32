---
title: CLUSCTL\_GROUP\_GET\_PROVIDER\_COLLECTIONS control code
description: Retrieves the collections that come from providers by specifying a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: C51FDDBC-5E32-4950-9A1E-64843F184172
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_GROUP_GET_PROVIDER_COLLECTIONS control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_GROUP_GET_PROVIDER_COLLECTIONS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_GROUP\_GET\_PROVIDER\_COLLECTIONS control code

Retrieves the collections that come from providers by specifying a group.

Applications use this [control code](about-control-codes.md) as a [**ClusterGroupCollectionControl**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_groupset_control?branch=master) parameter.


```C++
ClusterGroupCollectionControl( 
  hGroup,                                 // group handle
  hHostNode,                              // optional node handle
  CLUSCTL_GROUP_GET_PROVIDER_COLLECTIONS, // this control code
  NULL,                                   // input buffer (not used)
  0,                                      // input buffer size (not used)
  lpOutBuffer,                            // output buffer: property list
  cbOutBufferSize,                        // output buffer size (bytes)
  lpcbBytesReturned                       // resulting data size (bytes)
);
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterGroupCollectionControl**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_groupset_control?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) containing the collections in the that come from a provider.

</dd> </dl>

## Return value

[**ClusterGroupCollectionControl**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_groupset_control?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

The operation was successful. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

More data is available. This value is returned if the output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation was not successful. If the operation required an output buffer, the value specified by *lpBytesReturned* (if not **NULL** on input) is unreliable.

</dd> </dl>

## Remarks

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_GROUP\_GET\_PROVIDER\_COLLECTIONS as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                 |
|----------------|--------------|-------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_COLLECTION** (0x7)                    |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                           |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                            |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)                        |
| Type bit       | 20           | External (0x0)                                        |
| Operation code | 0 23         | **CLCTL\_GROUP\_GET\_PROVIDER\_COLLECTIONS** (0x2D7A) |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)                          |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Collection Control Codes](collection-control-codes-.md)
</dt> <dt>

[**ClusterGroupCollectionControl**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_groupset_control?branch=master)
</dt> </dl>

 

 





