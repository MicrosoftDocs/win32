---
title: Msvm\_SettingsDefineCapabilities class
description: Provides a link between the capabilities instance and the minimum, maximum, incremental, and default settings for a resource.
ms.assetid: 664bed96-6840-499e-a962-1db687227ea7
keywords:
- Msvm_SettingsDefineCapabilities class Hyper-V
- Msvm_SettingsDefineCapabilities class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_SettingsDefineCapabilities
- Msvm_SettingsDefineCapabilities.GroupComponent
- Msvm_SettingsDefineCapabilities.PartComponent
- Msvm_SettingsDefineCapabilities.PropertyPolicy
- Msvm_SettingsDefineCapabilities.ValueRole
- Msvm_SettingsDefineCapabilities.ValueRange
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

# Msvm\_SettingsDefineCapabilities class

Provides a link between the capabilities instance and the minimum, maximum, incremental, and default settings for a resource.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SettingsDefineCapabilities : CIM_SettingsDefineCapabilities
{
  CIM_Capabilities REF GroupComponent;
  CIM_SettingData  REF PartComponent;
  uint16               PropertyPolicy = 0;
  uint16               ValueRole;
  uint16               ValueRange;
};
```

## Members

The **Msvm\_SettingsDefineCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_SettingsDefineCapabilities** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_Capabilities**](cim-capabilities.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A reference to the [**CIM\_Capabilities**](cim-capabilities.md) instance.

This property is inherited from [**CIM\_SettingsDefineCapabilities**](cim-settingsdefinecapabilities.md).

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_SettingData**](cim-settingdata.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to the [**CIM\_SettingData**](cim-settingdata.md) instance used to define the [**CIM\_Capabilities**](cim-capabilities.md) instance.

This property is inherited from [**CIM\_SettingsDefineCapabilities**](cim-settingsdefinecapabilities.md).

</dd> <dt>

**PropertyPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_SettingsDefineCapabilities**](cim-settingsdefinecapabilities.md).**ValueRole**", "**CIM\_SettingsDefineCapabilities**.**ValueRange**")
</dt> </dl>

Indicates whether the non-null, non-key properties of the associated [**CIM\_SettingData**](cim-settingdata.md) instance are treated independently or as a correlated set. For instance, an independent set of maximum properties might be defined when there is no relationship between each property. In contrast, several correlated sets of maximum properties might need to be defined when the maximum values of each are dependent on some of the others.

This property is always set to 0 (Independent).

This property is inherited from [**CIM\_SettingsDefineCapabilities**](cim-settingsdefinecapabilities.md).

</dd> <dt>

**ValueRange**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_SettingsDefineCapabilities**](cim-settingsdefinecapabilities.md).**PropertyPolicy**", "**CIM\_SettingsDefineCapabilities**.**ValueRole**")
</dt> </dl>

Indicates the type of value range used by properties of the non-null, non-key properties of the [**CIM\_SettingData**](cim-settingdata.md) instance.

This property is inherited from [**CIM\_SettingsDefineCapabilities**](cim-settingsdefinecapabilities.md).

The possible values are:

<dt>

<span id="Point"></span><span id="point"></span><span id="POINT"></span>

**Point** (0)


</dt> <dd></dd> <dt>

<span id="Minimums"></span><span id="minimums"></span><span id="MINIMUMS"></span>

**Minimums** (1)


</dt> <dd></dd> <dt>

<span id="Maximums"></span><span id="maximums"></span><span id="MAXIMUMS"></span>

**Maximums** (2)


</dt> <dd></dd> <dt>

<span id="Increments"></span><span id="increments"></span><span id="INCREMENTS"></span>

**Increments** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 65535</dd> </dl>

</dd> <dt>

**ValueRole**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_SettingsDefineCapabilities**](cim-settingsdefinecapabilities.md).**PropertyPolicy**", "**CIM\_SettingsDefineCapabilities**.**ValueRange**")
</dt> </dl>

The additional semantics for the interpretation of the non-null, non-key properties of the [**CIM\_SettingData**](cim-settingdata.md) instance.

This property is inherited from [**CIM\_SettingsDefineCapabilities**](cim-settingsdefinecapabilities.md).

The possible values are:

<dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>**Default** (0)


</dt> <dd>

The property values will be used as default values when a new [**CIM\_SettingData**](cim-settingdata.md) instance is created.

</dd> <dt>

<span id="Optimal"></span><span id="optimal"></span><span id="OPTIMAL"></span>

<span id="Optimal"></span><span id="optimal"></span><span id="OPTIMAL"></span>**Optimal** (1)


</dt> <dd>

The [**CIM\_SettingData**](cim-settingdata.md) instance represents optimal setting values.

</dd> <dt>

<span id="Mean"></span><span id="mean"></span><span id="MEAN"></span>

<span id="Mean"></span><span id="mean"></span><span id="MEAN"></span>**Mean** (2)


</dt> <dd>

Non-null, non-key, non-enumerated, non-boolean, numeric properties of the [**CIM\_SettingData**](cim-settingdata.md) instance represent an average point along a dimension.

</dd> <dt>

<span id="Supported"></span><span id="supported"></span><span id="SUPPORTED"></span>

<span id="Supported"></span><span id="supported"></span><span id="SUPPORTED"></span>**Supported** (3)


</dt> <dd>

The non-null, non-key properties of the [**CIM\_SettingData**](cim-settingdata.md) instance represent a set of supported property values that have not been qualified.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> </dl>

</dd> </dl>

## Remarks

The values for the **ValueRole** and **ValueRange** properties are used in the following pairs:

-   Point/Default (0/0)
-   Minimums/Supported (1/3)
-   Maximums/Supported (2/3)
-   Increments/Supported (3/3).

"Point" means that each of the properties on the **PartComponent** object represents the platform default.

"Minimums" and "Maximums" mean that each of the properties on the **PartComponent** object represent the smallest and largest possible values for these properties that are supported by the platform based on your current machine configuration.

"Increments" indicates the granularity at which you can increase or decrease the settings.

Access to the **Msvm\_SettingsDefineCapabilities** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_SettingsDefineCapabilities**](cim-settingsdefinecapabilities.md)
</dt> <dt>

[**CIM\_SettingsDefineCapabilities**](https://msdn.microsoft.com/library/mt146257)
</dt> <dt>

[**Msvm\_SettingsDefineCapabilities (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850211)
</dt> <dt>

[Resource Management Classes](resource-management-classes.md)
</dt> </dl>

 

 





