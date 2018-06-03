---
title: CLUSCTL\_RESOURCE\_LEAVING\_GROUP control code
description: Tells a resource when it is leaving a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 95098d33-998f-426b-8a47-b00cd3c87ecb
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_LEAVING_GROUP control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_LEAVING_GROUP
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_LEAVING\_GROUP control code

Tells a resource when it is leaving a group. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) parameter. Because the control code is internal, applications cannot use it in a control code function.


```C++
ClusterResourceControl( 
  hResource,                      // resource handle
  hHostNode,                      // optional host node
  CLUSCTL_RESOURCE_LEAVING_GROUP, // this control code
  lpInBuffer,                     // input buffer: group name
  cbInBufferSize,                 // input buffer size (bytes)
  NULL,                           // output buffer (not used)
  0,                              // allocated buffer size (not used)
  lpcbBytesReturned );            // actual size of resulting data (not used)
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) or [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

contains the name of the group this resource is attempting to leave.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

The operation completed successfully.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, the operation failed.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_LEAVING\_GROUP (0x01500056) as follows.



| Component      | Bit location | Value                                |
|----------------|--------------|--------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)     |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)          |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)               |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)       |
| Type bit       | 20           | Internal (0x1)                       |
| Operation code | 0 23         | **CLCTL\_LEAVING\_GROUP** (0x500056) |
| Access code    | 0 1          | **CLUS\_ACCESS\_WRITE** (0x2)        |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Internal Resource Control Codes](internal-resource-control-codes.md)
</dt> <dt>

[**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine)
</dt> </dl>

 

 





