---
description: Outlines the introduction of libraries for Windows 7.
ms.assetid: 83c47963-4c8e-45ee-b707-bd45cfe048cd
title: Windows Shell Libraries in Windows 7
ms.topic: article
ms.date: 05/31/2018
---

# Windows Shell Libraries in Windows

This topic outlines the introduction of libraries for Windows 7 and later. Libraries are a Windows Shell feature. To access Windows Shell functionality, such as libraries, third-party developers of Windows Search applications must first implement a Shell data store. For more information, see [Implementing the Basic Folder Object Interfaces](/previous-versions/windows/desktop/legacy/cc144093(v=vs.85)).

This topic is organized as follows:

- [Libraries](#libraries)
  - [User Data Entry Points](#user-data-entry-points)
  - [Collections of Folders](#collections-of-folders)
  - [Supported Folders in Libraries](#supported-folders-in-libraries)
  - [Storage-Backed](#storage-backed)
  - [Non-File System Shell Containers](#non-file-system-shell-containers)
  - [Library Descriptions](#library-descriptions)
- [Related topics](#related-topics)

## Libraries

In Windows 7 and later, libraries are the default repository of user data. Users can browse their files the same way they would in a folder, or they can view their files arranged by properties such as date, type, and author. Unlike a folder, a library does not actually store items, but displays files that are stored in several folders at the same time. Libraries provide a single access point and rich view pivots to users of their aggregated content. For example, if a user has music files in folders on an external drive in addition to the **My Music** folder, then they are able to immediately access all music files through the Music library.

### User Data Entry Points

Default libraries (such as **My Documents**, **My Pictures**, and so forth) are the equivalent of [Known Folder](/previous-versions/windows/desktop/legacy/bb776911(v=vs.85)). Default libraries provide familiar entry points to users, but because library content is not limited to Known Folder content libraries give users more freedom to determine where documents and media should be stored. Libraries are exposed through the Shell namespace (Shell data source). Your application can provide users with the same familiar entry points to their data by enabling library awareness, and browsing.

### Collections of Folders

Libraries are user-defined collections of content. Windows Search indexes supported folders when they are included in libraries. This enables instant search, and property-based stack arrangement views in libraries.

### Supported Folders in Libraries

For folders to be supported in libraries, they must be indexable on the local machine, and indexed either on a remote Windows machine, or indexed on a server with files indexed by Windows Search.

Unsupported folders are blocked from being added by users in the Windows library management dialog. If non-indexed remote folders are added to a library using the [IShellLibrary](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishelllibrary) API, then the library user experience will revert to library **Safe Mode**. In **Safe Mode** features such as property-based stack arrangement views, filter suggestions, and **Start Menu** search support are removed from the affected library.

The following table lists folders included in libraries using the Windows Explorer library management dialog, and folders that are unsupported in **Safe Mode**:

| Supported Folders                                                                                                                            | Unsupported Folders                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Fixed and external NTFS and FAT32 hard drives                                                                                                | Removable drives (such as thumbdrives and SD cards)                                                     |
| Shares that are indexed by Windows Search (such as departmental servers, and on computers running Windows 10, and Windows 7 Home edition) | Removable media (such as CDs and DVDs)                                                                  |
| Shares that are available offline (such as **Redirected My Documents**, **Client Side Cache**)                                               | Network shares that are neither available offline nor remotely indexed (such as NAS drives)             |
| n/a                                                                                                                                          | Other data sources (such as Microsoft SharePoint, Microsoft Exchange, Microsoft OneDrive, and so forth) |

### Storage-Backed

Libraries are collections of storage folders. Users can save and copy files to a library directly, since every library has a default save location to send these files to. For default libraries, this is user Known Folder that is included in a library (such as **My Documents**), or the first folder added to a custom library. This is the folder where files go when a user drags and drops files on to a library or saves to a library with the common file dialog. The user may change the default save location of a library at any point, but if she removes the default save location, the next folder in the library will be selected as the new save location. Users can additionally save to any folder they have permissions to that has been included in a library.

### Non-File System Shell Containers

Libraries can contain on-file system Shell containers, such as **Computer** and **Control Panel**, but contain file system items. Library folders and contents can be enumerated and accessed using APIs for file system files and folders in previous operating systems. If your application is heavily dependent on file system specific APIs, then the [IShellLibrary](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishelllibrary) API can be used to obtain the file system paths of folders and files within libraries. In most cases it is recommended that you use the Shell programming model to support multiple Windows versions and item flexibility. For more information, see [Navigating the Shell Namespace](https://msdn.microsoft.com/library/dd378496(VS.85).aspx).

### Library Descriptions

Library descriptions are saved on disk as an XML file in the %appdata%Microsoft\\Windows\\Libraries folder (and potentially as **FOLDERID\_Libraries**. For more information about **FOLDERID\_Libraries**, see [KNOWNFOLDERID](/windows/desktop/shell/knownfolderid).

Library description files are XML files with the file name extension .library-ms. They files should never be accessed or edited by applications. The folder path text persisted to the library description files is not always current. Library folders are persisted in the library description file in the serialized binary [Shell Links](/windows/desktop/shell/links) format. For more information about libraries and the Library Description schema, see [Library Description Schema](../shell/library-schema-entry.md). For more information about federated search connectors and the Search Connector Description schema, [Search Connector Description Schema](search-sconn-desc-schema-entry.md).

> [NOTE]  
> Applications should always use the Shell programming model or the [IShellLibrary](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishelllibrary) API to consume and manipulate library contents, and never attempt to manually access or edit the library description file.

## Related topics

[Windows 7 Search](./-search-3x-wds-overview.md)

[New for Windows 7 Search](new-for-windows-7-search.md)

[Indexing Prioritization and Rowset Events in Windows 7](indexing-prioritization-and-rowset-events.md)