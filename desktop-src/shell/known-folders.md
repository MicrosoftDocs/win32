---
description: Windows Vista introduces new storage scenarios and a new user profile namespace.
title: Known Folders
ms.topic: article
ms.date: 05/31/2018
ms.assetid: d0c25eef-53ac-4dad-805a-b9ba4cd86be9
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Known Folders

Windows Vista introduces new storage scenarios and a new user profile namespace. To address these new factors, the older system of referring to standard folders by a [**CSIDL**](csidl.md) value has been replaced. As of Windows Vista, those folders are referenced by a new set of GUID values called Known Folder IDs.

The Known Folder system provides these advantages:

-   Independent software vendors (ISVs) can extend the set of Known Folder IDs with their own. They can define folders, give them IDs, and register them with the system. CSIDL values could not be extended.
-   All Known Folders on a system can be enumerated. No API provided this functionality for CSIDL values. See [**IKnownFolderManager::GetFolderIds**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iknownfoldermanager-getfolderids) for more information.
-   A known folder added by an ISV can add custom properties that allow it to explain its purpose and intended use.
-   Many known folders can be redirected to new locations, including network locations. Under the CSIDL system, only the **My Documents** folder could be redirected.
-   Known folders can have custom handlers for use during creation or deletion.

The CSIDL system and APIs that make use of CSIDL values are still supported for compatibility. However, it is not recommended to use them in any new development.


The following topics discuss the specifics of the Known Folders system.

-   [Working with Known Folders in Applications](working-with-known-folders.md)
-   [How to Extend Known Folders with Custom Folders](how-to-extend-known-folders-with-custom-folders.md)
-   [**KNOWNFOLDERID**](knownfolderid.md)

The following reference pages explain the Win32 Known Folders functions, which can be used to retrieve the location of Known Folders or redirect them to a new location. These functions replace older Win32 functions. The new functions are provided to give equivalent behavior to the old functions, but each new function is also duplicated by a Component Object Model (COM) API.



| New Function                                             | Replaces                                           | COM Equivalent                                            |
|----------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------|
| [**SHGetKnownFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetknownfolderpath)     | [**SHGetFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderpatha)         | [**IKnownFolder::GetPath**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iknownfolder-getpath)     |
| [**SHGetKnownFolderIDList**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetknownfolderidlist) | [**SHGetFolderLocation**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderlocation) | [**IKnownFolder::GetIDList**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iknownfolder-getidlist) |
| [**SHSetKnownFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shsetknownfolderpath)     | [**SHSetFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shsetfolderpatha)         | [**IKnownFolder::SetPath**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iknownfolder-setpath)     |



 

The following reference pages explain the COM Known Folders APIs, which provide all of the functionality of the Win32 APIs listed above, plus add the ability to enumerate all Known Folders, access Known Folder properties, and extend the standard set of Known Folders.

-   [**IKnownFolder**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iknownfolder)
-   [**IKnownFolderManager**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iknownfoldermanager)

A C++ sample that demonstrates the Known Folder APIs is included in the Windows Software Development Kit (SDK). Once you have installed the Windows SDK on your computer, the sample can be found under %ProgramFiles%\\Microsoft SDKs\\Windows\\v6.0\\Samples\\WinUI\\Shell\\AppPlatform\\KnownFolders.

## Related topics

<dl> <dt>

[Known Folders Sample](/windows/win32/shell/samples-knownfolders)
</dt> </dl>
