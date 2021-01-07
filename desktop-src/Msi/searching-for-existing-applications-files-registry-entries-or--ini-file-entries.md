---
description: Windows Installer can search for a specific file or directory during an installation. File or directory searches are used to determine whether a user has already installed a version of an application.
ms.assetid: a78ca652-c730-4231-80f2-60cf0bad5b02
title: Searching for Existing Applications, Files, Registry Entries or .ini File Entries
ms.topic: article
ms.date: 05/31/2018
---

# Searching for Existing Applications, Files, Registry Entries or .ini File Entries

Windows Installer can search for a specific file or directory during an installation. File or directory searches are used to determine whether a user has already installed a version of an application.

[AppSearch Action](appsearch-action.md) searches a user system for file signatures that are specified in the [AppSearch Table](appsearch-table.md). If the AppSearch action finds an installed file or directory with the specified signature, it sets a corresponding property, also specified in the AppSearch Table, to the location of the file or directory. When searching for a file, the file signature must also be listed in the [Signature Table](signature-table.md). If a file signature is listed in the AppSearch Table and is not listed in the Signature Table, the search looks for a directory, registry entry, or .ini file entry.

To expedite the search of a user computer, the Installer queries the following locator database tables in the order listed for a suggested search location:

-   If the file signature is listed in the [CompLocator Table](complocator-table.md), the suggested search location is the key path of a component. If the signature is not listed in this table or not installed at the suggested location, the Installer queries the [RegLocator Table](reglocator-table.md) for a suggested location.
-   If the file signature is listed in the [RegLocator Table](reglocator-table.md), the suggested search location is a key path written in the user registry. If the signature is not listed in this table or not installed at the suggested location, the Installer queries the [IniLocator Table](inilocator-table.md) for a suggested location.
-   If the file signature is listed in the [IniLocator Table](inilocator-table.md), the suggested search location is a key path written in an .ini file present in the default Windows directory of a user system. If the signature is not listed in this table or not installed at the suggested location, the Installer queries the [DrLocator Table](drlocator-table.md) for a suggested location.
-   If the file signature is listed in the [DrLocator Table](drlocator-table.md), the suggested search location is a path in the user directory tree. The depth of subdirectory levels to search below this location is also specified in this table.

The first time the Installer finds the file signature at a suggested location, it stops searching for this file or directory, and sets the corresponding property in the [AppSearch Table](appsearch-table.md). For more information, see the following:

-   [Searching All Fixed Drives for a File](searching-all-fixed-drives-for-a-file.md)
-   [Searching for a Directory and a File in the Directory](searching-for-a-directory-and-a-file-in-the-directory.md)
-   [Searching for a File and Creating a Property Holding the File's Path](searching-for-a-file-and-creating-a-property-holding-the-file-s-path.md)
-   [Searching for a File in a Specific Location](searching-for-a-file-in-a-specific-location.md)
-   [Searching for a Registry Entry and Creating a Property Holding the Value of the Registry](searching-for-a-registry-entry-and-creating-a-property-holding-the-value-of-the-registry.md)

 

 



