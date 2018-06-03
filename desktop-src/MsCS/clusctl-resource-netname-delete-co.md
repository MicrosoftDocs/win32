---
title: CLUSCTL\_RESOURCE\_NETNAME\_DELETE\_CO control code
description: Deletes the security principal associated with a designated resource. Applications use this control code as a parameter to the ClusterResourceControl function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4ee6893b-928e-4fce-85d1-f51118ee7556
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_NETNAME_DELETE_CO control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_NETNAME_DELETE_CO
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_NETNAME\_DELETE\_CO control code

Deletes the security principal associated with a designated resource. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) function.


```C++
ClusterResourceControl( hResource,    // resource handle
  hHostNode,                          // optional node handle
  CLUSCTL_RESOURCE_NETNAME_DELETE_CO, // this control code
  lpInBuffer,                         // input buffer: GUID
  cbInBufferSize,                     // input buffer size (bytes)
  NULL,                               // output buffer (not used)
  0,                                  // output buffer size (not used)
  NULL );                             // resulting data size (not used)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Pointer to a null-terminated Unicode string that contains a GUID of a security principal object on a directory server.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_NETNAME\_DELETE\_CO (0x0100017e) as follows.



| Component      | Bit location | Value                                  |
|----------------|--------------|----------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)       |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)            |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)             |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)         |
| Type bit       | 20           | External (0x0)                         |
| Operation code | 0 23         | **CLCTL\_NETNAME\_DELETE\_CO** (0x17e) |
| Access code    | 0 1          | **CLUS\_ACCESS\_WRITE** (0x2)          |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol)
</dt> </dl>

 

 





