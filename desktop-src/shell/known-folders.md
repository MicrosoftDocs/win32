---
Description: Windows Vista introduces new storage scenarios and a new user profile namespace.
title: Known Folders
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Known Folders

Windows Vista introduces new storage scenarios and a new user profile namespace. To address these new factors, the older system of referring to standard folders by a [**CSIDL**](csidl.md) value has been replaced. As of Windows Vista, those folders are referenced by a new set of GUID values called Known Folder IDs.

The Known Folder system provides these advantages:

-   Independent software vendors (ISVs) can extend the set of Known Folder IDs with their own. They can define folders, give them IDs, and register them with the system. CSIDL values could not be extended.
-   All Known Folders on a system can be enumerated. No API provided this functionality for CSIDL values. See [**IKnownFolderManager::GetFolderIds**](/windows/win32/shobjidl_core/nf-shobjidl_core-iknownfoldermanager-getfolderids?branch=master) for more information.
-   A known folder added by an ISV can add custom properties that allow it to explain its purpose and intended use.
-   Many known folders can be redirected to new locations, including network locations. Under the CSIDL system, only the **My Documents** folder could be redirected.
-   Known folders can have custom handlers for use during creation or deletion.

The CSIDL system and APIs that make use of CSIDL values are still supported for compatibility. However, it is not recommended to use them in any new development.

## 

The following topics discuss the specifics of the Known Folders system.

-   [Working with Known Folders in Applications](working-with-known-folders.md)
-   [How to Extend Known Folders with Custom Folders](how-to-extend-known-folders-with-custom-folders.md)
-   [**KNOWNFOLDERID**](knownfolderid.md)

The following reference pages explain the Win32 Known Folders functions, which can be used to retrieve the location of Known Folders or redirect them to a new location. These functions replace older Win32 functions. The new functions are provided to give equivalent behavior to the old functions, but each new function is also duplicated by a Component Object Model (COM) API.



| New Function                                             | Replaces                                           | COM Equivalent                                            |
|----------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------|
| [**SHGetKnownFolderPath**](/windows/win32/shlobj_core/nf-shlobj_core-shgetknownfolderpath?branch=master)     | [**SHGetFolderPath**](/windows/win32/shlobj_core/nf-shlobj_core-shgetfolderpatha?branch=master)         | [**IKnownFolder::GetPath**](/windows/win32/shobjidl_core/nf-shobjidl_core-iknownfolder-getpath?branch=master)     |
| [**SHGetKnownFolderIDList**](/windows/win32/shlobj_core/nf-shlobj_core-shgetknownfolderidlist?branch=master) | [**SHGetFolderLocation**](/windows/win32/shlobj_core/nf-shlobj_core-shgetfolderlocation?branch=master) | [**IKnownFolder::GetIDList**](/windows/win32/shobjidl_core/nf-shobjidl_core-iknownfolder-getidlist?branch=master) |
| [**SHSetKnownFolderPath**](/windows/win32/shlobj_core/nf-shlobj_core-shsetknownfolderpath?branch=master)     | [**SHSetFolderPath**](/windows/win32/shlobj_core/nf-shlobj_core-shsetfolderpatha?branch=master)         | [**IKnownFolder::SetPath**](/windows/win32/shobjidl_core/nf-shobjidl_core-iknownfolder-setpath?branch=master)     |



 

The following reference pages explain the COM Known Folders APIs, which provide all of the functionality of the Win32 APIs listed above, plus add the ability to enumerate all Known Folders, access Known Folder properties, and extend the standard set of Known Folders.

-   [**IKnownFolder**](/windows/win32/shobjidl_core/nn-shobjidl_core-iknownfolder?branch=master)
-   [**IKnownFolderManager**](/windows/win32/shobjidl_core/nn-shobjidl_core-iknownfoldermanager?branch=master)

A C++ sample that demonstrates the Known Folder APIs is included in the Windows Software Development Kit (SDK). Once you have installed the Windows SDK on your computer, the sample can be found under %ProgramFiles%\\Microsoft SDKs\\Windows\\v6.0\\Samples\\WinUI\\Shell\\AppPlatform\\KnownFolders.

## Related topics

<dl> <dt>

[Known Folders Sample](shell.samples_knownfolders)
</dt> </dl>

 

 



