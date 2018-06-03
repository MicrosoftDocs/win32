---
title: MDM\_SecurityStatus class
description: Represents security health metrics on the device.
ms.assetid: 362e011a-aab7-4021-bf81-f589564e31ac
keywords:
- MDM_SecurityStatus class MDM Settings
- MDM_SecurityStatus class MDM Settings , described
topic_type:
- apiref
api_name:
- MDM_SecurityStatus
- MDM_SecurityStatus.Key
- MDM_SecurityStatus.FirewallStatus
- MDM_SecurityStatus.AutoUpdateStatus
- MDM_SecurityStatus.AntiVirusStatus
- MDM_SecurityStatus.AntiVirusSignatureStatus
- MDM_SecurityStatus.RequireEncryption
- MDM_SecurityStatus.MaintenanceScheduleStartHour
- MDM_SecurityStatus.MaintenanceScheduleDelayPattern
- MDM_SecurityStatus.MaintenanceScheduleAllowWakeup
- MDM_SecurityStatus.IsMicrosoftAccountOptional
- MDM_SecurityStatus.ApplicationContentUriRules
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MDM\_SecurityStatus class

Represents security health metrics on the device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_SecurityStatus
{
  Uint32  Key;
  Uint32  FirewallStatus;
  Uint32  AutoUpdateStatus;
  Uint32  AntiVirusStatus;
  Uint32  AntiVirusSignatureStatus;
  boolean RequireEncryption;
  Uint32  MaintenanceScheduleStartHour;
  string  MaintenanceScheduleDelayPattern;
  boolean MaintenanceScheduleAllowWakeup;
  boolean IsMicrosoftAccountOptional;
  string  ApplicationContentUriRules;
};
```

## Members

The **MDM\_SecurityStatus** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_SecurityStatus** class has these properties.

<dl> <dt>

**AntiVirusSignatureStatus**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the antivirus signature file.

<dt>

<span id="On"></span><span id="on"></span><span id="ON"></span>

**On** (0)


</dt> <dd></dd> <dt>

<span id="Off"></span><span id="off"></span><span id="OFF"></span>

**Off** (1)


</dt> <dd></dd> <dt>

<span id="Snoozed"></span><span id="snoozed"></span><span id="SNOOZED"></span>

**Snoozed** (2)


</dt> <dd></dd> <dt>

<span id="Expired"></span><span id="expired"></span><span id="EXPIRED"></span>

**Expired** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**AntiVirusStatus**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the antivirus application.

<dt>

<span id="Good"></span><span id="good"></span><span id="GOOD"></span>

**Good** (0)


</dt> <dd></dd> <dt>

<span id="NotMonitored"></span><span id="notmonitored"></span><span id="NOTMONITORED"></span>

**NotMonitored** (1)


</dt> <dd></dd> <dt>

<span id="Poor"></span><span id="poor"></span><span id="POOR"></span>

**Poor** (2)


</dt> <dd></dd> <dt>

<span id="Snooze"></span><span id="snooze"></span><span id="SNOOZE"></span>

**Snooze** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**ApplicationContentUriRules**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Windows 8:** This property is supported beginning with Windows 8.1.

The application content URI rules. For example, "https://mail.microsoft.com/owa".

</dd> <dt>

**AutoUpdateStatus**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of Windows Update.

<dt>

<span id="Disable_Automatic_Updates"></span><span id="disable_automatic_updates"></span><span id="DISABLE_AUTOMATIC_UPDATES"></span>

**Disable Automatic Updates** (0)


</dt> <dd></dd> <dt>

<span id="Notify_for_download_and_notify_for_install"></span><span id="notify_for_download_and_notify_for_install"></span><span id="NOTIFY_FOR_DOWNLOAD_AND_NOTIFY_FOR_INSTALL"></span>

**Notify for download and notify for install** (1)


</dt> <dd></dd> <dt>

<span id="Auto_download_and_notify_for_install"></span><span id="auto_download_and_notify_for_install"></span><span id="AUTO_DOWNLOAD_AND_NOTIFY_FOR_INSTALL"></span>

**Auto download and notify for install** (2)


</dt> <dd></dd> <dt>

<span id="Auto_download_and_schedule_the_install"></span><span id="auto_download_and_schedule_the_install"></span><span id="AUTO_DOWNLOAD_AND_SCHEDULE_THE_INSTALL"></span>

**Auto download and schedule the install** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**FirewallStatus**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the firewall.

<dt>

<span id="Good"></span><span id="good"></span><span id="GOOD"></span>

**Good** (0)


</dt> <dd></dd> <dt>

<span id="NotMonitored"></span><span id="notmonitored"></span><span id="NOTMONITORED"></span>

**NotMonitored** (1)


</dt> <dd></dd> <dt>

<span id="Poor"></span><span id="poor"></span><span id="POOR"></span>

**Poor** (2)


</dt> <dd></dd> <dt>

<span id="Snooze"></span><span id="snooze"></span><span id="SNOOZE"></span>

**Snooze** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**IsMicrosoftAccountOptional**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Windows 8:** This property is supported beginning with Windows 8.1.

True if Microsoft accounts are optional to use modern applications.

</dd> <dt>

**Key**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the **MDM\_SecurityStatus** class instance.

</dd> <dt>

**MaintenanceScheduleAllowWakeup**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Windows 8:** This property is supported beginning with Windows 8.1.

True if to wake up the machine to start maintenance.

</dd> <dt>

**MaintenanceScheduleDelayPattern**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Windows 8:** This property is supported beginning with Windows 8.1.

The maintenance window start delay pattern. For example, "PT30M".

</dd> <dt>

**MaintenanceScheduleStartHour**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Windows 8:** This property is supported beginning with Windows 8.1.

The maintenance window start hour.

The possible values are.

Range: 0 23

</dd> <dt>

**RequireEncryption**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if BitLocker encryption is required.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





