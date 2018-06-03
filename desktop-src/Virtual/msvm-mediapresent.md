---
title: Msvm\_MediaPresent class
description: Associates a storage drive with the media inserted into the drive.
ms.assetid: 8060c15f-ff9c-47f7-85ba-8d5362eabba9
keywords:
- Msvm_MediaPresent class Hyper-V
- Msvm_MediaPresent class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_MediaPresent
- Msvm_MediaPresent.Antecedent
- Msvm_MediaPresent.Dependent
- Msvm_MediaPresent.FixedMedia
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

Data type: **CIM\_MediaAccessDevice**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The media access device.

This property is inherited from [**CIM\_MediaPresent**](cim-mediapresent.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StorageExtent**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The storage extent that is accessed when using the media access device.

This property is inherited from [**CIM\_MediaPresent**](cim-mediapresent.md).

</dd> <dt>

**FixedMedia**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the storage extent is fixed in the media access device and can not be ejected; otherwise, **false**.

This property is inherited from [**CIM\_MediaPresent**](cim-mediapresent.md).

</dd> </dl>

## Remarks

Access to the **Msvm\_MediaPresent** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_MediaPresent**](cim-mediapresent.md)
</dt> <dt>

[**CIM\_MediaPresent**](https://msdn.microsoft.com/library/aa387903)
</dt> <dt>

[Storage Classes](storage-classes.md)
</dt> </dl>

 

 





