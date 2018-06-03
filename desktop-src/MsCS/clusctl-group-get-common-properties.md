---
title: CLUSCTL\_GROUP\_GET\_COMMON\_PROPERTIES control code
description: Retrieves the read/write group common properties for a group. Applications use this control code as a ClusterGroupControl parameter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f00cd260-48aa-4e55-a2d6-079f82840da5
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_GROUP_GET_COMMON_PROPERTIES control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_GROUP_GET_COMMON_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_GROUP\_GET\_COMMON\_PROPERTIES control code

Retrieves the read/write [group common properties](group-common-properties.md) for a [group](groups.md). Applications use this [control code](about-control-codes.md) as a [**ClusterGroupControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupcontrol) parameter.


```C++
ClusterGroupControl( 
  hGroup,                               // group handle
  hHostNode,                            // optional node handle
  CLUSCTL_GROUP_GET_COMMON_PROPERTIES,  // this control code
  NULL,                                 // input buffer (not used)
  0,                                    // input buffer size (not used)
  lpOutBuffer,                          // output buffer: property list
  cbOutBufferSize,                      // output buffer size (bytes)
  lpcbBytesReturned                     // resulting data size (bytes)
);
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterGroupControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupcontrol).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) containing the specified group's read/write [group common properties](group-common-properties.md).

</dd> </dl>

## Return value

[**ClusterGroupControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupcontrol) returns one of the following values:

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

Do not use any group control codes in any resource DLL entry point function. Group control codes can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_GROUP\_GET\_COMMON\_PROPERTIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                |
|----------------|--------------|------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_GROUP** (0x3)<br/>             |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>               |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>            |
| Type bit       | 20           | External (0x0)<br/>                            |
| Operation code | 0 23         | **CLCTL\_GET\_COMMON\_PROPERTIES** (0x59)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>              |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ClusterGroupControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupcontrol)
</dt> </dl>

 

 





