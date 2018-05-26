---
title: DiskRunChkDsk
description: Determines whether the operating system runs chkdsk on a physical disk before attempting to mount the disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3deb34b4-6dfd-4c4b-864f-c696dfa34d91
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DiskRunChkDsk Failover Cluster , for Physical Disk private properties
- DiskRunChkDsk Failover Cluster
topic_type:
- apiref
api_name:
- DiskRunChkDsk
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DiskRunChkDsk

Determines whether the operating system runs chkdsk on a physical disk before attempting to mount the disk. The following table summarizes the attributes of the **DiskRunChkDsk** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Status<br/>    | Optional<br/>                                  |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 6<br/>                                         |
| Default<br/>   | 0<br/>                                         |



 

The possible values for this property are:



| Value | Description                                                                                                                                                                                                                                                             |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x0   | Verify whether the dirty bit is set on the volume, and then perform a normal check on the file system. If the dirty bit is set, or if the normal check returns **STATUS\_FILE\_CORRUPT\_ERROR** or **STATUS\_DISK\_CORRUPT\_ERROR**, chkdsk is started in verbose mode. |
| 0x1   | Verify whether the dirty bit is set on the volume, and then perform a verbose check on the file system. If the dirty bit is set or if the verbose check returns **STATUS\_FILE\_CORRUPT\_ERROR**, chkdsk is started in normal mode.                                     |
| 0x2   | Run chkdsk in verbose mode on the volume every time it is mounted.                                                                                                                                                                                                      |
| 0x3   | Verify whether the dirty bit is set on the volume, and then perform a normal check on the file system.                                                                                                                                                                  |
| 0x4   | Don't perform any checks.                                                                                                                                                                                                                                               |
| 0x5   | Verify whether the dirty bit is set on the volume, and then perform a verbose check on the file system. If a problem is found, chkdsk is started and the volume is not brought online.                                                                                  |



 

## Remarks

Forcing a disk to mount despite errors can result in loss of data. Use caution when changing these properties.

> [!Note]  
> The chkdsk tool cannot be run on a cluster shared volume (CSV) that is operating in redirected mode.

 

## Examples

The property value portion of a [property list](property-lists.md) entry for **DiskRunChkDsk** can be set with the following example code.


```C++
DWORD          DiskRunChkdskData = 5;
CLUSPROP_DWORD DiskRunChkdskValue;

DiskRunChkdskValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
DiskRunChkdskValue.cbLength  = sizeof(DWORD);
DiskRunChkdskValue.dw        = DiskRunChkdskData;
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

[**ConditionalMount**](physical-disks-conditionalmount.md)
</dt> <dt>

[**SkipChkdsk**](physical-disks-skipchkdsk.md)
</dt> </dl>

 

 





