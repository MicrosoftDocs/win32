---
Description: Represents information about a user profile on a Windows system.
ms.assetid: a0ba12a6-6fe6-4e06-9346-a54cc19143e6
title: Win32\_UserProfile class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_UserProfile class

Represents information about a user profile on a Windows system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_UserProfile
{
  string                        SID;
  string                        LocalPath;
  boolean                       Loaded;
  uint32                    REF refCount;
  boolean                       Special;
  boolean                       RoamingConfigured;
  string                        RoamingPath;
  boolean                       RoamingPreference;
  uint32                        Status;
  DATETIME                      LastUseTime;
  DATETIME                      LastDownloadTime;
  DATETIME                      LastUploadTime;
  uint8                         HealthStatus;
  DATETIME                      LastAttemptedProfileDownloadTime;
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



| Method                                               | Description                                     |
|:-----------------------------------------------------|:------------------------------------------------|
| [**ChangeOwner**](changeowner-win32-userprofile.md) | Changes the owner of a user profile.<br/> |



 

### Properties

The **Win32\_UserProfile** class has these properties.

<dl> <dt>

**AppDataRoaming**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that contains the health status of the user's redirected AppData\\Roaming folder.

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**Contacts**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that contains the health status of the user's redirected Contacts folder.

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**Desktop**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that contains the health status of the user's redirected Desktop folder.

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**Documents**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that contains the health status of the user's redirected Documents folder.

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**Downloads**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that contains the health status of the user's redirected Downloads folder.

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**Favorites**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that contains the health status of the user's redirected Favorites folder.

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The health status of the profile

This property contains one of the following values

<dl> <dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>**Healthy** (0)
</dt> <dt>

<span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span>**Unhealthy** (1)
</dt> <dt>

<span id="Caution"></span><span id="caution"></span><span id="CAUTION"></span>**Caution** (2)
</dt> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (3)
</dt> </dl>

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**LastAttemptedProfileDownloadTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this is a roaming profile, the last time an attempt was made to download the profile; otherwise "0".

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**LastAttemptedProfileUploadTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this is a roaming profile, the last time an attempt was made to upload the profile; otherwise "0".

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**LastBackgroundRegistryUploadTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this is a roaming profile, the last time the registry hive of the profile was uploaded; otherwise "0".

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**LastDownloadTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last time that a roaming profile was downloaded from the server.

</dd> <dt>

**LastUploadTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last time that a roaming profile was uploaded to the server.

</dd> <dt>

**LastUseTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last time that the profile was used.

</dd> <dt>

**Links**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that contains the health status of the user's redirected Links folder.

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**Loaded**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the user profile is loaded. **True** if the user profile is loaded; otherwise **false**.

</dd> <dt>

**LocalPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The local path of the user profile.

</dd> <dt>

**Music**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that contains the health status of the user's redirected Music folder.

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**Pictures**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that contains the health status of the user's redirected Pictures folder.

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**refCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The reference count of the profile. If the profile is loaded, the reference count is at least "1". Higher values indicate that more than one application or service has loaded the profile and is using it.

</dd> <dt>

**RoamingConfigured**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the owner of this user profile has roaming configured on any of their user profiles. **True** if the user has a roaming profile configured; otherwise **false**.

> [!Note]  
> If a user has a roaming profile configured, it does not mean that this profile is a roaming profile. Other policies and user preferences can prevent the profile from roaming. For more information, see the **RoamingPreference** and Status properties.

 

</dd> <dt>

**RoamingPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user's roaming profile path if the **RoamingConfigured** property is set to **true**.

</dd> <dt>

**RoamingPreference**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the user prefers to use this profile to roam if the **RoamingConfigured** property is set to true. By default, the **RoamingPreference** property is set to true and the roaming profile can roam between the local computer and the server. If the user sets this property to false to prevent roaming, the profile works like a local profile.

</dd> <dt>

**SavedGames**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that contains the health status of the user's redirected Saved Games folder.

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**Searches**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that contains the health status of the user's redirected Searches folder.

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**SID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The Security Identifier (SID) of the user who owns the user profile.

</dd> <dt>

**Special**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the user profile is owned by a special system service. **True** if the user profile is owned by a system service; otherwise **false**.

</dd> <dt>

**StartMenu**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that contains the health status of the user's redirected Start Menu folder.

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A bit field that contains the status of the profile.

This property contains one or more of the following values:



| Value                                                                                                                                                                                                                               | Meaning                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| <span id="Undefined"></span><span id="undefined"></span><span id="UNDEFINED"></span><dl> <dt>**Undefined**</dt> <dt>0</dt> </dl> | The status of the profile is not set.<br/>                                                                             |
| <span id="Temporary"></span><span id="temporary"></span><span id="TEMPORARY"></span><dl> <dt>**Temporary**</dt> <dt>1</dt> </dl> | The profile is a temporary profile and will be deleted after the user logs off.<br/>                                   |
| <span id="Roaming"></span><span id="roaming"></span><span id="ROAMING"></span><dl> <dt>**Roaming**</dt> <dt>2</dt> </dl>         | The profile is set to roaming. If this bit is not set, the profile is set to local.<br/>                               |
| <span id="Mandatory"></span><span id="mandatory"></span><span id="MANDATORY"></span><dl> <dt>**Mandatory**</dt> <dt>4</dt> </dl> | The profile is a mandatory profile.<br/>                                                                               |
| <span id="Corrupted"></span><span id="corrupted"></span><span id="CORRUPTED"></span><dl> <dt>**Corrupted**</dt> <dt>8</dt> </dl> | The profile is corrupted and is not in use. The user or administrator must fix the corruption to use the profile.<br/> |



 

</dd> <dt>

**Videos**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirectionHealth**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md) object that contains the health status of the user's redirected Videos folder.

**Windows Vista, Windows Server 2008, Windows 7 and Windows Server 2008 R2:** This property is not available before Windows 8 and Windows Server 2012.

</dd> </dl>

## Examples

To use **Win32\_UserProfile** to migrate a user to a new domain, see the following [Vista s MoveUser.exe replacement](http://blogs.technet.com/b/askds/archive/2008/09/09/vista-s-moveuser-exe-replacement.aspx) article on TechNet.

## Requirements



|                                     |                                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP1<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                                |
| MOF<br/>                      | <dl> <dt>UserProfileWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Profprov.dll</dt> </dl>               |



## See also

<dl> <dt>

[UserProfileProvider Provider Classes](userprofileprovider-provider-classes.md)
</dt> </dl>

 

 




