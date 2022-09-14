---
description: A cabinet is a single file, usually with a .cab extension, that stores compressed files in a file library.
ms.assetid: df240302-b875-49bf-8e62-7a35204c35fb
title: Cabinet Files
ms.topic: article
ms.date: 05/31/2018
---

# Cabinet Files

A cabinet is a single file, usually with a .cab extension, that stores compressed files in a file library. The cabinet format is an efficient way to package multiple files because compression is performed across file boundaries, which significantly improves the compression ratio.

Developers can use a cabinet file creation tool such as Makecab.exe to make cabinet files for use with installer packages. The Makecab.exe utility is included in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

Developers can also use a cabinet file creation tool such as Cabarc.exe to make cabinet files for use with installer packages. This tool writes to the Diamond cabinet structure.

The file keys of the files stored inside of a cabinet file must match the entries in the File column of the [File table](file-table.md) and the sequence of files in the cabinet must match the file sequence specified in the Sequence column. For more information, see [Using Cabinets and Compressed Sources](using-cabinets-and-compressed-sources.md).

Large files can be split between two or more cabinet files. There can be no more than 15 files in any one cabinet file that spans to the next cabinet file. For example, if you have three cabinet files the first cabinet can have 15 files that span to the second cabinet file and the second cabinet file can have 15 files that span to the third cabinet file.

The installer extracts files from a cabinet as they are needed by the installation and installs them in the same order as they are stored in the cabinet file. The space requirements for installing a file stored in a cabinet are no different than for installing an uncompressed file.

A cabinet file can be located inside or outside of the .msi file. Beginning with Windows Installer 5.0 running on Windows 7 or Windows Server 2008 R2 the installer saves any cabinets that are embedded in the .msi file before caching the installation package.

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** To conserve disk space, the installer always removes any cabinets that are embedded in the .msi file before caching the installation package on the user's computer.

 

 



