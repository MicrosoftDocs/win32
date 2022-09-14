---
description: Associates a storage drive with the media inserted into the drive.
ms.assetid: C0B2D604-0B55-4EA0-A46E-2450D89A5B22
title: Msvm_MediaPresent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_MediaPresent
- Msvm_MediaPresent.Antecedent
- Msvm_MediaPresent.Dependent
- Msvm_MediaPresent.FixedMedia
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_MediaPresent class

Associates a storage drive with the media inserted into the drive. This association is used for all storage drive objects.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_MediaPresent : CIM_MediaPresent
{
  CIM_MediaAccessDevice REF Antecedent;
  CIM_StorageExtent     REF Dependent;
  boolean                   FixedMedia;
};
```

## Members

The **Msvm\_MediaPresent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_MediaPresent** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_MediaAccessDevice**](/windows/desktop/CIMWin32Prov/cim-mediaaccessdevice)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The reference to the media access device. This property is inherited from [**CIM\_MediaPresent**](/windows/desktop/CIMWin32Prov/cim-mediapresent).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The reference to the storage extent accessed with the media access device. This property is inherited from [**CIM\_MediaPresent**](/windows/desktop/CIMWin32Prov/cim-mediapresent).

</dd> <dt>

**FixedMedia**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the accessed storage extent is fixed and cannot be ejected. The value is **True** for hard disks and **False** otherwise. This property is inherited from [**CIM\_MediaPresent**](/windows/desktop/CIMWin32Prov/cim-mediapresent).

</dd> </dl>

## Remarks

Access to the **Msvm\_MediaPresent** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

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

[**CIM\_MediaPresent**](cim-mediapresent.md)
</dt> <dt>

[**CIM\_MediaPresent**](/windows/desktop/CIMWin32Prov/cim-mediapresent)
</dt> <dt>

[Storage Classes](storage-classes.md)
</dt> </dl>

 

