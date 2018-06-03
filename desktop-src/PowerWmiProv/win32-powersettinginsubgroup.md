---
title: Win32\_PowerSettingInSubgroup class
description: Represents the association between the power setting and a subgroup. An instance of Win32\_PowerSettingInSubgroup is created for each power setting.
ms.assetid: 7bbb47ec-c1c5-4fc9-a90a-0c2a1ab25bc5
keywords:
- Win32_PowerSettingInSubgroup class
- Win32_PowerSettingInSubgroup class, described
topic_type:
- apiref
api_name:
- Win32_PowerSettingInSubgroup
- Win32_PowerSettingInSubgroup.GroupComponent
- Win32_PowerSettingInSubgroup.PartComponent
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

# Win32\_PowerSettingInSubgroup class

Represents the association between the power setting and a subgroup. An instance of **Win32\_PowerSettingInSubgroup** is created for each power setting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("PowerWmiProvider"), Dynamic]
class Win32_PowerSettingInSubgroup : CIM_ConcreteComponent
{
  Win32_PowerSettingSubgroup REF GroupComponent;
  Win32_PowerSetting         REF PartComponent;
};
```

## Members

The **Win32\_PowerSettingInSubgroup** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PowerSettingInSubgroup** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PowerSettingSubgroup**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The **InstanceID** of the subgroup.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PowerSetting**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The **InstanceID** of the power setting.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                               |
| Namespace<br/>                | Root\\CIMV2\\power<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>PowerWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PowerWmiProvider.dll</dt> </dl> |



 

 





