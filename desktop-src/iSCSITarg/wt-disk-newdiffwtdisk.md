---
title: NewDiffWTDisk method of the WT\_Disk class
description: Creates a new differencing virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1873A658-F824-4EE2-8861-8C4F7646477F'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["NewDiffWTDisk method iSCSI Software Target API", "NewDiffWTDisk method iSCSI Software Target API , WT_Disk class", "WT_Disk class iSCSI Software Target API , NewDiffWTDisk method"]
topic_type:
- apiref
api_name:
- WT_Disk.NewDiffWTDisk
api_location:
- WtWmiProv.dll
api_type:
- COM
---

# NewDiffWTDisk method of the WT\_Disk class

Creates a new differencing virtual disk.

**Windows Server 2012 R2:** This method is deprecated. Use [**CreateRamWTDisk**](createramwtdisk-wt-disk.md), [**CreateVhdWTDisk**](createvhdwtdisk-wt-disk.md), or [**ImportWTDisk**](importwtdisk-wt-disk.md) instead.

## Syntax


```mof
WT_Disk NewDiffWTDisk(
   string  DevicePath,
   string  ParentPath,
   string  Description,
   boolean CacheParent
);
```



## Parameters

<dl> <dt>

*DevicePath* 
</dt> <dd>

Full path to the VHD file.

</dd> <dt>

*ParentPath* 
</dt> <dd>

Full path to the parent VHD file.

</dd> <dt>

*Description* 
</dt> <dd>

An iSCSI disk friendly description.

</dd> <dt>

*CacheParent* 
</dt> <dd>

Deprecated; do not use.

</dd> </dl>

## Remarks

If the Microsoft iSCSI Target Server service is running on a Microsoft Failover Cluster, a cluster resource is created to represent the new virtual disk (VHD). The cluster resource resides in the same resource group as the physical disk where the VHD is stored.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
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

 

 





