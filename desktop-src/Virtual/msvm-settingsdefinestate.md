---
title: Msvm\_SettingsDefineState class
description: Associates a virtual system and its devices with instances of CIM\_SettingData representing the current settings that apply to these objects.
ms.assetid: 86c1dc91-a2b6-4cf5-ac6f-1f3db63a6a11
keywords:
- Msvm_SettingsDefineState class Hyper-V
- Msvm_SettingsDefineState class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_SettingsDefineState
- Msvm_SettingsDefineState.ManagedElement
- Msvm_SettingsDefineState.SettingData
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

# Msvm\_SettingsDefineState class

Associates a virtual system and its devices with instances of [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911) representing the current settings that apply to these objects. More specifically, it associates [**Msvm\_ComputerSystem**](msvm-computersystem.md) with instances of [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md), and it associates **Msvm\_\*** derivatives of [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) with **Msvm\_\*** derivatives of [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
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
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SettingsDefineState.ManagedElement")
</dt> </dl>

A reference to the virtual computer system.

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SettingsDefineState.SettingData")
</dt> </dl>

A reference to the currently active settings for the virtual computer system.

</dd> </dl>

## Remarks

Access to the **Msvm\_SettingsDefineState** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_SettingsDefineState**](cim-settingsdefinestate.md)
</dt> <dt>

[**CIM\_SettingsDefineState**](https://msdn.microsoft.com/library/cc136915)
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

 





