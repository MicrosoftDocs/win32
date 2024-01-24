---
description: The Locator Tables group is used to locate files and applications.
ms.assetid: 44ab770b-1a7f-4590-9681-8f6bd343bf86
title: Locator Tables Group
ms.topic: article
ms.date: 05/31/2018
---

# Locator Tables Group

The Locator Tables group is used to locate files and applications. To search for a file, first determine the file signature and then locate the file. The Locator tables are used to search the registry, installer configuration data, directory tree, or .ini files for the unique signature of a file. The file signature can then be checked in the [Signature table](signature-table.md) to ascertain that a particular file is really the file being sought and not another file with the same name. If a record in a locator table does not contain a key into the Signature table, then the record refers to a directory and not a file.

The component controlling a file is found in the [File table](file-table.md) through the external key to the [Component table](component-table.md). The installer resolves the location of a file through the Component table because every file belongs to one component. The location of a component is found through an external key in the Component table to the [Directory table](directory-table.md).

The location of an application is found by searching for files that make up the application. The installer also provides two tables for searching for previous versions of an application: the [AppSearch table](appsearch-table.md) and the [CCPSearch table](ccpsearch-table.md).

The following tables make up the Locator tables group and are used to determine the file signature.

-   The [RegLocator table](reglocator-table.md) holds the information needed to search for a file or directory in the registry.
-   The [IniLocator table](inilocator-table.md) holds the information needed to search for a .ini file. The .ini file must be present in the default Microsoft Windows directory.
-   The [CompLocator table](complocator-table.md) holds the information needed to search for a file or a directory using the installer's configuration data.
-   The [DrLocator table](drlocator-table.md) holds the information needed to search for a file or directory in the directory tree.
-   The [AppSearch table](appsearch-table.md) contains the properties that must be set to the search result of a corresponding file signature.
-   The [CCPSearch table](ccpsearch-table.md) contains the list of file signatures, at least one of which needs to be present on a user's computer for the Compliance Checking Program (CCP).

 

 



