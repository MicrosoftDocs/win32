---
title: CLUSCTL\_COLLECTION\_SET\_COMMON\_PROPERTIES control code
description: Updates the read/write common properties for a collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: B2C0D9C6-C26E-4A56-A15E-243ED6429C8E
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_COLLECTION_SET_COMMON_PROPERTIES control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_COLLECTION_SET_COMMON_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_COLLECTION\_SET\_COMMON\_PROPERTIES control code

Updates the read/write [common properties](common-properties.md) for a collection.

Applications use this [control code](about-control-codes.md) as a [**ClusterGroupCollectionControl**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_groupset_control) parameter.


```C++
ClusterGroupCollectionControl( 
  hCollection,                               // collection handle
  hHostNode,                                 // optional node handle
  CLUSCTL_COLLECTION_SET_COMMON_PROPERTIES,  // this control code
  lpInBuffer,                                // input buffer: property list
  cbInBufferSize,                            // input buffer size (bytes)
  NULL,                                      // output buffer (not used)
  0,                                         // output buffer size (not used)
  NULL );                                    // resulting data size (not used)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterGroupCollectionControl**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_groupset_control).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Pass a pointer to a [property list](property-lists.md) containing new values for one or more read/write properties for the collection.

</dd> </dl>

## Return value

[**ClusterGroupCollectionControl**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_groupset_control) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The property list is correctly formatted and contains valid data values.

</dd> <dt>

**ERROR\_INSUFFICIENT\_BUFFER**
</dt> <dd>

122 (0x7A)

The data area passed to a system call is too small. The actual size of the property list buffer is larger than the size specified in the *cbInBufferSize* parameter.

</dd> <dt>

**ERROR\_INVALID\_DATA**
</dt> <dd>

13 (0xD)

The data is invalid. The property list is either formatted incorrectly or contains invalid data, such as an out-of-range value.

</dd> <dt>

**ERROR\_INVALID\_PARAMETER**
</dt> <dd>

87 (0x57)

The parameter is incorrect.

</dd> <dt>

**RPC\_X\_BAD\_STUB\_DATA**
</dt> <dd>

1783 (0x6F7)

The stub received bad data. The *lpInBuffer* parameter is **NULL**.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed.

</dd> </dl>

## Remarks

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_COLLECTION\_SET\_COMMON\_PROPERTIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component                 | Bit location     | Value                                                    |
|---------------------------|------------------|----------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_GROUPSET** (0x7)<br/>              |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                   |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>                        |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_SET\_COMMON\_PROPERTIES** (0x40005e)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                 |



 

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

[**ClusterGroupCollectionControl**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_groupset_control)
</dt> </dl>

 

 





