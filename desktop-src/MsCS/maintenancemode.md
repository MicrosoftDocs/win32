---
title: MaintenanceMode
description: Contains the maintenance mode of the Physical Disk resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: af592311-15e6-4ad9-b7bd-4ef62bfd761f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MaintenanceMode Failover Cluster , for Physical Disk private properties
- MaintenanceMode Failover Cluster
topic_type:
- apiref
api_name:
- MaintenanceMode
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MaintenanceMode

Contains the maintenance mode of the [*Physical Disk resource*](p-gly.md#-wolf-physical-disk-resource-gly). The following table summarizes the attributes of the **MaintenanceMode** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 0                                         |
| Maximum   | 3                                         |
| Default   | 0                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_PHYSDISK\_MAINTMODE**.

The **MaintenanceMode** property can be set to one of the following values enumerated by the [**MAINTENANCE\_MODE\_TYPE\_ENUM**](/windows/previous-versions/ClusAPI/ne-clusapi-_maintenance_mode_type_enum?branch=master) enumeration.



| Value                                          | Description                                                                                                                                                                                        |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0                                              | The physical disk resource is not in a maintenance mode.                                                                                                                                           |
| **MaintenanceModeTypeDisableIsAliveCheck** (1) | Indicates that the server is ignoring the result of the resource's health check.                                                                                                                   |
| **MaintenanceModeTypeOfflineResource** (2)     | Indicates that the server has internally performed the operations to bring the storage resource to the **ClusterResourceOffline** state without changing the client visible state of the resource. |
| **MaintenanceModeTypeUnclusterResource** (3)   | Indicates the server has released ownership of the storage resource.                                                                                                                               |



 

These enumeration values are defined in ClusAPI.h.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> <dt>

[**MAINTENANCE\_MODE\_TYPE\_ENUM**](/windows/previous-versions/ClusAPI/ne-clusapi-_maintenance_mode_type_enum?branch=master)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





