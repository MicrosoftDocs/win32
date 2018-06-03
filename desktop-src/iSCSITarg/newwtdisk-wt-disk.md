---
title: NewWTDisk method of the WT\_Disk class
description: Creates a new virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e6a422a1-2918-4870-bebe-b8a865a181fc
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- NewWTDisk method iSCSI Software Target API
- NewWTDisk method iSCSI Software Target API , WT_Disk class
- WT_Disk class iSCSI Software Target API , NewWTDisk method
topic_type:
- apiref
api_name:
- WT_Disk.NewWTDisk
api_location:
- WtWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NewWTDisk method of the WT\_Disk class

Creates a new virtual disk.

**Windows Server 2012 R2:** This method is deprecated. Use [**CreateRamWTDisk**](createramwtdisk-wt-disk.md), [**CreateVhdWTDisk**](createvhdwtdisk-wt-disk.md), or [**ImportWTDisk**](importwtdisk-wt-disk.md) instead.

## Syntax


```mof
WT_Disk NewWTDisk(
  [in] string  DevicePath,
  [in] string  Description,
  [in] boolean ClearPartTable,
  [in] uint32  SizeInMB
);
```



## Parameters

<dl> <dt>

*DevicePath* \[in\]
</dt> <dd>

Full path to the VHD file.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Friendly description of the iSCSI Disk.

</dd> <dt>

*ClearPartTable* \[in\]
</dt> <dd>

Deprecated; do not use.

</dd> <dt>

*SizeInMB* \[in\]
</dt> <dd>

The iSCSI Disk Size, in megabytes.

</dd> </dl>

## Remarks

If the Microsoft iSCSI Target Server service is running on a Microsoft Failover Cluster, a cluster resource is created to represent the new virtual disk (VHD). The cluster resource resides in the same resource group as the physical disk where the VHD is stored.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**WT\_Disk**](wt-disk.md)
</dt> <dt>

[**CreateRamWTDisk**](createramwtdisk-wt-disk.md)
</dt> <dt>

[**CreateVhdWTDisk**](createvhdwtdisk-wt-disk.md)
</dt> <dt>

[**ImportWTDisk**](importwtdisk-wt-disk.md)
</dt> </dl>

 

 





