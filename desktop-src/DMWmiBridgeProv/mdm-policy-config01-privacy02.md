---
title: MDM\_Policy\_Config01\_Privacy02 class
description: The MDM\_Policy\_Config01\_Privacy02 class represents the search policies available.
ms.assetid: 202213b9-5301-4c55-bbc6-6ce3daf705ad
keywords:
- MDM_Policy_Config01_Privacy02 class
- MDM_Policy_Config01_Privacy02 class, described
topic_type:
- apiref
api_name:
- MDM_Policy_Config01_Privacy02
- MDM_Policy_Config01_Privacy02.InstanceID
- MDM_Policy_Config01_Privacy02.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MDM\_Policy\_Config01\_Privacy02 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_Policy\_Config01\_Privacy02** class represents the search policies available.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv")]
class MDM_Policy_Config01_Privacy02
{
  string InstanceID;
  string ParentID;
  sint32 AllowAutoAcceptPairingAndPrivacyConsentPrompts;
  sint32 AllowInputPersonalization;
  string LetAppsSyncWithDevices_UserInControlOfTheseApps;
  sint32 PublishUserActivities;
  string LetAppsSyncWithDevices_ForceDenyTheseApps;
  string LetAppsSyncWithDevices_ForceAllowTheseApps;
  sint32 LetAppsSyncWithDevices;
  string LetAppsAccessTrustedDevices_UserInControlOfTheseApps;
  string LetAppsRunInBackground_UserInControlOfTheseApps;
  string LetAppsRunInBackground_ForceDenyTheseApps;
  string LetAppsRunInBackground_ForceAllowTheseApps;
  sint32 LetAppsRunInBackground;
  string LetAppsGetDiagnosticInfo_UserInControlOfTheseApps;
  string LetAppsGetDiagnosticInfo_ForceDenyTheseApps;
  string LetAppsGetDiagnosticInfo_ForceAllowTheseApps;
  sint32 LetAppsGetDiagnosticInfo;
  string LetAppsAccessTrustedDevices_ForceDenyTheseApps;
  string LetAppsAccessTrustedDevices_ForceAllowTheseApps;
  sint32 LetAppsAccessTrustedDevices;
  string LetAppsAccessRadios_UserInControlOfTheseApps;
  string LetAppsAccessTasks_UserInControlOfTheseApps;
  string LetAppsAccessTasks_ForceDenyTheseApps;
  string LetAppsAccessTasks_ForceAllowTheseApps;
  sint32 LetAppsAccessTasks;
  string LetAppsAccessRadios_ForceDenyTheseApps;
  string LetAppsAccessRadios_ForceAllowTheseApps;
  sint32 LetAppsAccessRadios;
  string LetAppsAccessPhone_UserInControlOfTheseApps;
  string LetAppsAccessPhone_ForceDenyTheseApps;
  string LetAppsAccessPhone_ForceAllowTheseApps;
  sint32 LetAppsAccessPhone;
  string LetAppsAccessMotion_UserInControlOfTheseApps;
  string LetAppsAccessNotifications_UserInControlOfTheseApps;
  string LetAppsAccessNotifications_ForceDenyTheseApps;
  string LetAppsAccessNotifications_ForceAllowTheseApps;
  sint32 LetAppsAccessNotifications;
  string LetAppsAccessMotion_ForceDenyTheseApps;
  string LetAppsAccessMotion_ForceAllowTheseApps;
  sint32 LetAppsAccessMotion;
  string LetAppsAccessMicrophone_UserInControlOfTheseApps;
  string LetAppsAccessMicrophone_ForceDenyTheseApps;
  string LetAppsAccessMicrophone_ForceAllowTheseApps;
  sint32 LetAppsAccessMicrophone;
  string LetAppsAccessMessaging_UserInControlOfTheseApps;
  string LetAppsAccessMessaging_ForceDenyTheseApps;
  string LetAppsAccessMessaging_ForceAllowTheseApps;
  sint32 LetAppsAccessMessaging;
  string LetAppsAccessLocation_UserInControlOfTheseApps;
  string LetAppsAccessLocation_ForceDenyTheseApps;
  string LetAppsAccessLocation_ForceAllowTheseApps;
  sint32 LetAppsAccessLocation;
  string LetAppsAccessEmail_UserInControlOfTheseApps;
  string LetAppsAccessEmail_ForceDenyTheseApps;
  string LetAppsAccessEmail_ForceAllowTheseApps;
  sint32 LetAppsAccessEmail;
  string LetAppsAccessContacts_UserInControlOfTheseApps;
  string LetAppsAccessContacts_ForceDenyTheseApps;
  string LetAppsAccessContacts_ForceAllowTheseApps;
  sint32 LetAppsAccessContacts;
  string LetAppsAccessCamera_UserInControlOfTheseApps;
  string LetAppsAccessCamera_ForceDenyTheseApps;
  string LetAppsAccessCamera_ForceAllowTheseApps;
  sint32 LetAppsAccessCamera;
  string LetAppsAccessCallHistory_UserInControlOfTheseApps;
  string LetAppsAccessCallHistory_ForceDenyTheseApps;
  string LetAppsAccessCallHistory_ForceAllowTheseApps;
  sint32 LetAppsAccessCallHistory;
  string LetAppsAccessCalendar_UserInControlOfTheseApps;
  string LetAppsAccessCalendar_ForceDenyTheseApps;
  string LetAppsAccessCalendar_ForceAllowTheseApps;
  sint32 LetAppsAccessCalendar;
  string LetAppsAccessAccountInfo_UserInControlOfTheseApps;
  string LetAppsAccessAccountInfo_ForceDenyTheseApps;
  string LetAppsAccessAccountInfo_ForceAllowTheseApps;
  sint32 LetAppsAccessAccountInfo;
  sint32 DisableAdvertisingId;
  sint32 EnableActivityFeed;
};
```

## Members

The **MDM\_Policy\_Config01\_Privacy02** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Policy\_Config01\_Privacy02** class has these properties.

<dl> <dt>

[AllowAutoAcceptPairingAndPrivacyConsentPrompts](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-allowautoacceptpairingandprivacyconsentprompts)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowInputPersonalization](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-allowinputpersonalization)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[DisableAdvertisingId](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-disableadvertisingid)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[EnableActivityFeed](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-enableactivityfeed)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the name of the parent node. For this class, the string is "Privacy".

</dd> <dt>

[LetAppsAccessAccountInfo](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessaccountinfo)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessAccountInfo\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessaccountinfo-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessAccountInfo\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessaccountinfo-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessAccountInfo\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessaccountinfo-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessCalendar](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscalendar)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessCalendar\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscalendar-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessCalendar\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscalendar-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessCalendar\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscalendar-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessCallHistory](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscallhistory)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessCallHistory\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscallhistory-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessCallHistory\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscallhistory-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessCallHistory\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscallhistory-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessCamera](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscamera)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessCamera\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscamera-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessCamera\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscamera-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessCamera\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscamera-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessContacts](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscontacts)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessContacts\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscontacts-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessContacts\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscontacts-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessContacts\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesscontacts-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessEmail](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessemail)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessEmail\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessemail-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessEmail\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessemail-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessEmail\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessemail-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessLocation](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesslocation)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessLocation\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesslocation-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessLocation\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesslocation-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessLocation\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesslocation-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessMessaging](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessmessaging)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessMessaging\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessmessaging-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessMessaging\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessmessaging-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessMessaging\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessmessaging-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessMicrophone](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessmicrophone)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessMicrophone\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessmicrophone-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessMicrophone\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessmicrophone-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessMicrophone\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessmicrophone-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessMotion](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessmotion)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessMotion\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessmotion-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessMotion\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessmotion-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessMotion\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessmotion-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessNotifications](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessnotifications)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessNotifications\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessnotifications-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessNotifications\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessnotifications-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessNotifications\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessnotifications-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessPhone](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessphone)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessPhone\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessphone-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessPhone\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessphone-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessPhone\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessphone-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessRadios](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessradios)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessRadios\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessradios-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessRadios\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessradios-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessRadios\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccessradios-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessTasks](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesstasks)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessTasks\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesstasks-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessTasks\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesstasks-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessTasks\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesstasks-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessTrustedDevices](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesstrusteddevices)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessTrustedDevices\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesstrusteddevices-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessTrustedDevices\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesstrusteddevices-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsAccessTrustedDevices\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsaccesstrusteddevices-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsGetDiagnosticInfo](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsgetdiagnosticinfo)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsGetDiagnosticInfo\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsgetdiagnosticinfo-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsGetDiagnosticInfo\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsgetdiagnosticinfo-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsGetDiagnosticInfo\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsgetdiagnosticinfo-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsRunInBackground](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsruninbackground)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsRunInBackground\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsruninbackground-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsRunInBackground\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsruninbackground-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsRunInBackground\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappsruninbackground-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsSyncWithDevices](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappssyncwithdevices)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsSyncWithDevices\_ForceAllowTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappssyncwithdevices-forceallowtheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsSyncWithDevices\_ForceDenyTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappssyncwithdevices-forcedenytheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LetAppsSyncWithDevices\_UserInControlOfTheseApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-letappssyncwithdevices-userincontroloftheseapps)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/Policy/Config"

</dd> <dt>

[PublishUserActivities](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-privacy#privacy-publishuseractivities)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](https://msdn.microsoft.com/library/windows/hardware/mt614877)
</dt> </dl>

 

 





