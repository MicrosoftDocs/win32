---
title: CreateRamWTDisk method of the WT\_Disk class
description: Create a new RAM-based iSCSI virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 95b1b452-9c4c-41b2-97f4-4ccc8ccb3494
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateRamWTDisk method iSCSI Software Target API
- CreateRamWTDisk method iSCSI Software Target API , WT_Disk class
- WT_Disk class iSCSI Software Target API , CreateRamWTDisk method
topic_type:
- apiref
api_name:
- WT_Disk.CreateRamWTDisk
api_location:
- WtWmiProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateRamWTDisk method of the WT\_Disk class

Create a new RAM-based iSCSI virtual disk, which is not persisted and cannot be used in a failover cluster environment.

## Syntax


```mof
WT_Disk CreateRamWTDisk(
  [in] string DevicePath,
  [in] uint64 MaxInternalSize,
  [in] uint32 LogicalSectorSize,
  [in] uint32 PhysicalSectorSize,
  [in] string Description
);
```



## Parameters

<dl> <dt>

*DevicePath* \[in\]
</dt> <dd>

A decorated device path in the format of "RAMDISK:".

</dd> <dt>

*MaxInternalSize* \[in\]
</dt> <dd>

The maximum size of the virtual hard disk as viewable by an initiator, in bytes. The specified size is rounded up based on the larger value of among logical, physical sector size and memory page size.

</dd> <dt>

*LogicalSectorSize* \[in\]
</dt> <dd>

The logical sector size in bytes used by the virtual disk.

</dd> <dt>

*PhysicalSectorSize* \[in\]
</dt> <dd>

The physical sector size in bytes used by the virtual disk.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

iSCSI disk description.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                            |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>Wmiwtprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**WT\_Disk**](wt-disk.md)
</dt> </dl>

 

 





