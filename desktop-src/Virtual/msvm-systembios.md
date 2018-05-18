---
title: Msvm\_SystemBIOS class
description: Used to associate a virtual system with its BIOS.
ms.assetid: '99403b20-d39b-4f25-8b7a-cea8d13bbecf'
keywords: ["Msvm_SystemBIOS class Hyper-V", "Msvm_SystemBIOS class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_SystemBIOS
- Msvm_SystemBIOS.GroupComponent
- Msvm_SystemBIOS.PartComponent
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_SystemBIOS class

Used to associate a virtual system with its BIOS.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SystemBIOS : CIM_SystemBIOS
{
  Msvm_ComputerSystem REF GroupComponent;
  Msvm_BIOSElement    REF PartComponent;
};
```

## Members

The **Msvm\_SystemBIOS** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_SystemBIOS** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_ComputerSystem**](msvm-computersystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The virtual computer system that starts from the BIOS.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_BIOSElement**](msvm-bioselement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The BIOS associated with the virtual system.

</dd> </dl>

## Remarks

Access to the **Msvm\_SystemBIOS** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_SystemBIOS**](cim-systembios.md)
</dt> <dt>

[BIOS Classes](bios-classes.md)
</dt> </dl>

 

 





