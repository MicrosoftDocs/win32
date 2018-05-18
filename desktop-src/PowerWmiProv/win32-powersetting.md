---
title: Win32\_PowerSetting class
description: Represents a power setting on the system.
ms.assetid: 'd09061dd-b7df-4595-b941-0d564e862d80'
keywords: ["Win32_PowerSetting class", "Win32_PowerSetting class, described"]
topic_type:
- apiref
api_name:
- Win32_PowerSetting
- Win32_PowerSetting.Description
- Win32_PowerSetting.InstanceID
- Win32_PowerSetting.ElementName
api_location:
- PowerWmiProvider.dll
api_type:
- DllExport
---

# Win32\_PowerSetting class

Represents a power setting on the system. A power setting is a setting that controls some aspect of the power policy on the system, such as the display timeout, the idle-to-sleep timeout, or search indexing when idle. An instance of **Win32\_PowerSetting** is created for each power setting defined on the system. This object represents a Windows power policy setting and describes the basic metadata for a single power setting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("PowerWmiProvider"), Dynamic]
class Win32_PowerSetting : CIM_SettingData
{
  string Description;
  string InstanceID;
  string ElementName;
};
```

## Members

The **Win32\_PowerSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PowerSetting** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the description of the power setting.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the friendly name of the power setting.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the unique identifier for the power setting instance.

The **InstanceID** string must be in the following format: "Microsoft:PowerSetting\\{Setting\_GUID}".

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



 

 





