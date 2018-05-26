---
title: CLUSCTL\_RESOURCE\_SET\_NAME control code
description: Used by the Cluster service to notify a resource DLL that the name of a resource has been changed. Because the control code is internal, applications cannot use it in a control code function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 16f9da56-ec7b-4ac6-b7e4-4a65215d2fca
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_SET_NAME control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_SET_NAME
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_SET\_NAME control code

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that the name of a [resource](resources.md) has been changed. Because the [control code](about-control-codes.md) is internal, applications cannot use it in a control code function.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_SET\_NAME as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                       |
|----------------|--------------|---------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/> |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>      |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>           |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>   |
| Type bit       | 20           | Internal (0x1)<br/>                   |
| Operation code | 0 23         | **CLCTL\_SET\_NAME** (0x500026)<br/>  |
| Access code    | 0 1          | **CLUS\_ACCESS\_WRITE** (0x2)<br/>    |



 

### Resource DLL Support

None required. The resource name has already been changed in the [cluster database](cluster-database.md). Respond to the CLUSCTL\_RESOURCE\_SET\_NAME control code if you need to perform other tasks when the name of your resource changes.

For more information on the [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) entry point function, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master)
</dt> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> </dl>

 

 





