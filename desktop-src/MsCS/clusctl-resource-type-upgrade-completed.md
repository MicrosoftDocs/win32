---
title: CLUSCTL\_RESOURCE\_TYPE\_UPGRADE\_COMPLETED control code
description: Internal.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 11545278-86B8-4BEF-8FAB-07E4C85AE7CA
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_TYPE_UPGRADE_COMPLETED control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_UPGRADE_COMPLETED
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_TYPE\_UPGRADE\_COMPLETED control code

[Internal](internal-control-codes.md). Indicates that a [node](nodes.md) in the [*cluster*](c-gly.md#-wolf-cluster-gly) is preparing for an upgrade of the [Cluster service](cluster-service.md). [Resource DLLs](resource-dlls.md) receive this [control code](about-control-codes.md) through the [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) entry point function, which is called once for every resource type supported by the DLL.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of this control code (0x024020EE) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                         |
|----------------|--------------|---------------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/>             |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                        |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>                             |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                     |
| Type bit       | 20           | Internal (0x1)<br/>                                     |
| Operation code | 0 23         | **CLCTL\_RESOURCE\_UPGRADE\_COMPLETED** (0x4020EE)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                       |



 

### Resource DLL Support

Optional. For information about the [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) entry point, see [Implementing ResourceTypeControl](implementing-resourcetypecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master)
</dt> </dl>

 

 





