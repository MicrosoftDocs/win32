---
title: CLUSCTL\_RESOURCE\_GET\_LOADBAL\_PROCESS\_LIST control code
description: Retrieves the load balancing processor list.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6f0bba91-3992-475b-a681-0e511d64ebd2
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_GET_LOADBAL_PROCESS_LIST control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_LOADBAL_PROCESS_LIST
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_GET\_LOADBAL\_PROCESS\_LIST control code

Retrieves the load balancing processor list. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) function.


```C++
ClusterResourceControl( hResource,           // resource handle
  hHostNode,                                 // optional node handle
  CLUSCTL_RESOURCE_GET_LOADBAL_PROCESS_LIST, // this control code
  NULL,                                      // input buffer (not used)
  0,                                         // input buffer size (not used)
  lpOutBuffer,                               // output buffer list
  cbOutBufferSize,                           // output buffer size (bytes)
  lpcbBytesReturned );                       // resulting data size (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to the list of load balancing processors.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) returns one of the following values.

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

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_LOADBAL\_PROCESS\_LIST (0x010000c9) as follows.



| Component      | Bit location | Value                                         |
|----------------|--------------|-----------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)              |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                   |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                    |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)                |
| Type bit       | 20           | External (0x0)                                |
| Operation code | 0 23         | **CLCTL\_GET\_LOADBAL\_PROCESS\_LIST** (0xc9) |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)                  |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol)
</dt> </dl>

 

 





