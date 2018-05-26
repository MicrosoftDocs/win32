---
title: DiskReload
description: Reload the volume level information from the disk (for example, driveletters, volume guids), instead of applying the volume information from the DiskVolumeInfo property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ff4c5b45-c159-4a75-8051-e3566d20149e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DiskReload Failover Cluster , for Physical Disk private properties
- DiskReload Failover Cluster
topic_type:
- apiref
api_name:
- DiskReload
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DiskReload

If this property has a nonzero value, during the [*online*](o-gly.md#-wolf-online-gly) operation, the [*Physical Disk resource*](p-gly.md#-wolf-physical-disk-resource-gly) will reload the volume level information from the disk (for example, driveletters, volume guids), instead of applying the volume information from the [**DiskVolumeInfo**](diskvolumeinfo.md) property. The following table summarizes the attributes of the **DiskReload** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | **FALSE** (0)                             |
| Maximum   | **TRUE** (1)                              |
| Default   | **FALSE** (0)                             |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **DiskReload** can be set with the following example code.


```C++
DWORD          DiskReloadData = 1;
CLUSPROP_DWORD DiskReloadValue;

DiskReloadValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
DiskReloadValue.cbLength  = sizeof(DWORD);
DiskReloadValue.dw        = DiskReloadData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





