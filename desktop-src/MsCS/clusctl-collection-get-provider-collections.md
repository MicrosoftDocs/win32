---
title: CLUSCTL\_COLLECTION\_GET\_PROVIDER\_COLLECTIONS control code
description: Retrieves the collections in the collection that come from a provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '76222551-F27D-4354-8B4B-C9FA5EE55C22'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_COLLECTION_GET_PROVIDER_COLLECTIONS control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_COLLECTION_GET_PROVIDER_COLLECTIONS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_COLLECTION\_GET\_PROVIDER\_COLLECTIONS control code

Retrieves the collections in the collection that come from a provider.

Applications use this [control code](about-control-codes.md) as a [**ClusterGroupCollectionControl**](clustergroupcollectioncontrol.md) parameter.


```C++
ClusterGroupCollectionControl( 
  hCollection,                                  // collection handle
  hHostNode,                                    // optional node handle
  CLUSCTL_COLLECTION_GET_PROVIDER_COLLECTIONS,  // this control code
  NULL,                                         // input buffer (not used)
  0,                                            // input buffer size (not used)
  lpOutBuffer,                                  // output buffer: property list
  cbOutBufferSize,                              // output buffer size (bytes)
  lpcbBytesReturned                             // resulting data size (bytes)
);
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterGroupCollectionControl**](clustergroupcollectioncontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) containing the collections in the specified collection that come from a provider.

</dd> </dl>

## Return value

[**ClusterGroupCollectionControl**](clustergroupcollectioncontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

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

ClusAPI.h defines the 32 bits of CLUSCTL\_COLLECTION\_GET\_PROVIDER\_COLLECTIONS as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                      |
|----------------|--------------|------------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_GROUPSET** (0x7)                           |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                                |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                                 |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)                             |
| Type bit       | 20           | External (0x0)                                             |
| Operation code | 0–23         | **CLCTL\_COLLECTION\_GET\_PROVIDER\_COLLECTIONS** (0x2D7A) |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)                               |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Collection Control Codes](collection-control-codes-.md)
</dt> <dt>

[**ClusterGroupCollectionControl**](clustergroupcollectioncontrol.md)
</dt> </dl>

 

 





