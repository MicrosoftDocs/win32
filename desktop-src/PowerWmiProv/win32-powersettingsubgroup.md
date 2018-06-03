---
title: Win32\_PowerSettingSubgroup class
description: Represents a power setting subgroup in the system.
ms.assetid: defe65c5-6c2d-43ad-bbd5-965c62bdd4ad
keywords:
- Win32_PowerSettingSubgroup class
- Win32_PowerSettingSubgroup class, described
topic_type:
- apiref
api_name:
- Win32_PowerSettingSubgroup
- Win32_PowerSettingSubgroup.Description
- Win32_PowerSettingSubgroup.InstanceID
- Win32_PowerSettingSubgroup.ElementName
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

# Win32\_PowerSettingSubgroup class

Represents a power setting subgroup in the system. A power setting subgroup is a logical grouping for power settings. Subgroups provide an organizational structure for grouping settings. All power settings belong to only one subgroup. Settings that are not formally grouped belong to the "No SubGroup" group. An instance of **Win32\_PowerSettingSubgroup** is created for each power subgroup defined, including the special "No SubGroup" group.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("PowerWmiProvider"), Dynamic]
class Win32_PowerSettingSubgroup : CIM_SettingData
{
  string Description;
  string InstanceID;
  string ElementName;
};
```

## Members

The **Win32\_PowerSettingSubgroup** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PowerSettingSubgroup** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the description of the power subgroup.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the friendly name of the power subgroup.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the **GUID** that represents the power subgroup.

The **InstanceID** string must be in the following format: "Microsoft:PowerSettingSubgroup\\{Subgroup\_GUID}".

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                               |
| Namespace<br/>                | Root\\CIMV2\\power<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>PowerWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PowerWmiProvider.dll</dt> </dl> |



 

 





