---
title: Win32\_PowerSettingDefineCapabilities class
description: Associates a power setting's definition data with the power setting definition.
ms.assetid: 36d9d206-5be4-4e8f-a3b0-c5c3cf53f012
keywords:
- Win32_PowerSettingDefineCapabilities class
- Win32_PowerSettingDefineCapabilities class, described
topic_type:
- apiref
api_name:
- Win32_PowerSettingDefineCapabilities
- Win32_PowerSettingDefineCapabilities.PartComponent
- Win32_PowerSettingDefineCapabilities.PropertyPolicy
- Win32_PowerSettingDefineCapabilities.ValueRole
- Win32_PowerSettingDefineCapabilities.ValueRange
- Win32_PowerSettingDefineCapabilities.GroupComponent
api_location:
- PowerWmiProvider.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_PowerSettingDefineCapabilities class

Associates a power setting's definition data with the power setting definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("PowerWmiProvider"), Dynamic]
class Win32_PowerSettingDefineCapabilities : CIM_SettingsDefineCapabilities
{
  CIM_SettingData              REF PartComponent;
  uint16                           PropertyPolicy = 0;
  uint16                           ValueRole;
  uint16                           ValueRange = 0;
  Win32_PowerSettingDefinition REF GroupComponent;
};
```

## Members

The **Win32\_PowerSettingDefineCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PowerSettingDefineCapabilities** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PowerSettingDefinition**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The **InstanceID** of the power setting definition.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SettingData**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the **InstanceID** of the power setting definition data object. This is either a [**Win32\_PowerSettingDefinitionPossibleValue**](win32-powersettingdefinitionpossiblevalue.md) or [**Win32\_PowerSettingDefinitionRangeData**](win32-powersettingdefinitionrangedata.md) object.

</dd> <dt>

**PropertyPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Defines whether the power setting data object associated is independent or correlated. In general, discrete values are independent and range values are correlated.

<dl> <dt>

<span id="Independent"></span><span id="independent"></span><span id="INDEPENDENT"></span>**Independent** (0)
</dt> <dt>

<span id="Correlated"></span><span id="correlated"></span><span id="CORRELATED"></span>**Correlated** (1)
</dt> </dl>

</dd> <dt>

**ValueRange**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Defines the semantics of the setting data. For more information about the possible values, see [**CIM\_SettingsDefineCapabilities**](https://msdn.microsoft.com/library/mt146257).

<dl> <dt>

<span id="Point"></span><span id="point"></span><span id="POINT"></span>**Point** (0)
</dt> <dt>

<span id="Minimum"></span><span id="minimum"></span><span id="MINIMUM"></span>**Minimum** (1)
</dt> <dt>

<span id="Maximum"></span><span id="maximum"></span><span id="MAXIMUM"></span>**Maximum** (2)
</dt> <dt>

<span id="Increment"></span><span id="increment"></span><span id="INCREMENT"></span>**Increment** (3)
</dt> </dl>

</dd> <dt>

**ValueRole**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Defines the role of the associated power setting data object. Only Supported (3) is valid.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                               |
| Namespace<br/>                | Root\\CIMV2\\power<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>PowerWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PowerWmiProvider.dll</dt> </dl> |



 

 





