---
description: When installing an assembly to an isolated location for a specific application, the application must be specified in the File\_Application column of the MsiAssembly table.
ms.assetid: 8d7fc09c-1017-4a30-be00-b7b0e5f2a057
title: Installing and Removing Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# Installing and Removing Assemblies

When installing an assembly to an isolated location for a specific application, the application must be specified in the File\_Application column of the [MsiAssembly table](msiassembly-table.md). This field is a key into the [File table](file-table.md). The installer uses the directory structure that is specified in the [Directory table](directory-table.md) to install the assembly into the same directory as the component that contains this file.

When installing an assembly to the global assembly cache, the value in the File\_Application column of the [MsiAssembly Table](msiassembly-table.md) must be Null.

The following sections describe the installation of Win32 and common language runtime assemblies:

-   [Installation of Win32 Assemblies](installation-of-win32-assemblies.md)
-   [Installation of Common Language Runtime Assemblies](installation-of-common-language-runtime-assemblies.md)

 

 



