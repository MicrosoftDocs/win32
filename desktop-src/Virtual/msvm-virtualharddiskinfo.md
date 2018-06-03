---
title: Msvm\_VirtualHardDiskInfo class
description: Provides detailed information about an existing virtual hard disk image.
ms.assetid: 8ff4a58f-a754-4cbd-8cb5-2d2c770ae88f
keywords:
- Msvm_VirtualHardDiskInfo class Hyper-V
- Msvm_VirtualHardDiskInfo class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_VirtualHardDiskInfo
- Msvm_VirtualHardDiskInfo.Type
- Msvm_VirtualHardDiskInfo.FileSize
- Msvm_VirtualHardDiskInfo.MaxInternalSize
- Msvm_VirtualHardDiskInfo.InSavedState
- Msvm_VirtualHardDiskInfo.InUse
- Msvm_VirtualHardDiskInfo.ParentPath
api_location:
- Root\Virtualization
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_VirtualHardDiskInfo class

Provides detailed information about an existing virtual hard disk (VHD) image.

The following syntax is simplified Managed Object Format (MOF) code.

## Syntax

``` syntax
[AMENDMENT]
class Msvm_VirtualHardDiskInfo
{
  uint16  Type;
  uint64  FileSize;
  uint64  MaxInternalSize;
  boolean InSavedState;
  boolean InUse;
  string  ParentPath;
};
```

## Members

The **Msvm\_VirtualHardDiskInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualHardDiskInfo** class has these properties.

<dl> <dt>

**FileSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The size of the VHD file on the physical disk (the actual amount of storage being consumed by the VHD), in bytes.

</dd> <dt>

**InSavedState**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this VHD is associated with a virtual machine (VM) in a saved state.

</dd> <dt>

**InUse**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this VHD is currently mounted.

**Windows Server 2008:** The **InUse** property is **TRUE** if the VHD is mounted or if it is in use by a VM.

</dd> <dt>

**MaxInternalSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum size of the VHD as viewable by the VM, in bytes. The specified size will be rounded up to the next largest multiple of the sector size.

</dd> <dt>

**ParentPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The parent of the VHD. If the VHD does not have a parent, then this field is empty.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of VHD.

<dt>

<span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span>

**Fixed** (2)


</dt> <dd></dd> <dt>

<span id="Dynamic"></span><span id="dynamic"></span><span id="DYNAMIC"></span>

**Dynamic** (3)


</dt> <dd></dd> <dt>

<span id="Differencing"></span><span id="differencing"></span><span id="DIFFERENCING"></span>

**Differencing** (4)


</dt> <dd></dd> </dl>

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualHardDiskInfo** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[Storage Classes](storage-classes.md)
</dt> </dl>

 

 





