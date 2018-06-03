---
title: CreateVhdWTDisk method of the WT\_Disk class
description: Create a new VHDX-based iSCSI virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fb406648-8387-458e-aa7f-6434ea914266
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateVhdWTDisk method iSCSI Software Target API
- CreateVhdWTDisk method iSCSI Software Target API , WT_Disk class
- WT_Disk class iSCSI Software Target API , CreateVhdWTDisk method
topic_type:
- apiref
api_name:
- WT_Disk.CreateVhdWTDisk
api_location:
- WtWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateVhdWTDisk method of the WT\_Disk class

Create a new VHDX-based iSCSI virtual disk.

## Syntax


```mof
WT_Disk CreateVhdWTDisk(
  [in] string  DevicePath,
  [in] uint16  VhdType,
  [in] uint64  MaxInternalSize,
  [in] uint32  BlockSize,
  [in] uint32  LogicalSectorSize,
  [in] uint32  PhysicalSectorSize,
  [in] string  Description,
  [in] boolean ClearData,
  [in] string  ParentPath
);
```



## Parameters

<dl> <dt>

*DevicePath* \[in\]
</dt> <dd>

Full path to VHDX file.

</dd> <dt>

*VhdType* \[in\]
</dt> <dd>

VHD type.

<dt>

<span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span>

**Fixed** (2)


</dt> <dd></dd> <dt>

<span id="Dynamic"></span><span id="dynamic"></span><span id="DYNAMIC"></span>

**Dynamic** (3)


</dt> <dd></dd> <dt>

<span id="Differencing"></span><span id="differencing"></span><span id="DIFFERENCING"></span>

**Differencing** (4)


</dt> <dd></dd> </dl> </dd> <dt>

*MaxInternalSize* \[in\]
</dt> <dd>

The maximum size of the virtual hard disk as viewable by an initiator, in bytes. The specified size is rounded up based on the larger value of either logical or physical sector size.

</dd> <dt>

*BlockSize* \[in\]
</dt> <dd>

The block size in bytes used by the VHDX.

</dd> <dt>

*LogicalSectorSize* \[in\]
</dt> <dd>

The logical sector size in bytes used by the VHDX.

</dd> <dt>

*PhysicalSectorSize* \[in\]
</dt> <dd>

The physical sector size in bytes used by the VHDX.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

iSCSI disk description.

</dd> <dt>

*ClearData* \[in\]
</dt> <dd>

Whether to clear data upon fixed VHDX creation

</dd> <dt>

*ParentPath* \[in\]
</dt> <dd>

Full path to parent VHD file

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

 

 





