---
title: CLUSCTL\_COLLECTION\_GET\_COMMON\_PROPERTIES control code
description: Retrieves the read/write properties for a collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: CC8D848F-645B-4B26-8E70-DED95F25681B
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_COLLECTION_GET_COMMON_PROPERTIES control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_COLLECTION_GET_COMMON_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_COLLECTION\_GET\_COMMON\_PROPERTIES control code

Retrieves the read/write properties for a collection.

Applications use this [control code](about-control-codes.md) as a [**ClusterGroupCollectionControl**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_groupset_control?branch=master) parameter.


```C++
ClusterGroupCollectionControl( 
  hCollection,                               // collection handle
  hHostNode,                                 // optional node handle
  CLUSCTL_COLLECTION_GET_COMMON_PROPERTIES,  // this control code
  NULL,                                      // input buffer (not used)
  0,                                         // input buffer size (not used)
  lpOutBuffer,                               // output buffer: property list
  cbOutBufferSize,                           // output buffer size (bytes)
  lpcbBytesReturned                          // resulting data size (bytes)
);
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterGroupCollectionControl**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_groupset_control?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) containing the specified collection's read/write properties.

</dd> </dl>

## Return value

[**ClusterGroupCollectionControl**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_groupset_control?branch=master) returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

The operation was successful. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_COLLECTION\_GET\_COMMON\_PROPERTIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                     |
|----------------|--------------|-------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_GROUPSET** (0x7)          |
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
| Minimum supported server<br/> | Windows Server 2016<br/>                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Collection Control Codes](collection-control-codes-.md)
</dt> <dt>

[**ClusterGroupCollectionControl**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_groupset_control?branch=master)
</dt> </dl>

 

 





