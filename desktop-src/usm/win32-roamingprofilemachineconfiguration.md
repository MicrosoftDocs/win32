---
title: Win32\_RoamingProfileMachineConfiguration class
description: Represents the roaming profile configuration for a computer.
ms.assetid: 59ff72c2-976f-46b2-ab73-a2b616088847
keywords:
- Win32_RoamingProfileMachineConfiguration class User State Manageability API
- Win32_RoamingProfileMachineConfiguration class User State Manageability API , described
topic_type:
- apiref
api_name:
- Win32_RoamingProfileMachineConfiguration
- Win32_RoamingProfileMachineConfiguration.IsEffective
- Win32_RoamingProfileMachineConfiguration.PrimaryComputerEnabled
- Win32_RoamingProfileMachineConfiguration.AddAdminGroupToRUPEnabled
- Win32_RoamingProfileMachineConfiguration.BackgroundUploadParams
- Win32_RoamingProfileMachineConfiguration.DeleteRoamingCacheEnabled
- Win32_RoamingProfileMachineConfiguration.DeleteProfilesOlderDays
- Win32_RoamingProfileMachineConfiguration.DetectSlowLinkDisabled
- Win32_RoamingProfileMachineConfiguration.ForceUnloadDisabled
- Win32_RoamingProfileMachineConfiguration.TempProfileLogonBlocked
- Win32_RoamingProfileMachineConfiguration.OnlyAllowLocalProfiles
- Win32_RoamingProfileMachineConfiguration.ProfileUploadDisabled
- Win32_RoamingProfileMachineConfiguration.SlowLinkUIEnabled
- Win32_RoamingProfileMachineConfiguration.WaitForNetworkInSec
- Win32_RoamingProfileMachineConfiguration.MachineProfilePath
- Win32_RoamingProfileMachineConfiguration.SlowLinkTimeOutParams
- Win32_RoamingProfileMachineConfiguration.WaitForRemoteProfile
- Win32_RoamingProfileMachineConfiguration.AllowCrossForestUserPolicy
- Win32_RoamingProfileMachineConfiguration.OwnerCheckDisabled
api_location:
- Root\CIMv2
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_RoamingProfileMachineConfiguration class

Represents the roaming profile configuration for a computer.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_RoamingProfileMachineConfiguration
{
  boolean                                    IsEffective;
  boolean                                    PrimaryComputerEnabled;
  boolean                                    AddAdminGroupToRUPEnabled;
  Win32_RoamingProfileBackgroundUploadParams BackgroundUploadParams;
  boolean                                    DeleteRoamingCacheEnabled;
  uint16                                     DeleteProfilesOlderDays;
  boolean                                    DetectSlowLinkDisabled;
  boolean                                    ForceUnloadDisabled;
  boolean                                    TempProfileLogonBlocked;
  boolean                                    OnlyAllowLocalProfiles;
  boolean                                    ProfileUploadDisabled;
  boolean                                    SlowLinkUIEnabled;
  uint16                                     WaitForNetworkInSec;
  string                                     MachineProfilePath;
  Win32_RoamingProfileSlowLinkParams         SlowLinkTimeOutParams;
  boolean                                    WaitForRemoteProfile;
  boolean                                    AllowCrossForestUserPolicy;
  boolean                                    OwnerCheckDisabled;
};
```

## Members

The **Win32\_RoamingProfileMachineConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_RoamingProfileMachineConfiguration** class has these properties.

<dl> <dt>

**AddAdminGroupToRUPEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, add the Administrator group to roaming user profiles.

</dd> <dt>

**AllowCrossForestUserPolicy**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, allow cross-forest user policy and roaming user profiles. If **false**, a roaming profile user receives a local profile when logged on to a cross-forest domain.

</dd> <dt>

**BackgroundUploadParams**
</dt> <dd> <dl> <dt>

Data type: **Win32\_RoamingProfileBackgroundUploadParams**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**Win32\_RoamingProfileBackgroundUploadParams**](win32-roamingprofilebackgrounduploadparams.md) object containing the parameters for the background upload of a roaming user profile's registry file while the user is logged on.

</dd> <dt>

**DeleteProfilesOlderDays**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Max** (100000)
</dt> </dl>

If the **DeleteRoamingCache** property is **true**, this property specifies the number of days after which a user profile should be deleted. User profiles older than this number of days are deleted when the computer is restarted.

</dd> <dt>

**DeleteRoamingCacheEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, cached copies of the roaming profile are deleted when the user logs off.

</dd> <dt>

**DetectSlowLinkDisabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, do not detect slow network connections. If **false**, use the **SlowLinkTimeOutParams** property to determine whether the computer has a slow network connection.

</dd> <dt>

**ForceUnloadDisabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, do not forcibly unload the user's registry when the user logs off.

</dd> <dt>

**IsEffective**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the configuration settings are in effect.

</dd> <dt>

**MachineProfilePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The roaming profile path to be set for all users that log on to this computer. The path should be in the form of \\\\\\\\*ComputerName*\\\\*ShareName*\\\\%USERNAME% with no trailing backslash.

</dd> <dt>

**OnlyAllowLocalProfiles**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, allow only local user profiles.

</dd> <dt>

**OwnerCheckDisabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, don't check the owners of user profiles.

</dd> <dt>

**PrimaryComputerEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, a configured roaming profile will only be downloaded if the computer is a primary computer for the user.

</dd> <dt>

**ProfileUploadDisabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, prevent roaming profile changes from being copied to the server.

</dd> <dt>

**SlowLinkTimeOutParams**
</dt> <dd> <dl> <dt>

Data type: **Win32\_RoamingProfileSlowLinkParams**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**Win32\_RoamingProfileSlowLinkParams**](win32-roamingprofileslowlinkparams.md) object containing slow network connection timeout parameters to be used for user profiles.

If the **DetectSlowLinkDisabled** property is false, this property is ignored.

</dd> <dt>

**SlowLinkUIEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, the user is prompted to specify whether his or her profile should be downloaded even when the network connection is slow.

</dd> <dt>

**TempProfileLogonBlocked**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, do not allow users to log in with temporary profiles.

</dd> <dt>

**WaitForNetworkInSec**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Max** (300)
</dt> </dl>

The maximum time, in seconds, to wait for the network transport to be available if a user has a roaming user profile. If the network is unavailable after this time has elapsed, the user is logged on, but the profile is not synchronized.

</dd> <dt>

**WaitForRemoteProfile**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, wait for a remote user profile.

</dd> </dl>

## Remarks

This class requires a context object to be passed as the *pCtx* parameter to the [**IWbemServices::GetObject**](https://msdn.microsoft.com/library/aa392109) method. This context object has the following properties, which should be set to the following values:



| Property Name                                 | Type     | Specify This Value               |
|-----------------------------------------------|----------|----------------------------------|
| PolicyPlatformContext\_PrincipalContext\_Type | VT\_BSTR | "PolicyPlatform\_MachineContext" |
| PolicyPlatformContext\_PrincipalContext\_Id   | VT\_BSTR | "SYSTEM"                         |



 

## Requirements



|                                     |                                                                                                                    |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                               |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                             |
| MOF<br/>                      | <dl> <dt>UserProfileConfigurationWmiProvider.mof</dt> </dl> |



 

 





