---
title: Msvm\_ElementSettingData class
description: Associates a managed element with its configuration data.
ms.assetid: 724c2a93-b23d-4b95-a340-13eb3751bfd8
keywords:
- Msvm_ElementSettingData class Hyper-V
- Msvm_ElementSettingData class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_ElementSettingData
- Msvm_ElementSettingData.ManagedElement
- Msvm_ElementSettingData.SettingData
- Msvm_ElementSettingData.IsDefault
- Msvm_ElementSettingData.IsCurrent
- Msvm_ElementSettingData.IsNext
- Msvm_ElementSettingData.IsMaximum
- Msvm_ElementSettingData.IsMinimum
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

# Msvm\_ElementSettingData class

Associates a managed element with its configuration data. Some of the more notable applications of this association are its use in linking a virtual computer system and the logical devices that have been assigned to that system with their snapshot configuration information. Current configuration information is associated with the virtual system and its devices through the [**Msvm\_SettingsDefineState**](msvm-settingsdefinestate.md) association.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ElementSettingData : CIM_ElementSettingData
{
  CIM_ManagedElement REF ManagedElement;
  CIM_SettingData    REF SettingData;
  uint16                 IsDefault = 0;
  uint16                 IsCurrent = 0;
  uint16                 IsNext = 0;
  uint16                 IsMaximum = 0;
  uint16                 IsMinimum = 0;
};
```

## Members

The **Msvm\_ElementSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ElementSettingData** class has these properties.

<dl> <dt>

**IsCurrent**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates that the referenced setting is currently being used in the operation of the element or that this information is unknown. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053). The default value is 0 (Unknown).

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

Indicates that the referenced setting is a default setting for the element or that this information is unknown. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053). The default value is 0 (Unknown).

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

This property affects the interpretation of all non-null, non-enumerated, non-binary, numeric, non-key properties of the associated setting data instance. All other properties of the associated setting data instance are not affected by this property. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053).

> [!Note]  
> It is assumed that the semantics of each property of this set are designed to be compared mathematically.

 

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The affected property values specified in the associated setting data instance may correspond to maximum setting values.

</dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (1)


</dt> <dd>

The affected property values specified in the associated setting data instance shall not be interpreted with respect to whether each defines a maximum.

</dd> <dt>

<span id="Is_Maximum"></span><span id="is_maximum"></span><span id="IS_MAXIMUM"></span>

<span id="Is_Maximum"></span><span id="is_maximum"></span><span id="IS_MAXIMUM"></span>**Is Maximum** (2)


</dt> <dd>

The affected property values specified in the associated setting data instance shall define maximum setting values.

</dd> <dt>

<span id="Is_Not_Maximum"></span><span id="is_not_maximum"></span><span id="IS_NOT_MAXIMUM"></span>

<span id="Is_Not_Maximum"></span><span id="is_not_maximum"></span><span id="IS_NOT_MAXIMUM"></span>**Is Not Maximum** (3)


</dt> <dd>

The affected property values specified in the associated setting data instance shall not define maximum setting values.

</dd> </dl>

</dd> <dt>

**IsMinimum**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

This property affects the interpretation of all non-null, non-enumerated, non-binary, numeric, non-key properties of the associated setting data instance. All other properties of the associated setting data instance are not affected by this property. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053).

> [!Note]  
> It is assumed that the semantics of each property of this set are designed to be compared mathematically.

 

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The affected property values specified in the associated setting data instance may correspond to minimum setting values.

</dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (1)


</dt> <dd>

The affected property values specified in the associated setting data instance shall not be interpreted with respect to whether each defines a minimum.

</dd> <dt>

<span id="Is_Minimum"></span><span id="is_minimum"></span><span id="IS_MINIMUM"></span>

<span id="Is_Minimum"></span><span id="is_minimum"></span><span id="IS_MINIMUM"></span>**Is Minimum** (2)


</dt> <dd>

The affected property values specified in the associated setting data instance shall define minimum setting values.

</dd> <dt>

<span id="Is_Not_Minimum"></span><span id="is_not_minimum"></span><span id="IS_NOT_MINIMUM"></span>

<span id="Is_Not_Minimum"></span><span id="is_not_minimum"></span><span id="IS_NOT_MINIMUM"></span>**Is Not Minimum** (3)


</dt> <dd>

The affected property values specified in the associated setting data instance shall not define minimum setting values.

</dd> </dl>

</dd> <dt>

**IsNext**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Indicates whether the referenced setting is the next setting to be applied. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053). The default value is 0 (Unknown).

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

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the virtual computer system or virtual device. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053).

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_SettingData**](cim-settingdata.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the snapshotted settings for the virtual computer system or virtual device. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053).

</dd> </dl>

## Remarks

Access to the **Msvm\_ElementSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

See [Querying Networking Objects](querying-networking-objects.md).

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

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

 





