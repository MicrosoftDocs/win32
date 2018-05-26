---
title: Msvm\_PreviousSettingData class
description: An association between a virtual system and the setting data of the snapshot that is the parent to the virtual system.
ms.assetid: 4bb90616-c577-4c5f-a765-3e543748f5c7
keywords:
- Msvm_PreviousSettingData class Hyper-V
- Msvm_PreviousSettingData class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_PreviousSettingData
- Msvm_PreviousSettingData.IsDefault
- Msvm_PreviousSettingData.IsNext
- Msvm_PreviousSettingData.IsMaximum
- Msvm_PreviousSettingData.SettingData
- Msvm_PreviousSettingData.ManagedElement
- Msvm_PreviousSettingData.IsCurrent
- Msvm_PreviousSettingData.IsMinimum
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

# Msvm\_PreviousSettingData class

An association between a virtual system and the setting data of the snapshot that is the parent to the virtual system.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_PreviousSettingData : CIM_ElementSettingData
{
  uint16                            IsDefault;
  uint16                            IsNext;
  uint16                            IsMaximum = 0;
  Msvm_VirtualSystemSettingData REF SettingData;
  Msvm_ComputerSystem           REF ManagedElement;
  uint16                            IsCurrent;
  uint16                            IsMinimum = 0;
};
```

## Members

The **Msvm\_PreviousSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_PreviousSettingData** class has these properties.

<dl> <dt>

**IsCurrent**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the referenced setting is currently used in the operation of the element or that this information is unknown. For a given managed element and all instances of a setting data subclass, there shall be at most one instance that references the managed element and an instance of the setting data subclass where there is a specified non-null, non-key property, and the **IsMaximum** property on the referencing element setting data instance has a value of 2 (Is Maximum) or the **IsMinimum** property on the referencing element setting data instance has a value of 2 (Is Minimum) and the **IsCurrent** property on the referencing element setting data instance has a value of 1 (Is Current).

There shall be at most one instance of element setting data that references a managed element and an instance of a setting data subclass where the **IsCurrent** property has a value of 1 (Is Current) and the **IsMinimum** property does not have a value of 2 (Is Minimum) and the **IsMaximum** property does not have a value of 2 (Is Maximum). This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053).

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

Indicates whether the referenced setting is a default setting for the element or that this information is unknown. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053).

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

This property affects the interpretation of all non-null, non-enumerated, non-binary, numeric, non-key properties of the associated setting data instance. All other properties of the associated setting data instance are not affected by this property. Note: It is assumed that the semantics of each property of this set are designed to be compared mathematically. When **IsMaximum**= 2 (Is Maximum), this property indicates whether the affected property values specified in the associated setting data instance shall define maximum setting values. When **IsMaximum**= 3 (Is Not Maximum), this property indicates whether the affected property values specified in the associated setting data instance shall not define maximum setting values. When **IsMaximum**= 0 (Unknown), this property indicates whether the affected property values specified in the associated setting data instance may correspond to maximum setting values. When **IsMaximum**= 1 (Not Applicable), this property indicates whether the affected property values specified in the associated setting data instance shall not be interpreted with respect to whether each defines a maximum. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053).

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

This property affects the interpretation of all non-null, non-enumerated, non-binary, numeric, non-key properties of the associated setting data instance. All other properties of the associated setting data instance are not affected by this property. Be aware that it is assumed that the semantics of each property of this set are designed to be compared mathematically. When **IsMinimum** = 2 (Is Minimum), this property indicates whether the affected property values specified in the associated setting data instance shall define minimum setting values. When **IsMinimum** = 3 (Is Not Minimum), this property indicates whether the affected property values specified in the associated setting data instance shall not define minimum setting values. When **IsMinimum** = 0 (Unknown), this property indicates whether the affected property values specified in the associated setting data instance may correspond to minimum setting values. When **IsMinimum** = 1 (Not Applicable), this property indicates whether the affected property values specified in the associated setting data instance shall not be interpreted with respect to whether each defines a minimum. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053).

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

Indicates whether the referenced setting is the next setting to be applied. For example, the application could occur on a reinitialization, reset, or reconfiguration request. This could be a permanent setting, or a setting used only one time, as indicated by the flag. If it is a permanent setting then the setting is applied every time the managed element reinitializes, until this flag is manually reset. However, if it is single use, then the flag is automatically cleared after the settings are applied.

If this flag is specified (that is, set to a value other than 0 - Unknown), then this takes precedence over any setting data that may have been specified as default. For example: If the managed element is a computer system, and the value of this flag is 1 (Is Next), then the setting will be effective next time the system resets. Unless this flag is changed, it will persist for subsequent system resets. However, if this flag is set to 3 (Is Next For Single Use), then this setting will only be used once and the flag would be reset after that to 2 (Is Not Next). In the preceding example, if the system restarts in a quick succession, the setting will not be used at the second restart.

This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053).

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

Data type: **Msvm\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("ManagedElement")
</dt> </dl>

The computer system that is the target of the application. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053).

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_VirtualSystemSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("SettingData")
</dt> </dl>

The snapshot setting data that is the parent of this computer system. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053).

</dd> </dl>

## Remarks

Access to the **Msvm\_PreviousSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_ElementSettingData**](cim-elementsettingdata.md)
</dt> <dt>

[**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053)
</dt> <dt>

[Virtual System Classes](virtual-system-classes.md)
</dt> </dl>

 

 





