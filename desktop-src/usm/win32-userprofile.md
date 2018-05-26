---
title: Win32\_UserProfile class
description: Represents a user profile.
ms.assetid: b073a403-9850-4a4d-ba64-320cad5d8fed
keywords:
- Win32_UserProfile class User State Manageability API
- Win32_UserProfile class User State Manageability API , described
topic_type:
- apiref
api_name:
- Win32_UserProfile
- Win32_UserProfile.SID
- Win32_UserProfile.LocalPath
- Win32_UserProfile.Loaded
- Win32_UserProfile.RefCount
- Win32_UserProfile.Special
- Win32_UserProfile.RoamingConfigured
- Win32_UserProfile.RoamingPath
- Win32_UserProfile.RoamingPreference
- Win32_UserProfile.Status
- Win32_UserProfile.LastUseTime
- Win32_UserProfile.LastDownloadTime
- Win32_UserProfile.LastUploadTime
- Win32_UserProfile.HealthStatus
- Win32_UserProfile.LastAttempedProfileDownloadTime
- Win32_UserProfile.LastAttemptedProfileUploadTime
- Win32_UserProfile.LastBackgroundRegistryUploadTime
- Win32_UserProfile.AppDataRoaming
- Win32_UserProfile.Desktop
- Win32_UserProfile.StartMenu
- Win32_UserProfile.Documents
- Win32_UserProfile.Pictures
- Win32_UserProfile.Music
- Win32_UserProfile.Videos
- Win32_UserProfile.Favorites
- Win32_UserProfile.Contacts
- Win32_UserProfile.Downloads
- Win32_UserProfile.Links
- Win32_UserProfile.Searches
- Win32_UserProfile.SavedGames
api_location:
- Root\CIMv2
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_UserProfile class

Represents a user profile.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_UserProfile
{
  string                        SID;
  string                        LocalPath;
  boolean                       Loaded;
  uint32                        RefCount;
  boolean                       Special;
  boolean                       RoamingConfigured;
  string                        RoamingPath;
  boolean                       RoamingPreference;
  uint32                        Status;
  DATETIME                      LastUseTime;
  DATETIME                      LastDownloadTime;
  DATETIME                      LastUploadTime;
  uint8                         HealthStatus;
  DATETIME                      LastAttempedProfileDownloadTime;
  DATETIME                      LastAttemptedProfileUploadTime;
  DATETIME                      LastBackgroundRegistryUploadTime;
  Win32_FolderRedirectionHealth AppDataRoaming;
  Win32_FolderRedirectionHealth Desktop;
  Win32_FolderRedirectionHealth StartMenu;
  Win32_FolderRedirectionHealth Documents;
  Win32_FolderRedirectionHealth Pictures;
  Win32_FolderRedirectionHealth Music;
  Win32_FolderRedirectionHealth Videos;
  Win32_FolderRedirectionHealth Favorites;
  Win32_FolderRedirectionHealth Contacts;
  Win32_FolderRedirectionHealth Downloads;
  Win32_FolderRedirectionHealth Links;
  Win32_FolderRedirectionHealth Searches;
  Win32_FolderRedirectionHealth SavedGames;
};
```

## Members

The **Win32\_UserProfile** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_UserProfile** class has these methods.



| Method                                               | Description                                |
|:-----------------------------------------------------|:-------------------------------------------|
| [**ChangeOwner**](changeowner-win32-userprofile.md) | Changes a user profile's owner.<br/> |



 

### Properties

The **Win32\_UserProfile** class has these properties.

<dl> <dt>

**AppDataRoaming**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that represents the health of the user's redirected AppData\\\\Roaming folder.

</dd> <dt>

**Contacts**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that represents the health of the user's redirected Contacts folder.

</dd> <dt>

**Desktop**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that represents the health of the user's redirected Desktop folder.

</dd> <dt>

**Documents**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that represents the health of the user's redirected Documents folder.

</dd> <dt>

**Downloads**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that represents the health of the user's redirected Downloads folder.

</dd> <dt>

**Favorites**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that represents the health of the user's redirected Favorites folder.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (Healthy, Unhealthy, Caution, Not Applicable), **ValueMap** (0, 1, 2, 3)
</dt> </dl>

The health status of the profile.

</dd> <dt>

**LastAttempedProfileDownloadTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the profile is a roaming profile, this property is a [DATETIME](https://msdn.microsoft.com/library/aa389799) value that indicates the last time an attempt was made to download the profile from the server, even if it was unsuccessful.

If the profile is a local profile, this property is zero.

</dd> <dt>

**LastAttemptedProfileUploadTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the profile is a roaming profile, this property is a [DATETIME](https://msdn.microsoft.com/library/aa389799) value that indicates the last time an attempt was made to upload the profile to the server, even if it was unsuccessful.

If the profile is a local profile, this property is zero.

</dd> <dt>

**LastBackgroundRegistryUploadTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this profile is a roaming profile, this property is a [DATETIME](https://msdn.microsoft.com/library/aa389799) value that indicates the last time the profile's registry hive was uploaded to the server.

</dd> <dt>

**LastDownloadTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this profile is a roaming profile, this property is a [DATETIME](https://msdn.microsoft.com/library/aa389799) value that indicates the last time the profile was downloaded from the server.

</dd> <dt>

**LastUploadTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this profile is a roaming profile, this property is a [DATETIME](https://msdn.microsoft.com/library/aa389799) value that indicates the last time the profile was uploaded to the server.

</dd> <dt>

**LastUseTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [DATETIME](https://msdn.microsoft.com/library/aa389799) value that indicates the last time this profile was used.

</dd> <dt>

**Links**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that represents the health of the user's redirected Links folder.

</dd> <dt>

**Loaded**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the profile is loaded.

</dd> <dt>

**LocalPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user profile's path on the local computer.

</dd> <dt>

**Music**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that represents the health of the user's redirected Music folder.

</dd> <dt>

**Pictures**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that represents the health of the user's redirected Pictures folder.

</dd> <dt>

**RefCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The reference count of the profile. The profile's reference count is the number of applications or services that have loaded the profile and are using it. If the profile is loaded, the reference count must be greater than or equal to 1.

</dd> <dt>

**RoamingConfigured**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, a roaming profile is configured for the user.

> [!Note]  
> Even if a roaming profile is configured for the user, that doesn't necessarily mean that this user profile is a roaming profile. Policies and user preferences can prevent the profile from roaming. These are indicated in the **RoamingPreference** and **Status** properties.

 

</dd> <dt>

**RoamingPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If the **RoamingConfigured** property is true, this property contains the user's roaming profile path.

</dd> <dt>

**RoamingPreference**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, and if the **RoamingConfigured** property is **true**, this user profile can roam between the local computer and the server.

If **false**, or if the **RoamingConfigured** property is **false**, roaming is not allowed, and this user profile acts the same as a local profile.

The default value of this property is **true**.

</dd> <dt>

**SavedGames**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that represents the health of the user's redirected Saved Games folder.

</dd> <dt>

**Searches**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that represents the health of the user's redirected Searches folder.

</dd> <dt>

**SID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The [security identifier](https://msdn.microsoft.com/library/windows/desktop/aa379571) (SID) of the user who owns this user profile.

</dd> <dt>

**Special**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the profile belongs to a special system service.

</dd> <dt>

**StartMenu**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that represents the health of the user's redirected Start Menu folder.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the user profile. One or more of the following status values.



| Value                                                                                                                                                                                                                                        | Meaning                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Temporary"></span><span id="temporary"></span><span id="TEMPORARY"></span><dl> <dt>**Temporary**</dt> <dt>0x00000001</dt> </dl> | The profile is a temporary profile. It will be deleted when the user logs off.<br/>                                                                             |
| <span id="Roaming"></span><span id="roaming"></span><span id="ROAMING"></span><dl> <dt>**Roaming**</dt> <dt>0x00000002</dt> </dl>         | If this flag is set, the profile is a roaming profile. If it is not set, the profile is a local profile.<br/>                                                   |
| <span id="Mandatory"></span><span id="mandatory"></span><span id="MANDATORY"></span><dl> <dt>**Mandatory**</dt> <dt>0x00000004</dt> </dl> | The profile is a mandatory profile. This means that the administrator has set the profile for the user, and the user is not allowed to make changes to it.<br/> |
| <span id="Corrupted"></span><span id="corrupted"></span><span id="CORRUPTED"></span><dl> <dt>**Corrupted**</dt> <dt>0x00000008</dt> </dl> | The profile is corrupted and is not in use. A user or administrator must repair the corruption in order to use this profile again.<br/>                         |



 

</dd> <dt>

**Videos**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that represents the health of the user's redirected Videos folder.

</dd> </dl>

## Requirements



|                                     |                                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                  |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                |
| MOF<br/>                      | <dl> <dt>UserProfileWmiProvider.mof</dt> </dl> |



 

 





