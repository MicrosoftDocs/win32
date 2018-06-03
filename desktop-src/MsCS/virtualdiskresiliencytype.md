---
title: VirtualDiskResiliencyType
description: Specifies the resiliency type of the virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: F0A42CE9-06C1-4A92-8F5A-CC5F4EEDC1F6
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- VirtualDiskResiliencyType Failover Cluster
topic_type:
- apiref
api_name:
- VirtualDiskResiliencyType
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VirtualDiskResiliencyType

Specifies the resiliency type of the virtual disk.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | **SpResiliencyTypeUnknown** (0)           |
| Maximum   | **SpResiliencyTypeMax** (4)               |
| Default   | 0                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_STORAGESPACE\_RESILIENCYTYPE**.

This property can be set to one of the following values contained in the **SP\_RESILIENCY\_TYPE** enumeration.



| Name                        | Value | Description                                         |
|-----------------------------|-------|-----------------------------------------------------|
| **SpResiliencyTypeUnknown** | 0     | The resiliency type of the virtual disk is unknown. |
| **SpResiliencyTypeSimple**  | 1     | The virtual disk has a simple resiliency type.      |
| **SpResiliencyTypeMirror**  | 2     | The virtual disk has a mirror resiliency type.      |
| **SpResiliencyTypeParity**  | 3     | The virtual disk has a parity resiliency type.      |
| **SpResiliencyTypeMax**     | 4     | Maximum value.                                      |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> </dl>

 

 





