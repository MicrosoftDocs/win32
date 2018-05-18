---
title: Msvm\_NetworkElementSettingData class
description: An association that connects a computer system to a LAN endpoint inside of Hyper-V.
ms.assetid: '27b902b7-cbac-4b56-91a1-6f500ca30652'
keywords: ["Msvm_NetworkElementSettingData class Hyper-V", "Msvm_NetworkElementSettingData class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_NetworkElementSettingData
- Msvm_NetworkElementSettingData.IsDefault
- Msvm_NetworkElementSettingData.IsNext
- Msvm_NetworkElementSettingData.IsMaximum
- Msvm_NetworkElementSettingData.IsMinimum
- Msvm_NetworkElementSettingData.SettingData
- Msvm_NetworkElementSettingData.ManagedElement
- Msvm_NetworkElementSettingData.IsCurrent
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_NetworkElementSettingData class

An association that connects a computer system to a LAN endpoint inside of Hyper-V. This object facilitates finding all of the LAN endpoints for a given computer system without having to know the Ethernet ports.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_NetworkElementSettingData : CIM_ElementSettingData
{
  uint16                           IsDefault;
  uint16                           IsNext;
  uint16                           IsMaximum = 0;
  uint16                           IsMinimum = 0;
  Msvm_VLANEndpointSettingData REF SettingData;
  Msvm_VLANEndpoint            REF ManagedElement;
  uint16                           IsCurrent;
};
```

## Members

The **Msvm\_NetworkElementSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_NetworkElementSettingData** class has these properties.

<dl> <dt>

**IsCurrent**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the referenced setting is currently being used in the operation of the element or that this information is unknown. For a given managed element and all instances of a setting data subclass, there shall be at most one instance of ElementSettingData which references the managed element and an instance of the setting data subclass where there is a specified non-null, non-key property of the setting data subclass, and the **IsMaximum** property on the referencing element setting data instance has a value of "Is Maximum" or the **IsMinimum** property on the referencing element setting data instance has a value of "Is Minimum" and the **IsCurrent** property on the referencing element setting data instance has a value of "Is Current". There shall be at most one instance of element setting data which references a managed element and an instance of a setting data subclass where the **IsCurrent** property has a value of "Is Current" and the **IsMinimum** property does not have a value of "Is Minimum" and the **IsMaximum** property does not have a value of "Is Maximum". This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053).

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

This property affects the interpretation of all non-null, non-enumerated, non-binary, numeric, non-key properties of the associated setting data instance. All other properties of the associated setting data instance are not affected by this property. Note: It is assumed that the semantics of each property of this set are designed to be compared mathematically. When **IsMaximum** = "Is Maximum", this property indicates whether the affected property values specified in the associated setting data instance shall define maximum setting values. When **IsMaximum** = "Is Not Maximum", this property indicates whether the affected property values specified in the associated setting data instance shall not define maximum setting values. When **IsMaximum** = "Unknown", this property indicates whether the affected property values specified in the associated setting data instance may correspond to maximum setting values. When **IsMaximum** = "Not Applicable", this property indicates whether the affected property values specified in the associated setting data instance shall not be interpreted with respect to whether each defines a maximum. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053) and is always set to 0.

</dd> <dt>

**IsMinimum**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

This property affects the interpretation of all non-null, non-enumerated, non-binary, numeric, non-key properties of the associated setting data instance. All other properties of the associated setting data instance are not affected by this property. Note: It is assumed that the semantics of each property of this set are designed to be compared mathematically. When **IsMinimum** = "Is Minimum", this property indicates whether the affected property values specified in the associated setting data instance shall define minimum setting values. When **IsMinimum** = "Is Not Minimum", this property indicates whether the affected property values specified in the associated setting data instance shall not define minimum setting values. When **IsMinimum** = "Unknown", this property indicates whether the affected property values specified in the associated setting data instance may correspond to minimum setting values. When **IsMinimum** = "Not Applicable", this property indicates whether the affected property values specified in the associated setting data instance shall not be interpreted with respect to whether each defines a minimum. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053) and is always set to 0.

</dd> <dt>

**IsNext**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Indicates whether the referenced setting is the next setting to be applied. For example, the application could take place on a re-initialization, reset, reconfiguration request. This could be a permanent setting, or a setting used only one time, as indicated by the flag. If it is a permanent setting then the setting is applied every time the managed element reinitializes, until this flag is manually reset. However, if it is single use, then the flag is automatically cleared after the settings are applied. Also note that if this flag is specified (that is, set to value other than "Unknown"), then this takes precedence over any setting data that may have been specified as Default. For example: If the managed element is a computer system, and the value of this flag is "Is Next", then the setting will be effective next time the system resets. And, unless this flag is changed, it will persist for subsequent system resets. However, if this flag is set to "Is Next For Single Use", then this setting will only be used once and the flag would be reset after that to "Is Not Next". So, in the above example, if the system reboots in a quick succession, the setting will not be used at the second reboot. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053).

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

Data type: **Msvm\_VLANEndpoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("ManagedElement")
</dt> </dl>

The managed element. This will be a reference to an [**Msvm\_VLANEndpoint**](msvm-vlanendpoint.md) object. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053).

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_VLANEndpointSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("SettingData")
</dt> </dl>

The setting data object that is associated with the element. This will be a reference to an [**Msvm\_VLANEndpointSettingData**](msvm-vlanendpointsettingdata.md) object. This property is inherited from [**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053).

</dd> </dl>

## Remarks

Access to the **Msvm\_NetworkElementSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

See [Querying Networking Objects](querying-networking-objects.md).

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

[**CIM\_ElementSettingData**](cim-elementsettingdata.md)
</dt> <dt>

[**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053)
</dt> </dl>

 

 





