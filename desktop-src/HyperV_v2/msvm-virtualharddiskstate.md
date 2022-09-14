---
description: Provides state information for an existing virtual hard disk image.
ms.assetid: b0177906-71dc-4be8-b351-97d7ef427acd
title: Msvm_VirtualHardDiskState class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualHardDiskState
- Msvm_VirtualHardDiskState.FileSize
- Msvm_VirtualHardDiskState.InUse
- Msvm_VirtualHardDiskState.MinInternalSize
- Msvm_VirtualHardDiskState.PhysicalSectorSize
- Msvm_VirtualHardDiskState.Alignment
- Msvm_VirtualHardDiskState.FragmentationPercentage
- Msvm_VirtualHardDiskState.Timestamp
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_VirtualHardDiskState class

Provides state information for an existing virtual hard disk image.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Msvm_VirtualHardDiskState
{
  uint64   FileSize;
  boolean  InUse;
  uint64   MinInternalSize;
  uint32   PhysicalSectorSize;
  uint32   Alignment;
  uint32   FragmentationPercentage;
  DATETIME Timestamp;
};
```

## Members

The **Msvm\_VirtualHardDiskState** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualHardDiskState** class has these properties.

<dl> <dt>

**Alignment**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the type of alignment of the virtual hard disk. This will be one of the following values.



| Value                                                                        | Meaning                        |
|------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>0</dt> </dl> | 512 byte alignment.<br/> |
| <dl> <dt>1</dt> </dl> | 4 KB alignment.<br/>     |



 

</dd> <dt>

**FileSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The size of the virtual hard disk file (the actual amount of storage being consumed by the file), in bytes.

</dd> <dt>

**FragmentationPercentage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An approximation of the percentage of virtual disk blocks that are fragmented in the virtual hard disk file.

</dd> <dt>

**InUse**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is reserved for future use.

</dd> <dt>

**MinInternalSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minimum size that the virtual hard disk can be shrunk to, in bytes. This size is rounded up to the next largest multiple of the sector size.

</dd> <dt>

**PhysicalSectorSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The physical sector size used by the underlying physical disk, in bytes.

</dd> <dt>

**Timestamp**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The timestamp of the virtual hard disk

> [!Note]  
> Added in Windows 10 and Windows Server 2016.

 

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**GetVirtualHardDiskState**](getvirtualharddiskstate-msvm-imagemanagementservice.md)
</dt> </dl>

 

 




