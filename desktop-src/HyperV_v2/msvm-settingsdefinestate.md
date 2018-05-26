---
Description: Associates a virtual machine and its devices with instances of CIM\_SettingData that represent the current settings that apply to these objects.
ms.assetid: 991FE773-1F87-4D5E-89E6-CB1A33989B1A
title: Msvm\_SettingsDefineState class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_SettingsDefineState class

Associates a virtual machine and its devices with instances of [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911) that represent the current settings that apply to these objects. More specifically, it associates [**Msvm\_ComputerSystem**](msvm-computersystem.md) with instances of [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md), and it associates **Msvm\_\*** derivatives of [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) with **Msvm\_\*** derivatives of [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider")]
class Msvm_SettingsDefineState : CIM_SettingsDefineState
{
  Msvm_ComputerSystem           REF ManagedElement;
  Msvm_VirtualSystemSettingData REF SettingData;
};
```

## Members

The **Msvm\_SettingsDefineState** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_SettingsDefineState** class has these properties.

<dl> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_ComputerSystem**](msvm-computersystem.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to the virtual machine.

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to the currently active settings for the virtual machine.

</dd> </dl>

## Remarks

Access to the **Msvm\_SettingsDefineState** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_SettingsDefineState**](cim-settingsdefinestate.md)
</dt> <dt>

[**CIM\_SettingsDefineState**](https://msdn.microsoft.com/library/mt146258)
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

 




