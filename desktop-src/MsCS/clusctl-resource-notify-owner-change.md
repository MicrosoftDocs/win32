---
title: CLUSCTL\_RESOURCE\_NOTIFY\_OWNER\_CHANGE control code
description: Used by the Cluster service to notify a resource DLL that a node is TBD. Resource DLLs receive this control code as a ResourceControl parameter. Because the control code is internal, applications cannot use it in a control code function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 60AB41C2-561D-4C1B-B894-403CB573F5A0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_NOTIFY_OWNER_CHANGE control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_NOTIFY_OWNER_CHANGE
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_NOTIFY\_OWNER\_CHANGE control code

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that a [node](nodes.md) is TBD. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_NOTIFY\_OWNER\_CHANGE (0x01502122) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                  |
|----------------|--------------|--------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>            |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                 |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>                      |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>              |
| Type bit       | 20           | Internal (0x1)<br/>                              |
| Operation code | 0 23         | **CLCTL\_NOTIFY\_OWNER\_CHANGE** (0x502122)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_WRITE** (0x2)<br/>               |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                    |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Internal Resource Control Codes](internal-resource-control-codes.md)
</dt> <dt>

[Control Codes](about-control-codes.md)
</dt> </dl>

 

 





