---
title: CLUSCTL\_RESOURCE\_JOINING\_GROUP control code
description: Tells a resource when it is joining a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 09f3248a-97a1-4f00-971f-1d2d4a373c88
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_JOINING_GROUP control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_JOINING_GROUP
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_JOINING\_GROUP control code

Tells a resource when it is joining a group. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.


```C++
ClusterResourceControl( 
  hResource,                                 // resource handle
  hHostNode,                                 // optional host node
  CLUSCTL_RESOURCE_FSWITNESS_SET_EPOCH_INFO, // this control code
  lpInBuffer,                                // input buffer: group name
  cbInBufferSize,                            // input buffer size (bytes)
  NULL,                                      // output buffer (not used)
  0,                                         // allocated buffer size (not used)
  lpcbBytesReturned );                       // actual size of resulting data (not used)
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) or [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

contains the name of the group this resource is attempting to join.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values.

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

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_JOINING\_GROUP (0x0150005a) as follows.



| Component      | Bit location | Value                                |
|----------------|--------------|--------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)     |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)          |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)               |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)       |
| Type bit       | 20           | Internal (0x1)                       |
| Operation code | 0 23         | **CLCTL\_JOINING\_GROUP** (0x50005a) |
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

[**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master)
</dt> </dl>

 

 





