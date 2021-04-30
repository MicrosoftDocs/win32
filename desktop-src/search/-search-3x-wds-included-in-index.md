---
description: This topic describes the items that Windows Search indexes.
ms.assetid: 'vs|search|~\search\wds3x\overviews\misc_items_in_index.htm'
title: What Is Included in the Index
ms.topic: article
ms.date: 05/31/2018
---

# What Is Included in the Index

This topic describes the items that Windows Search indexes.

This topic is organized as follows:

-   [Indexed by Default](#indexed-by-default)
-   [File Formats Supported](#file-formats-supported)
-   [File Exclusions](#file-exclusions)
-   [Folder Exclusions](#folder-exclusions)
-   [Drive Exclusions](#drive-exclusions)
-   [Related topics](#related-topics)

 

## Indexed by Default

Protocol handlers and filters are included in Windows Search to index the following kinds of content:

-   In Windows Vista and later, a user's Microsoft Outlook and Microsoft Outlook Express mail items are indexed while the mail application is running.
-   Offline files in the client-side cache (CSC) are indexed by Windows Search locally.
-   Windows Search supports gathering file start addresses on NTFS and FAT32 volumes. NTFS supports notification-based indexing, and FAT32 supports an incremental crawl on start up and then responds to notifications.
-   Windows Vista and later continue to expose a per-folder/per-file property to enable indexing: the "**For fast searching, allowing Indexing Service to index this folder**" option in the **Property** dialog box. Setting the FANCI bit flag ensures that basic properties from the protocol, such as URL, filename, and size are indexed, but that neither filter handlers nor property handlers are run.
-   Text content is indexed but punctuation is not.

## File Formats Supported

Windows Search has protocol handlers, property handlers, and filter handlers to index the following formats automatically:

-   Media files: all media file types
-   **HTML** (nlhtml.dll): .ascx, .asp, .aspx, .css, .hhc, .htm, .html, .htt, .htw, .htx, .odc, .stm
-   **MIME HTML** (mimefilt.dll): .mht, .mhtml
-   **Office** (offfilt.dll): .doc, .dot, .pot, .pps, .ppt, .xlb, .xlc, .xls, .xlt
-   **Text** (query.dll): .asm, .asx, .bat, .c, .cmd, .cpp, .cxx, .def, .dic, .h, .hpp, .hxx, .idl, .idq , .inf, .ini, .inx, .js, .log, .m3u, .rc, .reg, .rtf, .txt, .url, .vbs, .wtx
-   **XML** (xmlfilt.dll): .xml, .xsl
-   **OneNote**: .one
-   **Tablet Journal** (jntfiltr.dll): .jnt

Properties are indexed for all files except structured storage. On Windows Vista and later, many media file properties are indexed; however, the content is not indexed if the files are protected by digital rights management (DRM).

> [!Note]  
> The HTML filter does not index HTML comments.

 

## File Exclusions

When a file type does not have an associated filter, or when a file does not have an extension, the system properties for files of that type are indexed, but the file content is not indexed.

Additionally, Windows Search does not index the content of files under information rights management (IRM) or digital rights management (DRM).

On Windows Vista (only), the following files are excluded from indexing by default:

-   Files marked as Hidden or System.
-   Files with the following extensions:

    .386, .aps, .AudioCD, .bin, .bk1, .bk2, .bkf, .bsc, .btr, .chk, .ci, .crwl, .dbg, .dct, .DeskLink, .dir, .dl\_, .dll, .drv, .dvd, .evt, .ex\_, .exe, .exp, .eyb, .fnd, .fnt, .Folder, .fon, .ghi, .gthr, .hqx, .icm, .idb, .idx, .ilk, .imc, .in\_, .ini, .inv, .jbf, .latex, .lib, .local, .m14, .mac, .manifest, .map, .MAPIMail, .mmf, .movie, .mv, .mydocs, .ncb, .obj, .oc\_, .ocx, .pch, .pdb, .pf, .pma, .pmc, .pml, .pmr, .res, .rmp, .rpc, .rsp, .sbr, .sc2, .sit, .sr\_, .sy\_, .sym, .sys, .tlb, .trc, .ttc, .ttf, .vbx, .vxd, .wll, .wlt, .xix, .z96, .ZFSendToTarget.

## Folder Exclusions

> [!TIP]
> Folder names are not case-sensitive.

 

The following folders are excluded from indexing by default:



| Folder exclusion pattern                                                              | Effect in Windows 7 | Effect in Windows Vista | Description                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------|---------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *%System%*\\ProgramData\\Microsoft\\Search\\Data\\                                    | **Excluded**        | No effect               | Indexer data on the system drive.                                                                                                                                                                                          |
| *%System%*\\Users\\*UserName*\\AppData\\                                              | **Excluded**        | No effect               | User's application data (includes temp data) on the system drive.<br/> For each user who logs onto the system, a specific exclusion pattern is added that excludes their application data from the index.<br/> |
| *%System%*\\Users\\\*\\AppData\\Local\\Microsoft\\Windows\\Temporary Internet Files\\ | **Excluded**        | No effect               | Default location of Windows Internet Explorer temporary internet files on the system drive.<br/> If the location of Internet Explorer temporary internet files is changed, those files may be indexed.<br/>    |
| *%System%*\\Windows\\CSC\\                                                            | **Excluded**        | No effect               | If indexing is turned on for the Windows system directory, the CSC folder (on the system drive) is still excluded from indexing.                                                                                           |
| *%System%*\\Windows\\\*\\Temp\\                                                       | **Excluded**        | No effect               | Windows temp data on the system drive.                                                                                                                                                                                     |
| *%System%*\\Windows.\*\\                                                              | **Excluded**        | No effect               | Old Windows installations on the system drive.                                                                                                                                                                             |
| *%System%*\\ProgramData\\                                                             | **Excluded**        | **Excluded**            | Note that the shared Start Menu sub-folder is indexed.                                                                                                                                                                     |
| *%System%*\\Users\\\*\\AppData\\                                                      | **Excluded**        | **Excluded**            | Users' application data (includes temp data).                                                                                                                                                                              |
| *%System%*\\Users\\\*\\AppData\\Local\\Temp\\                                         | **Excluded**        | **Excluded**            | Users' temp data. If indexing is turned on for user application data, user temp data is still excluded from indexing by default.                                                                                           |
| *%System%*\\Windows\\                                                                 | **Excluded**        | **Excluded**            | Operating system files on the system drive.                                                                                                                                                                                |
| *%System%*\\$Recycle Bin\\                                                            | **Excluded**        | **Excluded**            | Location of files in the Recycle Bin.                                                                                                                                                                                      |
| *%System%*\\Build\\                                                                   | No effect           | **Excluded**            | On the system drive.                                                                                                                                                                                                       |
| *%System%*\\Installed Repository\\                                                    | No effect           | **Excluded**            | On the system drive.                                                                                                                                                                                                       |
| *%System%*\\Program Files\\                                                           | No effect           | **Excluded**            | On the system drive.                                                                                                                                                                                                       |
| *%System%*\\Program Files (x86)\\                                                     | No effect           | **Excluded**            | On the system drive.                                                                                                                                                                                                       |
| \*\\Temp\\\*                                                                          | No effect           | **Excluded**            | Windows temp data and other folders with the name "temp".                                                                                                                                                                  |
| *%System%*\\Users\\Default\\                                                          | No effect           | **Excluded**            | The location of default user profile data on the system drive.                                                                                                                                                             |
| \*\\windows.\*\\                                                                      | No effect           | **Excluded**            | Old Windows installations and other folders with names that begin with "windows.".                                                                                                                                         |



 

## Drive Exclusions

On Windows 7 and Windows Vista, removable drives are not indexed by default.

> [!Note]  
> If removable drives report themselves as fixed drives, you can add them to be indexed even if they are actually removable. Information will remain in the index and Windows Search will do an incremental crawl to reconcile indexing results when the removable disk is plugged in again. Because USB flash drives report themselves as removable, they cannot be indexed.

 

## Related topics

<dl> <dt>

[Indexing, Querying and Notifications in Windows Search](-search-3x-wds-included-in-index.md)
</dt> <dt>

[Indexing Process in Windows Search](-search-indexing-process-overview.md)
</dt> <dt>

[Querying Process in Windows Search](querying-process--windows-search-.md)
</dt> <dt>

[Notifications Process in Windows Search](-search-3x-wds-support.md)
</dt> <dt>

[URL Formatting Requirements](url-formatting-requirements.md)
</dt> </dl>

 

 




