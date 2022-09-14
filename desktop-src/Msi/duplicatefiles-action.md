---
description: The DuplicateFiles action duplicates files installed by the InstallFiles action. The duplicate files can be copied to the same directory with a different name or to a different directory with the original name.
ms.assetid: 51cc0b3f-aa01-4f4d-9a4d-add832698061
title: DuplicateFiles Action
ms.topic: article
ms.date: 05/31/2018
---

# DuplicateFiles Action

The DuplicateFiles action duplicates files installed by the [InstallFiles](installfiles-action.md) action. The duplicate files can be copied to the same directory with a different name or to a different directory with the original name.

## Sequence Restrictions

The DuplicateFiles action must come after the [InstallFiles action](installfiles-action.md). The DuplicateFiles Action must also come after the [PatchFiles action](patchfiles-action.md) to prevent duplicating the unpatched version of the file.

## ActionData Messages



| Field | Description of action data                       |
|-------|--------------------------------------------------|
| \[1\] | Identifier of duplicated file.                   |
| \[6\] | Size of duplicated file.                         |
| \[9\] | Identifier of directory holding duplicated file. |



 

## Remarks

The DuplicateFiles action processes a [DuplicateFile table](duplicatefile-table.md) entry only if the component linked to that entry is being installed locally. For more information, see [Component table](component-table.md).

The string in the DestFolder field is a property name whose value is expected to resolve to a fully qualified path. This property can either be any of the directory entries in the [Directory](directory-table.md) table, any pre-defined folder property ([**CommonFilesFolder**](commonfilesfolder.md), for example), or a property set by any entry in the [AppSearch](appsearch-table.md) table. If the **DestFolder** property does not evaluate to a valid path the DuplicateFiles action does nothing for that entry.

If the name of the destination file in the DestName column of the DuplicateFile table is left blank, the destination file name will be the same as the original file name.

Files installed by the DuplicateFiles action are removed by the [RemoveDuplicateFiles](removeduplicatefiles-action.md) action when appropriate.

 

 



