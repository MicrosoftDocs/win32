---
title: Win32\_FolderRedirectionHealth class
description: Represents the health of a known folder that is being redirected.
ms.assetid: aa33db6f-201b-474f-9c2f-6792585c73e5
keywords:
- Win32_FolderRedirectionHealth class User State Manageability API
- Win32_FolderRedirectionHealth class User State Manageability API , described
topic_type:
- apiref
api_name:
- Win32_FolderRedirectionHealth
- Win32_FolderRedirectionHealth.OfflineFileNameFolderGUID
- Win32_FolderRedirectionHealth.Redirected
- Win32_FolderRedirectionHealth.OfflineAccessEnabled
- Win32_FolderRedirectionHealth.LastSuccessfulSyncTime
- Win32_FolderRedirectionHealth.LastSyncTime
- Win32_FolderRedirectionHealth.LastSyncStatus
- Win32_FolderRedirectionHealth.HealthStatus
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

# Win32\_FolderRedirectionHealth class

Represents the health of a known folder that is being redirected.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_FolderRedirectionHealth
{
  string   OfflineFileNameFolderGUID;
  boolean  Redirected;
  boolean  OfflineAccessEnabled;
  DATETIME LastSuccessfulSyncTime;
  DATETIME LastSyncTime;
  uint8    LastSyncStatus;
  uint8    HealthStatus;
};
```

## Members

The **Win32\_FolderRedirectionHealth** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_FolderRedirectionHealth** class has these properties.

<dl> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (Healthy, Caution, Unhealthy), **ValueMap** (0, 1, 2)
</dt> </dl>

The health status of this folder, based on the values that were set in the [**Win32\_FolderRedirectionHealthConfiguration**](win32-folderredirectionhealthconfiguration.md) properties.

</dd> <dt>

**LastSuccessfulSyncTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [DATETIME](https://msdn.microsoft.com/library/aa389799) value that represents the last time this folder was successfully synchronized to the Offline Files cache.

</dd> <dt>

**LastSyncStatus**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the last attempt to synchronize this folder to the Offline Files cache.

</dd> <dt>

**LastSyncTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [DATETIME](https://msdn.microsoft.com/library/aa389799) value that represents the last time an attempt was made to synchronized this folder to the Offline Files cache, even if it was unsuccessful.

</dd> <dt>

**OfflineAccessEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the Offline Files feature is enabled for this folder.

</dd> <dt>

**OfflineFileNameFolderGUID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The GUID for the known folder. One of the following values.



| For This Known Folder:   | Use This Known Folder Identifier: |
|--------------------------|-----------------------------------|
| Application Data Roaming | FOLDERID\_RoamingAppData          |
| Desktop                  | FOLDERID\_Desktop                 |
| Start Menu               | FOLDERID\_StartMenu               |
| Documents                | FOLDERID\_Documents               |
| Pictures                 | FOLDERID\_Pictures                |
| Music                    | FOLDERID\_Music                   |
| Videos                   | FOLDERID\_Videos                  |
| Favorites                | FOLDERID\_Favorites               |
| Contacts                 | FOLDERID\_Contacts                |
| Downloads                | FOLDERID\_Downloads               |
| Links                    | FOLDERID\_Links                   |
| Searches                 | FOLDERID\_SavedSearches           |
| Saved Games              | FOLDERID\_SavedGames              |



 

</dd> <dt>

**Redirected**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the folder is being redirected.

</dd> </dl>

## Requirements



|                                     |                                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                  |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                |
| MOF<br/>                      | <dl> <dt>UserProfileWmiProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_FolderRedirection**](win32-folderredirection.md)
</dt> <dt>

[**Win32\_FolderRedirectionHealthConfiguration**](win32-folderredirectionhealthconfiguration.md)
</dt> <dt>

[**Win32\_FolderRedirectionUserConfiguration**](win32-folderredirectionuserconfiguration.md)
</dt> </dl>

 

 





