---
title: MDM\_Restrictions class
description: Represents the configuration of restrictions on the device.
ms.assetid: b7766fe4-726f-4d4a-806d-49997cec8301
keywords:
- MDM_Restrictions class MDM Settings
- MDM_Restrictions class MDM Settings , described
topic_type:
- apiref
api_name:
- MDM_Restrictions
- MDM_Restrictions.Key
- MDM_Restrictions.DiagnosticsSubmissionEnabled
- MDM_Restrictions.DataRoamingEnabled
- MDM_Restrictions.BluetoothEnabled
- MDM_Restrictions.WifiEnabled
- MDM_Restrictions.PCSettingsSyncEnabled
- MDM_Restrictions.PCSettingsMeteredNetworkSyncEnabled
- MDM_Restrictions.PCSettingsPasswordSyncEnabled
- MDM_Restrictions.EcsSyncUrl
- MDM_Restrictions.EcsAutoProvisionEnabled
- MDM_Restrictions.UserAccountControlStatus
- MDM_Restrictions.SmartScreenEnabled
- MDM_Restrictions.IEEnterpriseModeEnabled
- MDM_Restrictions.IEEnterpriseModeEnabledURL
- MDM_Restrictions.IEEnterpriseModeSitelist
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

# MDM\_Restrictions class

Represents the configuration of restrictions on the device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_Restrictions
{
  Uint32  Key;
  boolean DiagnosticsSubmissionEnabled;
  boolean DataRoamingEnabled;
  boolean BluetoothEnabled;
  boolean WifiEnabled;
  boolean PCSettingsSyncEnabled;
  boolean PCSettingsMeteredNetworkSyncEnabled;
  boolean PCSettingsPasswordSyncEnabled;
  string  EcsSyncUrl;
  boolean EcsAutoProvisionEnabled;
  Uint32  UserAccountControlStatus;
  boolean SmartScreenEnabled;
  boolean IEEnterpriseModeEnabled;
  string  IEEnterpriseModeEnabledURL;
  string  IEEnterpriseModeSitelist;
};
```

## Members

The **MDM\_Restrictions** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Restrictions** class has these properties.

<dl> <dt>

**BluetoothEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if at least one Bluetooth device is found and is enabled on the device.

</dd> <dt>

**DataRoamingEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if *Data Roaming* is enabled on the device.

</dd> <dt>

**DiagnosticsSubmissionEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if *Windows Error Reporting* is enabled on the device.

</dd> <dt>

**EcsAutoProvisionEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the Enterprise Client Sync product is auto-provisioned.

</dd> <dt>

**EcsSyncUrl**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The URL of the Enterprise Client Sync product to which the client syncs.

</dd> <dt>

**IEEnterpriseModeEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if Internet Explorer Enterprise Mode is enabled.

**Windows 8.1:** This property is not supported before Windows 8.1 Update.

</dd> <dt>

**IEEnterpriseModeEnabledURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Internet Explorer Enterprise Mode Reporting URL specified while enabling the value. For more information see [Turn on Enterprise Mode and use a site list](https://technet.microsoft.com/library/dn640699.aspx).

**Windows 8.1:** This property is not supported before Windows 8.1 Update.

</dd> <dt>

**IEEnterpriseModeSitelist**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Internet Explorer Enterprise Mode Reporting site list. For more information see [Add multiple sites to the Enterprise Mode site list using a file and Enterprise Mode Site List Manager](https://technet.microsoft.com/library/dn640696.aspx).

**Windows 8.1:** This property is not supported before Windows 8.1 Update.

</dd> <dt>

**Key**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the **MDM\_Restrictions** class instance.

</dd> <dt>

**PCSettingsMeteredNetworkSyncEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the **Sync settings over metered connection** option under **Change Settings** is turned on.

</dd> <dt>

**PCSettingsPasswordSyncEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the **Passwords** option under **Change Settings** is turned on.

</dd> <dt>

**PCSettingsSyncEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the **Sync your settings** option under **Change Settings** is turned on.

</dd> <dt>

**SmartScreenEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if *Smart Screen* is enabled.

</dd> <dt>

**UserAccountControlStatus**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current *User Access Control* level on the client.

<dt>

<span id="Always_Notify"></span><span id="always_notify"></span><span id="ALWAYS_NOTIFY"></span>

**Always Notify** (0)


</dt> <dd></dd> <dt>

<span id="Notify_App_Changes"></span><span id="notify_app_changes"></span><span id="NOTIFY_APP_CHANGES"></span>

**Notify App Changes** (1)


</dt> <dd></dd> <dt>

<span id="Notify_App_Changes__No_Dim_"></span><span id="notify_app_changes__no_dim_"></span><span id="NOTIFY_APP_CHANGES__NO_DIM_"></span>

**Notify App Changes (No Dim)** (2)


</dt> <dd></dd> <dt>

<span id="Never_Notify"></span><span id="never_notify"></span><span id="NEVER_NOTIFY"></span>

**Never Notify** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**WifiEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if at least one enabled wireless network adapter is found on the device.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                         |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





