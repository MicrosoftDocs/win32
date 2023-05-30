---
description: The data types supported by VDS define function return values, function parameters, and structure members. Data types define the size and meaning of these elements.
ms.assetid: f17e8c7e-e3cb-49ca-9060-2299dda55770
title: VDS Data Types
ms.topic: article
ms.date: 05/31/2018
---

# VDS Data Types

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/windows-hardware/drivers/storage/windows-storage-management-api-portal).\]

The data types supported by VDS define function return values, function parameters, and structure members. Data types define the size and meaning of these elements.



| Data type                                                                                      | Description                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="VDS_OBJECT_ID"></span><span id="vds_object_id"></span>**VDS\_OBJECT\_ID**<br/> | VDS object ID. These values are not guaranteed to be unique across reboots. <br/> This type is declared in Vds.h (VdsHwPrv.h for hardware providers) as a GUID. <br/> |
| <span id="VDS_PATH_ID"></span><span id="vds_path_id"></span>**VDS\_PATH\_ID**<br/>       | VDS path ID for multipath I/O (MPIO). <br/> This type is declared in Vds.h (VdsHwPrv.h for hardware providers) as a UINT64.<br/>                                      |



 

 

