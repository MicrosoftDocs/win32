---
title: Win32\_PowerSettingDataIndex class
description: Represents the setting data index value for a power setting in the system.
ms.assetid: '39da9e54-165c-46ae-a9f5-e1118579eaf4'
keywords: ["Win32_PowerSettingDataIndex class", "Win32_PowerSettingDataIndex class, described"]
topic_type:
- apiref
api_name:
- Win32_PowerSettingDataIndex
- Win32_PowerSettingDataIndex.InstanceID
- Win32_PowerSettingDataIndex.SettingIndexValue
api_location:
- PowerWmiProvider.dll
api_type:
- DllExport
---

# Win32\_PowerSettingDataIndex class

Represents the setting data index value for a power setting in the system. A power setting data index value instance represents the actual AC or DC value for a given power setting. Two instances of this class are created for each power setting; one represents the AC value and the other represents the DC value. On systems that have only AC power, the DC values will be absent. The **InstanceID** property indicates whether the setting applies to AC or DC. Power setting values are associated with power plans through the [**Win32\_PowerSettingDataIndexInPlan**](win32-powersettingdataindexinplan.md) class. Each power setting is also associated with its power setting definition, represented by the [**Win32\_PowerSettingDefinition**](win32-powersettingdefinition.md) class, via the [**Win32\_PowerSettingDefineCapabilities**](win32-powersettingdefinecapabilities.md) association.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("PowerWmiProvider"), Dynamic]
class Win32_PowerSettingDataIndex : CIM_SettingData
{
  string InstanceID;
  uint32 SettingIndexValue;
};
```

## Members

The **Win32\_PowerSettingDataIndex** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PowerSettingDataIndex** class has these properties.

<dl> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the unique identifier for the power setting data index instance.

The **InstanceID** string must be in the following format: "Microsoft:PowerSettingDataIndex\\{Plan\_GUID}\\\\{AC\|DC\\\\{DataIndex\_GUID}". The {Plan\_GUID} portion of the string corresponds to the GUID of the power plan, the {AC\|DC} portion corresponds to either the AC or DC value, and the {DataIndex\_GUID) portion corresponds to the unique GUID of the power setting data index.

</dd> <dt>

**SettingIndexValue**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the value for the power setting.

</dd> </dl>

## Remarks

Setting a power setting value that is associated with the active power scheme does not automatically make the power setting value take effect on the system. Instead, the [**Win32\_PowerPlan.Activate**](activate-win32-powerplan.md) method must be called to activate the new settings.

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



 

 





