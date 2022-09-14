---
description: Provides setting data for a virtual hard disk.
ms.assetid: 492a0b81-86b2-4d7d-a118-6ec14e3971ed
title: Msvm_VirtualHardDiskSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualHardDiskSettingData
- Msvm_VirtualHardDiskSettingData.InstanceID
- Msvm_VirtualHardDiskSettingData.Caption
- Msvm_VirtualHardDiskSettingData.Description
- Msvm_VirtualHardDiskSettingData.ElementName
- Msvm_VirtualHardDiskSettingData.Type
- Msvm_VirtualHardDiskSettingData.Format
- Msvm_VirtualHardDiskSettingData.Path
- Msvm_VirtualHardDiskSettingData.ParentPath
- Msvm_VirtualHardDiskSettingData.ParentTimestamp
- Msvm_VirtualHardDiskSettingData.ParentIdentifier
- Msvm_VirtualHardDiskSettingData.MaxInternalSize
- Msvm_VirtualHardDiskSettingData.BlockSize
- Msvm_VirtualHardDiskSettingData.LogicalSectorSize
- Msvm_VirtualHardDiskSettingData.PhysicalSectorSize
- Msvm_VirtualHardDiskSettingData.VirtualDiskId
- Msvm_VirtualHardDiskSettingData.DataAlignment
- Msvm_VirtualHardDiskSettingData.PmemAddressAbstractionType
- Msvm_VirtualHardDiskSettingData.IsPmemCompatible
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_VirtualHardDiskSettingData class

Provides setting data for a virtual hard disk.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Msvm_VirtualHardDiskSettingData : CIM_SettingData
{
  string   InstanceID;
  string   Caption = "Virtual Hard Disk Setting Data";
  string   Description = "Setting Data for a Virtual Hard Disk";
  string   ElementName;
  uint16   Type;
  uint16   Format;
  string   Path;
  string   ParentPath;
  DATETIME ParentTimestamp;
  string   ParentIdentifier;
  uint64   MaxInternalSize;
  uint32   BlockSize;
  uint32   LogicalSectorSize;
  uint32   PhysicalSectorSize;
  string   VirtualDiskId;
  uint64   DataAlignment;
  uint16   PmemAddressAbstractionType;
  boolean  IsPmemCompatible;
};
```

## Members

The **Msvm\_VirtualHardDiskSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualHardDiskSettingData** class has these properties.

<dl> <dt>

**BlockSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The block size used by the virtual hard disk, in bytes.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Virtual Hard Disk Setting Data".

</dd> <dt>

**DataAlignment**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the desired alignment, in bytes, for the data payload of the virtual disk

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Setting Data for a Virtual Hard Disk".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**Format**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The format for the virtual hard disk. This will be one of the following values.

<dt>

<span id="VHD"></span><span id="vhd"></span>

<span id="VHD"></span><span id="vhd"></span>**VHD** (2)


</dt> <dd></dd> <dt>

<span id="VHDX"></span><span id="vhdx"></span>

<span id="VHDX"></span><span id="vhdx"></span>**VHDX** (3)


</dt> <dd></dd> <dt>

<span id="VHDSet"></span><span id="vhdset"></span><span id="VHDSET"></span>

<span id="VHDSet"></span><span id="vhdset"></span><span id="VHDSET"></span>**VHDSet** (4)


</dt> <dd>

> [!Note]  
> Added in Windows 10 and Windows Server 2016.

 

</dd> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_SettingData**](/previous-versions//cc136911(v=vs.85)).

</dd> <dt>

**IsPmemCompatible**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether the virtual disk can be used as the backing store for a persistent memory device.

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> <dt>

**LogicalSectorSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The logical sector size used by the virtual hard disk, in bytes.

</dd> <dt>

**MaxInternalSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum size of the virtual hard disk as viewable by the virtual machine, in bytes. This size will be rounded up to the next largest multiple of the sector size.

</dd> <dt>

**ParentIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The GUID used to uniquely identify the parent of the virtual hard disk. If the virtual hard disk does not have a parent, then this field is empty.

> [!Note]  
> Added in Windows 10 and Windows Server 2016.

 

</dd> <dt>

**ParentPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The parent of the virtual hard disk. If the virtual hard disk does not have a parent, then this property is empty.

</dd> <dt>

**ParentTimestamp**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The timestamp of the parent of the virtual hard disk. If the virtual hard disk does not have a parent, then this field is empty.

> [!Note]  
> Added in Windows 10 and Windows Server 2016.

 

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The fully qualified path of the virtual hard disk.

</dd> <dt>

**PhysicalSectorSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The physical sector size used by the virtual hard disk, in bytes.

</dd> <dt>

**PmemAddressAbstractionType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The persistent memory address abstraction method to be used with this virtual disk.

> [!Note]  
> Added in Windows 10, version 1709.

 

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="BTT"></span><span id="btt"></span>

**BTT** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (65535)


</dt> <dd></dd> </dl>

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The type of virtual hard disk. This will be one of the following values.

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

</dd> <dt>

**VirtualDiskId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The GUID that is used to uniquely identify the virtual disk.

When the [**Msvm\_ImageManagementService.GetVirtualHardDiskSettingData**](getvirtualharddisksettingdata-msvm-imagemanagementservice.md) method returns an instance of **Msvm\_VirtualHardDiskSettingData**, the client can use this property to get the unique disk ID of the VHD.

On conflict detection or otherwise, a client can set the **VirtualDiskId** value to a new GUID and pass this **Msvm\_VirtualHardDiskSettingData** instance to the [**Msvm\_ImageManagementService.SetVirtualHardDiskSettingData**](setvirtualharddisksettingdata-msvm-imagemanagementservice.md) method to change the disk ID of the VHD. If the VHD is not a VHDX VHD, or if the VHD is attached, the operation fails. The operation also fails if the passed value is malformed, that is, not a GUID or has all 0s. The operation silently succeeds if the passed value is the same as the current disk ID.

Errors generated by the [**SetVirtualDiskInformation**](/windows/win32/api/virtdisk/nf-virtdisk-setvirtualdiskinformation) function are bubbled up through this property. A client can also use the same mechanism to provide the **VirtualDiskId** value at VHD creation via the [**Msvm\_ImageManagementService.CreateVirtualHardDisk**](createvirtualharddisk-msvm-imagemanagementservice.md) method in the same namespace. This can be used to create VHD1 or VHD2 VHDs.

**Windows 8.1:** This value is not supported until Windows 8.1 and Windows Server 2012 R2.

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

[**CIM\_SettingData**](cim-settingdata.md)
</dt> <dt>

[**GetVirtualHardDiskSettingData**](getvirtualharddisksettingdata-msvm-imagemanagementservice.md)
</dt> </dl>

 

