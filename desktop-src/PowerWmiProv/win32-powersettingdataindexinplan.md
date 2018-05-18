---
title: Win32\_PowerSettingDataIndexInPlan class
description: Represents the association between the power plan and the power setting data index.
ms.assetid: 'bb799299-998b-4a8c-9610-0312b2cd5d18'
keywords: ["Win32_PowerSettingDataIndexInPlan class", "Win32_PowerSettingDataIndexInPlan class, described"]
topic_type:
- apiref
api_name:
- Win32_PowerSettingDataIndexInPlan
- Win32_PowerSettingDataIndexInPlan.GroupComponent
- Win32_PowerSettingDataIndexInPlan.PartComponent
api_location:
- PowerWmiProvider.dll
api_type:
- DllExport
---

# Win32\_PowerSettingDataIndexInPlan class

Represents the association between the power plan and the power setting data index.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("PowerWmiProvider"), Dynamic]
class Win32_PowerSettingDataIndexInPlan : CIM_ConcreteComponent
{
  Win32_PowerPlan             REF GroupComponent;
  Win32_PowerSettingDataIndex REF PartComponent;
};
```

## Members

The **Win32\_PowerSettingDataIndexInPlan** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PowerSettingDataIndexInPlan** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PowerPlan**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The **InstanceID** of the power plan.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PowerSettingDataIndex**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The **InstanceID** power setting data index.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                               |
| Namespace<br/>                | Root\\CIMV2\\power<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>PowerWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PowerWmiProvider.dll</dt> </dl> |



 

 





