---
title: Msvm\_SystemExportSettingData class
description: Associates a virtual system and its export setting data.
ms.assetid: eac54cf3-4216-42d8-af60-012ebe951f07
keywords:
- Msvm_SystemExportSettingData class Hyper-V
- Msvm_SystemExportSettingData class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_SystemExportSettingData
- Msvm_SystemExportSettingData.IsDefault
- Msvm_SystemExportSettingData.IsCurrent
- Msvm_SystemExportSettingData.IsNext
- Msvm_SystemExportSettingData.IsMaximum
- Msvm_SystemExportSettingData.IsMinimum
- Msvm_SystemExportSettingData.ManagedElement
- Msvm_SystemExportSettingData.SettingData
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

# Msvm\_SystemExportSettingData class

Associates a virtual system and its export setting data. Before calling the [**ExportVirtualSystemEx**](msvm-virtualsystemmanagementservice-exportvirtualsystemex.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class, an instance of [**Msvm\_VirtualSystemExportSettingData**](msvm-virtualsystemexportsettingdata.md) can be retrieved using this association.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SystemExportSettingData : CIM_ElementSettingData
{
  uint16                                  IsDefault;
  uint16                                  IsCurrent;
  uint16                                  IsNext;
  uint16                                  IsMaximum = 0;
  uint16                                  IsMinimum = 0;
  Msvm_ComputerSystem                 REF ManagedElement;
  Msvm_VirtualSystemExportSettingData REF SettingData;
};
```

## Members

The **Msvm\_SystemExportSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_SystemExportSettingData** class has these properties.

<dl> <dt>

**IsCurrent**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the referenced setting is currently being used by the element.

This property is inherited from [**CIM\_ElementSettingData**](cim-elementsettingdata.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Is_Current"></span><span id="is_current"></span><span id="IS_CURRENT"></span>

**Is Current** (1)


</dt> <dd></dd> <dt>

<span id="Is_Not_Current"></span><span id="is_not_current"></span><span id="IS_NOT_CURRENT"></span>

**Is Not Current** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**IsDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicating whether the setting is a default setting for the element.

This property is inherited from [**CIM\_ElementSettingData**](cim-elementsettingdata.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Is_Default"></span><span id="is_default"></span><span id="IS_DEFAULT"></span>

**Is Default** (1)


</dt> <dd></dd> <dt>

<span id="Is_Not_Default"></span><span id="is_not_default"></span><span id="IS_NOT_DEFAULT"></span>

**Is Not Default** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**IsMaximum**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

This property affects the interpretation of all non-null, non-enumerated, non-binary, numeric, non-key properties of the associated setting data instance. All other properties of the associated setting data instance are not affected by this property.

This property is inherited from [**CIM\_ElementSettingData**](cim-elementsettingdata.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (1)


</dt> <dd></dd> <dt>

<span id="Is_Maximum"></span><span id="is_maximum"></span><span id="IS_MAXIMUM"></span>

**Is Maximum** (2)


</dt> <dd></dd> <dt>

<span id="Is_Not_Maximum"></span><span id="is_not_maximum"></span><span id="IS_NOT_MAXIMUM"></span>

**Is Not Maximum** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**IsMinimum**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

This property affects the interpretation of all non-null, non-enumerated, non-binary, numeric, non-key properties of the associated setting data instance. All other properties of the associated setting data instance are not affected by this property.

This property is inherited from [**CIM\_ElementSettingData**](cim-elementsettingdata.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (1)


</dt> <dd></dd> <dt>

<span id="Is_Minimum"></span><span id="is_minimum"></span><span id="IS_MINIMUM"></span>

**Is Minimum** (2)


</dt> <dd></dd> <dt>

<span id="Is_Not_Minimum"></span><span id="is_not_minimum"></span><span id="IS_NOT_MINIMUM"></span>

**Is Not Minimum** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**IsNext**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

A flag that indicates when and how often to apply the setting.

For example, the setting could be applied on a re-initialization, reset, reconfiguration request. This could be a permanent setting, or a setting used only one time, as indicated by the flag. If it is a permanent setting then the setting is applied every time the managed element reinitializes, until this flag is manually reset. However, if it is single use, then the flag is automatically cleared after the settings are applied. In addition, if this flag is set to value other than 0 (Unknown), then this takes precedence over a **SettingData** property that is set to "Default".

If the managed element is a computer system, and the value of this flag is "Is Next", then the setting will be effective next time the system resets. And, unless this flag is changed, it will persist for subsequent system resets. However, if this flag is set to "Is Next For Single Use", then this setting will only be used once and the flag would be reset after that to 2 (Is Not Next). So, in the above example, if the system reboots in a quick succession, the setting will not be used at the second reboot.

This property is inherited from [**CIM\_ElementSettingData**](cim-elementsettingdata.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

Unknown.

</dd> <dt>

<span id="Is_Next"></span><span id="is_next"></span><span id="IS_NEXT"></span>

<span id="Is_Next"></span><span id="is_next"></span><span id="IS_NEXT"></span>**Is Next** (1)


</dt> <dd>

The setting will be applied to the managed element every time the managed element is reset.

</dd> <dt>

<span id="Is_Not_Next"></span><span id="is_not_next"></span><span id="IS_NOT_NEXT"></span>

<span id="Is_Not_Next"></span><span id="is_not_next"></span><span id="IS_NOT_NEXT"></span>**Is Not Next** (2)


</dt> <dd>

This setting is no longer used.

</dd> <dt>

<span id="Is_Next_For_Single_Use"></span><span id="is_next_for_single_use"></span><span id="IS_NEXT_FOR_SINGLE_USE"></span>

<span id="Is_Next_For_Single_Use"></span><span id="is_next_for_single_use"></span><span id="IS_NEXT_FOR_SINGLE_USE"></span>**Is Next For Single Use** (3)


</dt> <dd>

The setting will only be applied to the managed element once, and then this flag will be set to **Is Not Next** (2).

</dd> </dl>

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_ComputerSystem**](msvm-computersystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ElementSettingData.ManagedElement")
</dt> </dl>

Reference to the virtual system.

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_VirtualSystemExportSettingData**](msvm-virtualsystemexportsettingdata.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ElementSettingData.SettingData")
</dt> </dl>

Reference to the export setting data for the virtual system.

</dd> </dl>

## Remarks

Access to the **Msvm\_SystemExportSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                    |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



 

 





