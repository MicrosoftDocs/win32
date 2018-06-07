---
Description: Associates a storage drive with the media inserted into the drive.
ms.assetid: C0B2D604-0B55-4EA0-A46E-2450D89A5B22
title: Msvm\_MediaPresent class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Data type: **[**CIM\_MediaAccessDevice**](https://msdn.microsoft.com/library/aa387901)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The reference to the media access device. This property is inherited from [**CIM\_MediaPresent**](https://msdn.microsoft.com/library/aa387903).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The reference to the storage extent accessed with the media access device. This property is inherited from [**CIM\_MediaPresent**](https://msdn.microsoft.com/library/aa387903).

</dd> <dt>

**FixedMedia**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the accessed storage extent is fixed and cannot be ejected. The value is **True** for hard disks and **False** otherwise. This property is inherited from [**CIM\_MediaPresent**](https://msdn.microsoft.com/library/aa387903).

</dd> </dl>

## Remarks

Access to the **Msvm\_MediaPresent** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                         |
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

[**CIM\_MediaPresent**](https://msdn.microsoft.com/library/aa387903)
</dt> <dt>

[Storage Classes](storage-classes.md)
</dt> </dl>

 

 




