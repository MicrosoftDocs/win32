---
title: Win32\_FolderRedirection class
description: Represents the redirection properties of a known folder.
ms.assetid: 47c75ebd-8c49-4d5a-8c31-710fead8b593
keywords:
- Win32_FolderRedirection class User State Manageability API
- Win32_FolderRedirection class User State Manageability API , described
topic_type:
- apiref
api_name:
- Win32_FolderRedirection
- Win32_FolderRedirection.FolderId
- Win32_FolderRedirection.RedirectionType
- Win32_FolderRedirection.RedirectionPath
- Win32_FolderRedirection.ExclusiveRightsGranted
- Win32_FolderRedirection.ContentsMovedOnPolicyRemoval
- Win32_FolderRedirection.ContentsMoved
- Win32_FolderRedirection.ContentsRenamedInLocalCache
- Win32_FolderRedirection.MakeFoldersAvailableOfflineDisabled
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

# Win32\_FolderRedirection class

Represents the redirection properties of a known folder.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_FolderRedirection
{
  string  FolderId;
  uint8   RedirectionType;
  string  RedirectionPath;
  boolean ExclusiveRightsGranted;
  boolean ContentsMovedOnPolicyRemoval;
  boolean ContentsMoved;
  boolean ContentsRenamedInLocalCache;
  boolean MakeFoldersAvailableOfflineDisabled;
};
```

## Members

The **Win32\_FolderRedirection** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_FolderRedirection** class has these properties.

<dl> <dt>

**ContentsMoved**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, the files and directories in the known folder will be moved to the new location in the server share in two steps:

1.  The files and directories in the known folder are copied into the local UNC location.
2.  The files and directories in all redirected folders in the local UNC location are synchronized with the files and directories in the corresponding folders in the server share. This causes the files and directories to be moved from the local UNC location to the server share.

</dd> <dt>

**ContentsMovedOnPolicyRemoval**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, the files and directories in the known folder will be moved back to the local user profile when the redirection policy is removed.

If **false**, the folder will remain in the redirected location after the redirection policy is removed.

</dd> <dt>

**ContentsRenamedInLocalCache**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, the files and directories in the known folder are renamed from the old location to the new location in the Offline Files cache. Note that setting this property does not move the files and directories. To move them, you must set the **ContentsMoved** property.

</dd> <dt>

**ExclusiveRightsGranted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, the user whose files are being redirected will be granted exclusive rights to the folder.

If **false**, the folder's access permissions are not changed.

</dd> <dt>

**FolderId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
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

**MakeFoldersAvailableOfflineDisabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, redirected folders will not automatically be made available offline.

</dd> <dt>

**RedirectionPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The redirection path to be used if the value of the **RedirectionType** property is **ToFullPath** or **ToUserFolder**.

</dd> <dt>

**RedirectionType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The type of folder redirection to be performed.



| Value                                                                                                                                                                                                                                                                   | Meaning                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <span id="ToFullPath"></span><span id="tofullpath"></span><span id="TOFULLPATH"></span><dl> <dt>**ToFullPath**</dt> <dt>0</dt> </dl>                                 | Redirect to the location specified by the **RedirectionPath** property.<br/> |
| <span id="ToLocalUserProfile"></span><span id="tolocaluserprofile"></span><span id="TOLOCALUSERPROFILE"></span><dl> <dt>**ToLocalUserProfile**</dt> <dt>1</dt> </dl> | Redirect to the local user profile.<br/>                                     |



 

</dd> </dl>

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                        |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                      |
| MOF<br/>                      | <dl> <dt>FolderRedirectionWMIProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_FolderRedirectionHealth**](win32-folderredirectionhealth.md)
</dt> <dt>

[**Win32\_FolderRedirectionHealthConfiguration**](win32-folderredirectionhealthconfiguration.md)
</dt> <dt>

[**Win32\_FolderRedirectionUserConfiguration**](win32-folderredirectionuserconfiguration.md)
</dt> </dl>

 

 





