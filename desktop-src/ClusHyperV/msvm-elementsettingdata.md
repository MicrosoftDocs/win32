---
title: Msvm\_ElementSettingData class
description: Associates a managed element with its configuration data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cc55bd87-f97a-4a8e-b8e6-ec94a53e99e1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Msvm_ElementSettingData class", "Msvm_ElementSettingData class, described"]
topic_type:
- apiref
api_name:
- Msvm_ElementSettingData
- Msvm_ElementSettingData.ManagedElement
- Msvm_ElementSettingData.SettingData
- Msvm_ElementSettingData.IsDefault
- Msvm_ElementSettingData.IsCurrent
- Msvm_ElementSettingData.IsNext
api_location:
- VMMS.exe
api_type:
- DllExport
---

# Msvm\_ElementSettingData class

Associates a managed element with its configuration data.

This association is often used to link a virtual computer system and the logical devices that have been assigned to that system with their snapshot configuration information. Current configuration information is associated with a virtual system and its devices through the [**Msvm\_SettingsDefineState**](msvm-settingsdefinestate.md) association.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ElementSettingData : CIM_ElementSettingData
{
  CIM_ManagedElement REF ManagedElement;
  CIM_SettingData    REF SettingData;
  uint16                 IsDefault;
  uint16                 IsCurrent;
  uint16                 IsNext;
};
```

## Members

The **Msvm\_ElementSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ElementSettingData** class has these properties.

<dl> <dt>

**IsCurrent**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the referenced setting is currently being used by the element.

This property is inherited from [**CIM\_ElementSettingData**](cim-elementsettingdata.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

"Unknown"

</dd> <dt>

<span id="Is_Current"></span><span id="is_current"></span><span id="IS_CURRENT"></span>

<span id="Is_Current"></span><span id="is_current"></span><span id="IS_CURRENT"></span>**Is Current** (1)


</dt> <dd>

"Is Current"

</dd> <dt>

<span id="Is_Not_Current"></span><span id="is_not_current"></span><span id="IS_NOT_CURRENT"></span>

<span id="Is_Not_Current"></span><span id="is_not_current"></span><span id="IS_NOT_CURRENT"></span>**Is Not Current** (2)


</dt> <dd>

"Is Not Current"

</dd> </dl>

</dd> <dt>

**IsDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicating whether the setting is a default setting for the element.

This property is inherited from [**CIM\_ElementSettingData**](cim-elementsettingdata.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

"Unknown"

</dd> <dt>

<span id="Is_Default"></span><span id="is_default"></span><span id="IS_DEFAULT"></span>

<span id="Is_Default"></span><span id="is_default"></span><span id="IS_DEFAULT"></span>**Is Default** (1)


</dt> <dd>

"Is Default"

</dd> <dt>

<span id="Is_Not_Default"></span><span id="is_not_default"></span><span id="IS_NOT_DEFAULT"></span>

<span id="Is_Not_Default"></span><span id="is_not_default"></span><span id="IS_NOT_DEFAULT"></span>**Is Not Default** (2)


</dt> <dd>

"Is Not Default"

</dd> </dl>

</dd> <dt>

**IsNext**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A flag that indicates when and how often to apply the setting.

For example, the setting could be applied on a re-initialization, reset, reconfiguration request. This could be a permanent setting, or a setting used only one time, as indicated by the flag. If it is a permanent setting then the setting is applied every time the managed element reinitializes, until this flag is manually reset. However, if it is single use, then the flag is automatically cleared after the settings are applied. In addition, if this flag is set to value other than 0 (Unknown), then this takes precedence over a **SettingData** property that is set to "Default".

If the managed element is a computer system, and the value of this flag is "Is Next", then the setting will be effective next time the system resets. And, unless this flag is changed, it will persist for subsequent system resets. However, if this flag is set to "Is Next For Single Use", then this setting will only be used once and the flag would be reset after that to 2 (Is Not Next). So, in the above example, if the system reboots in a quick succession, the setting will not be used at the second reboot.

This property is inherited from [**CIM\_ElementSettingData**](cim-elementsettingdata.md).

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

The setting will only be applied to the managed element once, and then this flag will be set to 2 (Is Not Next).

</dd> </dl>

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The managed element.

This property is inherited from [**CIM\_ElementSettingData**](cim-elementsettingdata.md).

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The setting data associated with the element.

This property is inherited from [**CIM\_ElementSettingData**](cim-elementsettingdata.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_ElementSettingData**](cim-elementsettingdata.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





