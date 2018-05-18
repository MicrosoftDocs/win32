---
title: Win32\_FolderRedirectionUserConfiguration class
description: Represents the user's folder redirection configuration settings.
ms.assetid: '1b9ebf84-6caf-4ff8-bb86-11490a8ad7a2'
keywords: ["Win32_FolderRedirectionUserConfiguration class User State Manageability API", "Win32_FolderRedirectionUserConfiguration class User State Manageability API , described"]
topic_type:
- apiref
api_name:
- Win32_FolderRedirectionUserConfiguration
- Win32_FolderRedirectionUserConfiguration.IsEffective
- Win32_FolderRedirectionUserConfiguration.PrimaryComputerEnabled
- Win32_FolderRedirectionUserConfiguration.AppDataRoaming
- Win32_FolderRedirectionUserConfiguration.Desktop
- Win32_FolderRedirectionUserConfiguration.StartMenu
- Win32_FolderRedirectionUserConfiguration.Documents
- Win32_FolderRedirectionUserConfiguration.Pictures
- Win32_FolderRedirectionUserConfiguration.Music
- Win32_FolderRedirectionUserConfiguration.Videos
- Win32_FolderRedirectionUserConfiguration.Favorites
- Win32_FolderRedirectionUserConfiguration.Contacts
- Win32_FolderRedirectionUserConfiguration.Downloads
- Win32_FolderRedirectionUserConfiguration.Links
- Win32_FolderRedirectionUserConfiguration.Searches
- Win32_FolderRedirectionUserConfiguration.SavedGames
api_location:
- Root\CIMv2
api_type:
- Schema
---

# Win32\_FolderRedirectionUserConfiguration class

Represents the user's folder redirection configuration settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_FolderRedirectionUserConfiguration
{
  boolean                 IsEffective;
  boolean                 PrimaryComputerEnabled;
  Win32_FolderRedirection AppDataRoaming;
  Win32_FolderRedirection Desktop;
  Win32_FolderRedirection StartMenu;
  Win32_FolderRedirection Documents;
  Win32_FolderRedirection Pictures;
  Win32_FolderRedirection Music;
  Win32_FolderRedirection Videos;
  Win32_FolderRedirection Favorites;
  Win32_FolderRedirection Contacts;
  Win32_FolderRedirection Downloads;
  Win32_FolderRedirection Links;
  Win32_FolderRedirection Searches;
  Win32_FolderRedirection SavedGames;
};
```

## Members

The **Win32\_FolderRedirectionUserConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_FolderRedirectionUserConfiguration** class has these properties.

<dl> <dt>

**AppDataRoaming**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirection**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**Win32\_FolderRedirection**](win32-folderredirection.md) object that represents the properties of the user's AppData\\\\Roaming folder.

</dd> <dt>

**Contacts**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirection**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**Win32\_FolderRedirection**](win32-folderredirection.md) object that represents the properties of the user's Contacts folder.

</dd> <dt>

**Desktop**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirection**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**Win32\_FolderRedirection**](win32-folderredirection.md) object that represents the properties of the user's Desktop folder.

</dd> <dt>

**Documents**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirection**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**Win32\_FolderRedirection**](win32-folderredirection.md) object that represents the properties of the user's Documents folder.

</dd> <dt>

**Downloads**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirection**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**Win32\_FolderRedirection**](win32-folderredirection.md) object that represents the properties of the user's Downloads folder.

</dd> <dt>

**Favorites**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirection**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**Win32\_FolderRedirection**](win32-folderredirection.md) object that represents the properties of the user's Favorites folder.

</dd> <dt>

**IsEffective**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the configuration settings are in effect.

</dd> <dt>

**Links**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirection**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**Win32\_FolderRedirection**](win32-folderredirection.md) object that represents the properties of the user's Links folder.

</dd> <dt>

**Music**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirection**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**Win32\_FolderRedirection**](win32-folderredirection.md) object that represents the properties of the user's Music folder.

</dd> <dt>

**Pictures**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirection**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**Win32\_FolderRedirection**](win32-folderredirection.md) object that represents the properties of the user's Pictures folder.

</dd> <dt>

**PrimaryComputerEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, the Primary Computer feature is enabled for this user.

</dd> <dt>

**SavedGames**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirection**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**Win32\_FolderRedirection**](win32-folderredirection.md) object that represents the properties of the user's Saved Games folder.

</dd> <dt>

**Searches**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirection**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**Win32\_FolderRedirection**](win32-folderredirection.md) object that represents the properties of the user's Searches folder.

</dd> <dt>

**StartMenu**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirection**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**Win32\_FolderRedirection**](win32-folderredirection.md) object that represents the properties of the user's Start Menu folder.

</dd> <dt>

**Videos**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FolderRedirection**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**Win32\_FolderRedirection**](win32-folderredirection.md) object that represents the properties of the user's Videos folder.

</dd> </dl>

## Remarks

Folder redirection must be applied during logon, and the logon process cannot be completed until folder redirection is complete. This ensures that:

-   The files are not being used by any application and can be freely redirected by the feature.
-   The user's folders and files will be fully configured before the user accesses them.

In Windows 7, Windows Server 2008 R2, and earlier Windows versions, folder redirection was implemented by a Group Policy Client Side Extension (GPCSE) that received the following data from the Group Policy Manager:

-   The list of folders to be redirected
-   The user's logon state
-   The user's impersonation token

In Windows 8, Windows Server 2012, and later, folder redirection can be performed by WMI or by Group Policy. If it's performed by WMI, the **Win32\_FolderRedirectionUserConfiguration** class itself contains the list of folders to be redirected.

Because folder redirection must be applied during logon, and the logon process cannot be completed until folder redirection is complete, the user's logon must be blocked until Folder Redirection is applied. To ensure this behavior, you must implement a GPCSE. This GPCSE is invoked by the Group Policy Manager on every logon. The Group Policy Manager informs the GPCSE extension if the logon is blocked or not and passes a user token to the GPCSE that can be used for impersonation.

To pass the user's logon state and impersonation token, this class requires a context object to be passed as the *pCtx* parameter to the [**IWbemServices::GetObject**](https://msdn.microsoft.com/library/aa392109) method. This context object has the following properties, which should be set to the following values:



| Property Name                                        | Type     | Specify This Value                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PolicyPlatformContext\_PrincipalContext\_Type        | VT\_BSTR | "PolicyPlatform\_UserContext"                                                                                                                                                                                                                                                                                         |
| PolicyPlatformContext\_PrincipalContext\_Id          | VT\_BSTR | The user's SID in SDDL format                                                                                                                                                                                                                                                                                         |
| PolicyPlatformContext\_PrincipalContext\_UserSession | VT\_I4   | The identifier of a Windows session to which the user is interactively logged on. It is possible that there are multiple sessions to which the user is logged on interactively. The MPP will pass the id of one of these sessions.                                                                                    |
| PolicyPlatformContext\_PrincipalContext\_Flags       | VT\_I4   | This property is set to zero to indicate that the user's logon is blocked. Folder Redirection can be safely applied, because the user's files are guaranteed not to be in use.<br/> This property is set to 0x10 to indicate a nonblocking state, in which Folder Redirection should not be applied.<br/> |
| PolicyPlatformContext\_PrincipalContext\_ProcessId   | VT\_I4   | The process identifier of the process that owns the user's impersonation token                                                                                                                                                                                                                                        |
| PolicyPlatformContext\_PrincipalContext\_UserToken   | VT\_I8   | The user's impersonation token                                                                                                                                                                                                                                                                                        |



 

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                        |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                      |
| MOF<br/>                      | <dl> <dt>FolderRedirectionWMIProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_FolderRedirection**](win32-folderredirection.md)
</dt> <dt>

[**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md)
</dt> <dt>

[**Win32\_FolderRedirectionHealthConfiguration**](win32-folderredirectionhealthconfiguration.md)
</dt> </dl>

 

 





