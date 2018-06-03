---
title: SkipChkdsk
description: Determines whether the operating system runs chkdsk on a physical disk before attempting to mount the disk. The following table summarizes the attributes of the SkipChkdsk property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ec711e63-2c94-4afe-ab34-52dec9b320a6
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- SkipChkdsk Failover Cluster ,for physical disks
- SkipChkdsk Failover Cluster
topic_type:
- apiref
api_name:
- SkipChkdsk
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SkipChkdsk

\[The **SkipChkdsk** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use the [**DiskRunChkDsk**](diskrunchkdsk.md) property.\]

Determines whether the operating system runs chkdsk on a physical disk before attempting to mount the disk. The following table summarizes the attributes of the **SkipChkdsk** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | **FALSE** (run Chkdsk)                    |
| Maximum   | **TRUE** (skip Chkdsk)                    |
| Default   | **FALSE**                                 |



 

## Remarks

Setting **SkipChkdsk** to **TRUE** causes the operating system to mount the disk without running chkdsk. With **SkipChkdsk** set to **FALSE** (the default), the operating system runs chkdsk first and, if errors are found, takes action based on the [**ConditionalMount**](physical-disks-conditionalmount.md) property. The following table summarizes the interaction between **SkipChkdsk** and **ConditionalMount**.



| **SkipChkdsk** value | [**ConditionalMount**](physical-disks-conditionalmount.md) value | Chkdsk runs? | Disk mounted?                                 |
|----------------------|-------------------------------------------------------------------|--------------|-----------------------------------------------|
| **FALSE**            | **TRUE**                                                          | yes          | If chkdsk reports errors, no. Otherwise, yes. |
| **FALSE**            | **FALSE**                                                         | yes          | yes                                           |
| **TRUE**             | **TRUE**                                                          | no           | yes                                           |
| **TRUE**             | **FALSE**                                                         | no           | yes                                           |



 

Forcing a disk to mount despite errors can result in loss of data. Use caution when changing these properties.

## Examples

The property value portion of a [property list](property-lists.md) entry for **SkipChkdsk** can be set with the following example code.


```C++
DWORD          SkipChkdskData = FALSE;
CLUSPROP_DWORD SkipChkdskValue;

SkipChkdskValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
SkipChkdskValue.cbLength  = sizeof(DWORD);
SkipChkdskValue.dw        = SkipChkdskData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> <dt>

[**ConditionalMount**](physical-disks-conditionalmount.md)
</dt> </dl>

 

 





