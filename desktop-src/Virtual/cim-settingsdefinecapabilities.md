---
title: CIM\_SettingsDefineCapabilities class
description: Represents an association between properties of a CIM\_SettingData instance and a CIM\_Capabilities instance.
ms.assetid: f4967050-21c0-4506-b0d2-b5449c16f405
keywords:
- CIM_SettingsDefineCapabilities class Hyper-V
- CIM_SettingsDefineCapabilities class Hyper-V , described
topic_type:
- apiref
api_name:
- CIM_SettingsDefineCapabilities
- CIM_SettingsDefineCapabilities.GroupComponent
- CIM_SettingsDefineCapabilities.PartComponent
- CIM_SettingsDefineCapabilities.PropertyPolicy
- CIM_SettingsDefineCapabilities.ValueRole
- CIM_SettingsDefineCapabilities.ValueRange
api_location:
- Root\virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CIM\_SettingsDefineCapabilities class

Represents an association between properties of a [**CIM\_SettingData**](cim-settingdata.md) instance and a [**CIM\_Capabilities**](cim-capabilities.md) instance. In the association, specific non-NULL, non-key properties are associated with some of the capabilities of the [**CIM\_Capabilities**](cim-capabilities.md) instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Experimental, Aggregation, Composition, Version("2.12"), AMENDMENT]
class CIM_SettingsDefineCapabilities : CIM_Component
{
  CIM_Capabilities REF GroupComponent;
  CIM_SettingData  REF PartComponent;
  uint16               PropertyPolicy;
  uint16               ValueRole;
  uint16               ValueRange;
};
```

## Members

The **CIM\_SettingsDefineCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SettingsDefineCapabilities** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_Capabilities**](cim-capabilities.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A reference to the [**CIM\_Capabilities**](cim-capabilities.md) instance.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_SettingData**](cim-settingdata.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

A reference to the [**CIM\_SettingData**](cim-settingdata.md) instance used to define the [**CIM\_Capabilities**](cim-capabilities.md) instance.

</dd> <dt>

**PropertyPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_SettingsDefineCapabilities**.**ValueRole**", "**CIM\_SettingsDefineCapabilities**.**ValueRange**")
</dt> </dl>

Indicates whether the non-null, non-key properties of the associated [**CIM\_SettingData**](cim-settingdata.md) instance are treated independently or as a correlated set. For instance, an independent set of maximum properties might be defined when there is no relationship between each property. In contrast, several correlated sets of maximum properties might need to be defined when the maximum values of each are dependent on some of the others.

The possible values are:

<dt>

<span id="Independent"></span><span id="independent"></span><span id="INDEPENDENT"></span>

**Independent** (0)


</dt> <dd></dd> <dt>

<span id="Correlated"></span><span id="correlated"></span><span id="CORRELATED"></span>

**Correlated** (1)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>2 65535</dd> </dl>

</dd> <dt>

**ValueRange**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_SettingsDefineCapabilities**.**PropertyPolicy**", "**CIM\_SettingsDefineCapabilities**.**ValueRole**")
</dt> </dl>

Indicates the type of value range used by properties of the non-null, non-key properties of the [**CIM\_SettingData**](cim-settingdata.md) instance.

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

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_SettingsDefineCapabilities**.**PropertyPolicy**", "**CIM\_SettingsDefineCapabilities**.**ValueRange**")
</dt> </dl>

The additional semantics for the interpretation of the non-null, non-key properties of the [**CIM\_SettingData**](cim-settingdata.md) instance.

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

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> </dl>

 

 





