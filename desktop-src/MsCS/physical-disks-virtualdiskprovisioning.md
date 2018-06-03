---
title: VirtualDiskProvisioning
description: Specifies the provisioning type of the virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: FF4556AA-A251-4896-84E3-7901ED8B92E3
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- VirtualDiskProvisioning Failover Cluster
topic_type:
- apiref
api_name:
- VirtualDiskProvisioning
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VirtualDiskProvisioning

Specifies the provisioning type of the virtual disk.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | **SpProvisioningTypeUnknown** (0)         |
| Maximum   | **SpProvisioningTypeMax** (3)             |
| Default   | 0                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_STORAGESPACE\_PROVISIONING**.

This property can be set to one of the following values contained in the **SP\_PROVISIONING\_TYPE** enumeration. However, clustering only supports **SpProvisioningTypeFixed**.



| Name                          | Value | Description                                           |
|-------------------------------|-------|-------------------------------------------------------|
| **SpProvisioningTypeUnknown** | 0     | The provisioning type of the virtual disk is unknown. |
| **SpProvisioningTypeThin**    | 1     | The virtual disk contains thin provisioning.          |
| **SpProvisioningTypeFixed**   | 2     | The virtual disk contains fixed provisioning.         |
| **SpProvisioningTypeMax**     | 3     | TBD                                                   |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> </dl>

 

 





