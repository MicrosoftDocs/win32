---
title: Msvm\_ParentChildSettingData class
description: An association between an instance of Msvm\_VirtualSystemSettingData and the Msvm\_VirtualSystemSettingData instance that represents the most recent snapshot upon which this object is based.
ms.assetid: 8c9bfe20-eee3-4db6-8862-076e4cb80e7c
keywords:
- Msvm_ParentChildSettingData class Hyper-V
- Msvm_ParentChildSettingData class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_ParentChildSettingData
- Msvm_ParentChildSettingData.Antecedent
- Msvm_ParentChildSettingData.Dependent
api_location:
- Root\Virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_ParentChildSettingData class

An association between an instance of [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) and the **Msvm\_VirtualSystemSettingData** instance that represents the most recent snapshot upon which this object is based.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ParentChildSettingData : CIM_Dependency
{
  Msvm_VirtualSystemSettingData REF Antecedent;
  Msvm_VirtualSystemSettingData REF Dependent;
};
```

## Members

The **Msvm\_ParentChildSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ParentChildSettingData** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Dependency.Antecedent")
</dt> </dl>

The snapshot setting data upon which the child setting data is based.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Dependency.Dependent")
</dt> </dl>

The setting data for the virtual system that represents the child of the parent.

</dd> </dl>

## Remarks

Access to the **Msvm\_ParentChildSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dt>

[**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238)
</dt> <dt>

[Virtual System Classes](virtual-system-classes.md)
</dt> </dl>

 

 





