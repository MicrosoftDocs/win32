---
title: System.Shell.knownFolderPath method
description: Retrieves a Known Folder Universal Naming Convention (UNC) path.
ms.assetid: b5c0b99b-2cd2-4b28-8c2b-bd007687bccf
keywords:
- knownFolderPath method Windows Sidebar
- knownFolderPath method Windows Sidebar , System.Shell object
- System.Shell object Windows Sidebar , knownFolderPath method
topic_type:
- apiref
api_name:
- System.Shell.knownFolderPath
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Shell.knownFolderPath method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Retrieves a **Known Folder** Universal Naming Convention (UNC) path.

## Syntax


```JScript
strRetVal = System.Shell.knownFolderPath(
  strKnownFolderID
)
```



## Parameters

<dl> <dt>

*strKnownFolderID* \[in\]
</dt> <dd>

**String** that specifies the Known Folder ID.

> [!Note]  
> For Windows 7, this method can accept a [KNOWNFOLDERID](http://msdn.microsoft.com/library/bb762584.aspx) globally unique identifier (GUID).

 

</dd> </dl>

## Return value

**String** that specifies the UNC path.

## Remarks

*strKnownFolderID* represents the GUID that identifies standard folders registered with the system as Known Folders. These folders are installed with Windows Vista and later operating systems; a computer will only have the folders appropriate to it installed.

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
> Well-known names can vary across operating systems.

 

## Examples

The following example demonstrates how to retrieve the UNC path for a known folder.


```JScript
// --------------------------------------------------------------------
// Display the UNC path of the Known Folder.
// txtKnownFolderID: the Known Folder GUID.
// --------------------------------------------------------------------
function GetKnownFolderPath(txtKnownFolderID)
{
    try
    {
        spFeedback.innerHTML = System.Shell.knownFolderPath(txtKnownFolderID) + "<br/>";
    }
    catch(e)
    {
        spFeedback.innerHTML = "Unable to retrieve path.<br/>";
    }
}
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





