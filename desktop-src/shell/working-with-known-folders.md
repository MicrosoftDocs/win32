---
description: The Known Folder system provides a way to interact with certain high-profile folders that are present by default in Windows.
ms.assetid: 8b6163b5-e152-47c2-99f1-43e80cf0713e
title: Working with Known Folders in Applications
ms.topic: article
ms.date: 05/31/2018
---

# Working with Known Folders in Applications

The Known Folder system provides a way to interact with certain high-profile folders that are present by default in Windows. It also allows those same interactions with folders installed and registered with the Known Folder system by applications. This topic discusses those possible interactions as they are provided by the Known Folder APIs.

- [Known Folder Interfaces](#known-folder-interfaces)
- [Redirection](#redirection)
- [Related topics](#related-topics)

> [!IMPORTANT]
> To redirect the Documents, Pictures, or Desktop folders to OneDrive, use OneDrive Known Folder Move instead of the redirection method described in this article. For information, see [Redirect and move Windows known folders to OneDrive](/onedrive/redirect-known-folders).  

## Known Folder Interfaces

There are two Known Folder interfaces: [**IKnownFolder**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iknownfolder) and [**IKnownFolderManager**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iknownfoldermanager).

[**IKnownFolderManager**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iknownfoldermanager) provides many of the more general functions in regard to these folders. Its methods allow you to:

-   Retrieve an [**IKnownFolder**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iknownfolder) based on either that folder's [**KNOWNFOLDERID**](knownfolderid.md), its canonical name, its path expressed as a string, or its path expressed as an IDList.
-   Convert a CSIDL to its [**KNOWNFOLDERID**](knownfolderid.md) equivalent or convert a **KNOWNFOLDERID** to its legacy CSIDL equivalent.
-   Register or unregister a Known Folder with the system.
-   Retrieve all [**KNOWNFOLDERID**](knownfolderid.md) values registered on that system.
-   Redirect a Known Folder to a new location.

[**IKnownFolder**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iknownfolder) provides a method that allows a folder to redirect itself by providing a new path. Its other methods get information about a specific Known Folder, including:

-   The category of the folder: virtual, fixed, common, or per-user.
-   The type of the folder, such as compressed, documents, pictures, or user files.
-   The [**KNOWNFOLDERID**](knownfolderid.md) of the folder.
-   The full path of the folder as an IDList or as a string. Also its relative path to a parent folder.
-   The canonical name of the folder.
-   The tooltip displayed for the folder.
-   The icon displayed for the folder.
-   A description of the folder that explains its purpose and use.
-   Whether the folder is capable of being redirected.

[**IKnownFolder**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iknownfolder) also provides a method to retrieve an [**IShellItem**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem) based on the folder. That allows you to bind the folder to a handler, compare two folders, and retrieve the folder's attributes, display name, and parent folder.

## Redirection

Folder redirection is an important feature of the known folder system. All known folders of category [**common**KF\_CATEGORY\_COMMON****](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-kf_category) or [**per-user**KF\_CATEGORY\_PERUSER****](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-kf_category) are redirectable. Folder of category [**virtual**KF\_CATEGORY\_VIRTUAL****](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-kf_category) or [**fixedr**KF\_CATEGORY\_FIXED****](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-kf_category), however, cannot be redirected.

Folders can be redirected either to another location on the same computer or to a location on a network. In the case of a network redirection, the folder can be cached locally through client-side caching to provide offline access. However, even if a local cache exists, the redirected folder itself must be accessed through the network.

Folder redirection is not new for Windows Vista. For example, in Windows XP some folders identified through the CSIDL system could be redirected through a call to [**SHSetFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shsetfolderpatha) or by modifying the CSIDL's entry in the registry. In Windows Vista and later, redirection should be accomplished through [**IKnownFolder::SetPath**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iknownfolder-setpath) or [**SHSetKnownFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shsetknownfolderpath).

To determine whether a folder can be redirected, call [**IKnownFolder::GetRedirectionCapabilities**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iknownfolder-getredirectioncapabilities). If the folder cannot be redirected, this call can give an explanation.

If a folder is redirected to a network location, the [**IKnownFolder**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iknownfolder) methods can still be successfully called on it.

## Related topics

<dl> <dt>

[Known Folders Sample](/previous-versions/windows/desktop/legacy/dd940364(v=vs.85))
</dt> </dl>

 

 
