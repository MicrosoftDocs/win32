---
title: CLUSCTL\_RESOURCE\_UPGRADE\_COMPLETED control code
description: Used by the Cluster service to notify a resource DLL that a rolling upgrade of the operating system on a cluster is complete.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'A30F9CBE-83CE-4207-A9A5-7E218A591357'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_UPGRADE_COMPLETED control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_UPGRADE_COMPLETED
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_UPGRADE\_COMPLETED control code

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that a rolling upgrade of the operating system on a cluster is complete. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](resourcecontrol.md) parameter. Because the control code is internal, applications cannot use it in a control code function.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_UPGRADE\_COMPLETED (0x014020EE) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                         |
|----------------|--------------|---------------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>                   |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                        |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>                             |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                     |
| Type bit       | 20           | Internal (0x1)<br/>                                     |
| Operation code | 0–23         | **CLCTL\_RESOURCE\_UPGRADE\_COMPLETED** (0x4020EE)<br/> |
| Access code    | 0–1          | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                      |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Internal Resource Control Codes](internal-resource-control-codes.md)
</dt> <dt>

[Control Codes](about-control-codes.md)
</dt> <dt>

[**ClusterUpgradeFunctionalLevel**](clusterupgradefunctionallevel.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_PREPARE\_UPGRADE](clusctl-resource-prepare-upgrade.md)
</dt> </dl>

 

 





