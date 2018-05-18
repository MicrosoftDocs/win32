---
title: Win32\_PowerPlan class
description: Represents a power plan on a system.
ms.assetid: '86069bd7-8a3f-47d1-abdc-292e8ebf3bad'
keywords: ["Win32_PowerPlan class", "Win32_PowerPlan class, described"]
topic_type:
- apiref
api_name:
- Win32_PowerPlan
- Win32_PowerPlan.InstanceID
- Win32_PowerPlan.ElementName
- Win32_PowerPlan.Description
- Win32_PowerPlan.IsActive
api_location:
- PowerWmiProvider.dll
api_type:
- DllExport
---

# Win32\_PowerPlan class

Represents a power plan on a system. A power plan or scheme consists of a group of power settings and preference information. Each power plan is identified through a unique GUID as well as by a friendly name. Windows power plans also have a personality attribute that indicates the overall power savings behavior of the plan. Multiple power plans can exist; however, each computer can have only a single active power plan in effect at any given time.

A WMI consumer can enumerate all instances of **Win32\_PowerPlan** to get all the power schemes that currently exist on the system. The active **Win32\_PowerPlan** can be obtained by examining the **IsActive** property on the instance. The [**Activate**](activate-win32-powerplan.md) method will make the power plan the active plan on the system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("PowerWmiProvider"), Dynamic]
class Win32_PowerPlan : CIM_SettingData
{
  string  InstanceID;
  string  ElementName;
  string  Description;
  boolean IsActive;
};
```

## Members

The **Win32\_PowerPlan** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_PowerPlan** class has these methods.



| Method                                       | Description                                                     |
|:---------------------------------------------|:----------------------------------------------------------------|
| [**Activate**](activate-win32-powerplan.md) | Makes the power scheme the active one on the system.<br/> |



 

### Properties

The **Win32\_PowerPlan** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the description of the power plan.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the friendly name of the power plan.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Defines the unique identifier for the power plan instance.

The **InstanceID** string must be in the following format: "Microsoft:PowerPlan\\{Plan\_GUID}".

</dd> <dt>

**IsActive**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the power scheme is currently active on the system. This property is set to **TRUE** if the power scheme is active; otherwise, it is set to **FALSE**.

</dd> </dl>

## Examples

The following PowerShell code example displays the power settings of the local computer.


```PowerShell
$powerplan=get-wmiobject -namespace "root\cimv2\power" -class Win32_powerplan | where {$_.IsActive}

$powerSettings = $powerplan.GetRelated("win32_powersettingdataindex") | foreach {
 $powersettingindex = $_;

 $powersettingindex.GetRelated("Win32_powersetting") | select @{Label="Power Setting";Expression={$_.instanceid}},
 @{Label="AC/DC";Expression={$powersettingindex.instanceid.split("\")[2]}},
 @{Label="Summary";Expression={$_.ElementName}},
 @{Label="Description";Expression={$_.description}},
 @{Label="Value";Expression={$powersettingindex.settingindexvalue}}
 }

$powerSettings | ft "AC/DC",Summary,Value -autosize
```



## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                               |
| Namespace<br/>                | Root\\CIMV2\\power<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>PowerWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PowerWmiProvider.dll</dt> </dl> |



 

 





