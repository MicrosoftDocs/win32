---
title: System.Shell.knownFolder method
description: Returns an instance of a System.Shell.Folder based on a \ 0034;well-known folder \ 0034; name as defined within the user profile (for example, Documents or ProgramFiles).
ms.assetid: 'f94c4cb5-208c-41e1-b5f0-6ca3272a1428'
keywords: ["knownFolder method Windows Sidebar", "knownFolder method Windows Sidebar , System.Shell object", "System.Shell object Windows Sidebar , knownFolder method"]
topic_type:
- apiref
api_name:
- System.Shell.knownFolder
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.knownFolder method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Returns an instance of a [**System.Shell.Folder**](system-shell-folder.md) based on a "well-known folder" name as defined within the user profile (for example, Documents or ProgramFiles).

## Syntax


```JScript
objRetVal = System.Shell.knownFolder(
  strKnownFolderPath
)
```



## Parameters

<dl> <dt>

*strKnownFolderPath* \[in\]
</dt> <dd>

The well-known name of a folder as a string.

</dd> </dl>

## Return value

An instance of a [**System.Shell.Folder**](system-shell-folder.md) object that can be used with [**System.Shell.Item**](system-shell-item.md) object methods.

## Remarks

The following are valid well-known folder names:

-   Desktop
-   Startup
-   StartMenu
-   Documents
-   Programs
-   CommonStartup
-   CommonPrograms
-   PublicDesktop
-   PublicFavorites
-   PublicDocuments
-   System
-   SystemX86
-   Profile
-   Windows
-   Pictures
-   Music
-   Videos
-   ProgramFiles
-   ProgramFilesCommon
-   ProgramFilesX86
-   ProgramFilesCommonX86
-   AdminTools
-   CommonAdminTools
-   PublicMusic
-   PublicPictures
-   PublicVideos
-   UserProfiles
-   Downloads
-   PublicDownloads
-   GadgetsUser
-   RecycleBinFolder

> [!Note]  
> Well-known names can vary between operating systems.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





