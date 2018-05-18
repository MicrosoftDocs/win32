---
title: MDM\_BrowserSettings class
description: Contains configuration information about browser security settings on the device.
ms.assetid: 'f119e8f7-0995-48ca-8b1f-a52ff9af199f'
keywords: ["MDM_BrowserSettings class MDM Settings", "MDM_BrowserSettings class MDM Settings , described"]
topic_type:
- apiref
api_name:
- MDM_BrowserSettings
- MDM_BrowserSettings.Key
- MDM_BrowserSettings.ForceFraudWarning
- MDM_BrowserSettings.AutofillEnabled
- MDM_BrowserSettings.InternetScriptingEnabled
- MDM_BrowserSettings.InternetPluginsEnabled
- MDM_BrowserSettings.InternetBlockPopups
- MDM_BrowserSettings.AlwaysSendDoNotTrackHeader
- MDM_BrowserSettings.IntranetSecurityZoneEnabled
- MDM_BrowserSettings.InternetProtectedModeEnabled
- MDM_BrowserSettings.GoToIntranetForSingleWord
- MDM_BrowserSettings.InternetZoneSecurityLevel
- MDM_BrowserSettings.IntranetZoneSecurityLevel
- MDM_BrowserSettings.RestrictedSitesZoneSecurityLevel
- MDM_BrowserSettings.TrustedSitesZoneSecurityLevel
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
---

# MDM\_BrowserSettings class

Contains configuration information about browser security settings on the device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_BrowserSettings
{
  Uint32  Key;
  boolean ForceFraudWarning;
  boolean AutofillEnabled;
  boolean InternetScriptingEnabled;
  boolean InternetPluginsEnabled;
  boolean InternetBlockPopups;
  boolean AlwaysSendDoNotTrackHeader;
  boolean IntranetSecurityZoneEnabled;
  boolean InternetProtectedModeEnabled;
  boolean GoToIntranetForSingleWord;
  Uint32  InternetZoneSecurityLevel;
  Uint32  IntranetZoneSecurityLevel;
  Uint32  RestrictedSitesZoneSecurityLevel;
  Uint32  TrustedSitesZoneSecurityLevel;
};
```

## Members

The **MDM\_BrowserSettings** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_BrowserSettings** class has these properties.

<dl> <dt>

**AlwaysSendDoNotTrackHeader**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the *Always send do not track header* setting is enabled.

</dd> <dt>

**AutofillEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if Auto fill is enabled.

</dd> <dt>

**ForceFraudWarning**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the Force fraud warning is enabled.

</dd> <dt>

**GoToIntranetForSingleWord**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the *Go to Intranet for single word* setting is enabled.

</dd> <dt>

**InternetBlockPopups**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if pop-up windows are disabled.

</dd> <dt>

**InternetPluginsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if plugins are enabled.

</dd> <dt>

**InternetProtectedModeEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the Internet protected mode is enabled.

</dd> <dt>

**InternetScriptingEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if Scripting is enabled for the Internet security zone.

</dd> <dt>

**InternetZoneSecurityLevel**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The security level for the Internet security zone.

Possible values are.

<dt>

<span id="Medium"></span><span id="medium"></span><span id="MEDIUM"></span>

**Medium** (3)


</dt> <dd></dd> <dt>

<span id="Medium-high"></span><span id="medium-high"></span><span id="MEDIUM-HIGH"></span>

**Medium-high** (4)


</dt> <dd></dd> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>

**High** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**IntranetSecurityZoneEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the Intranet security zone is enabled.

</dd> <dt>

**IntranetZoneSecurityLevel**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The security level for the Intranet security zone.

Possible values are.

<dt>

<span id="Low"></span><span id="low"></span><span id="LOW"></span>

**Low** (1)


</dt> <dd></dd> <dt>

<span id="Medium-low"></span><span id="medium-low"></span><span id="MEDIUM-LOW"></span>

**Medium-low** (2)


</dt> <dd></dd> <dt>

<span id="Medium"></span><span id="medium"></span><span id="MEDIUM"></span>

**Medium** (3)


</dt> <dd></dd> <dt>

<span id="Medium-high"></span><span id="medium-high"></span><span id="MEDIUM-HIGH"></span>

**Medium-high** (4)


</dt> <dd></dd> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>

**High** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**Key**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the **MDM\_BrowserSettings** class instance.

</dd> <dt>

**RestrictedSitesZoneSecurityLevel**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The security level for the restricted sites security zone.

Possible values are.

<dt>

<span id="Low"></span><span id="low"></span><span id="LOW"></span>

**Low** (1)


</dt> <dd></dd> <dt>

<span id="Medium-low"></span><span id="medium-low"></span><span id="MEDIUM-LOW"></span>

**Medium-low** (2)


</dt> <dd></dd> <dt>

<span id="Medium"></span><span id="medium"></span><span id="MEDIUM"></span>

**Medium** (3)


</dt> <dd></dd> <dt>

<span id="Medium-high"></span><span id="medium-high"></span><span id="MEDIUM-HIGH"></span>

**Medium-high** (4)


</dt> <dd></dd> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>

**High** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**TrustedSitesZoneSecurityLevel**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The security level for the trusted sites security zone.

Possible values are.

<dt>

<span id="Low"></span><span id="low"></span><span id="LOW"></span>

**Low** (1)


</dt> <dd></dd> <dt>

<span id="Medium-low"></span><span id="medium-low"></span><span id="MEDIUM-LOW"></span>

**Medium-low** (2)


</dt> <dd></dd> <dt>

<span id="Medium"></span><span id="medium"></span><span id="MEDIUM"></span>

**Medium** (3)


</dt> <dd></dd> <dt>

<span id="Medium-high"></span><span id="medium-high"></span><span id="MEDIUM-HIGH"></span>

**Medium-high** (4)


</dt> <dd></dd> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>

**High** (5)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                         |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





