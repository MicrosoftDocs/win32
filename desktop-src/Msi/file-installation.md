---
description: 'Once file costing has been completed, the installer has all the information required to process the two file manipulation actions: DuplicateFiles and MoveFiles.'
ms.assetid: 2e6d6eb3-1e71-46e6-a946-d9cc0b209325
title: File Installation
ms.topic: article
ms.date: 05/31/2018
---

# File Installation

Once [file costing](file-costing.md) has been completed, the installer has all the information required to process the two file manipulation actions: [DuplicateFiles](duplicatefiles-action.md) and [MoveFiles](movefiles-action.md).

Use the [DuplicateFiles action](duplicatefiles-action.md) to specify the files the installer is to duplicate in the [DuplicateFile table](duplicatefile-table.md). Use the [MoveFiles action](movefiles-action.md)to determine which files to move by querying the [MoveFile table](movefile-table.md).

Note that the Options field of the [MoveFile table](movefile-table.md) specifies whether or not the original file is to be deleted from its current location. Files that are moved or copied by the MoveFiles action are not deleted when the product is uninstalled.

The [InstallFiles action](installfiles-action.md) is called once all other file manipulation operations have completed. The InstallFiles action processes the [Media table](media-table.md), the [File table](file-table.md), and the [Component table](component-table.md) to determine which files will be copied from the source to the destination.

The [InstallFiles action](installfiles-action.md) creates the directory structure necessary to install all files. If an explicitly empty folder is required to be installed, the [CreateFolders action](createfolders-action.md) may be called to create it.

 

 



