---
description: The directories in the Directory table specify the layout of an installation.
ms.assetid: 59f6ae09-d013-46d7-a1a7-0543f31ac487
title: Using a Directory Property in a Path
ms.topic: article
ms.date: 05/31/2018
---

# Using a Directory Property in a Path

The directories in the [Directory table](directory-table.md) specify the layout of an installation. When the Windows Installer resolves these directories during the [CostFinalize action](costfinalize-action.md), the keys in the Directory table become [properties](properties.md) set to directory paths. The installer also always sets a number of standard [System Folder Properties](property-reference.md) to system folder paths.

The values of the [System Folder Properties](property-reference.md) are guaranteed to end in a directory separator. The values of all other properties entered in the [Directory table](directory-table.md) are only guaranteed to end in a directory separator after the installer has run the [CostFinalize action](costfinalize-action.md). Before costing has completed, the values of properties entered in the Directory table which are not [System Folder Properties](property-reference.md) may not end in a directory separator. Therefore, if your installation sets directory properties using [custom actions](custom-actions.md) in the package, the values on reference might not end with a directory separator.

Directory properties ending with a directory separator can therefore be used in a path string without explicitly including the directory separator. For example, if the value of DirectoryProperty ends with a directory separator, the following string correctly specifies the path to *file* in *subdirectory*

``` syntax
[DirectoryProperty]subdirectory\file
```

and the following path string is incorrect.

``` syntax
[DirectoryProperty]\subdirectory\file
```

 

 



