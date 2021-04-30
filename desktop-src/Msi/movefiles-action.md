---
description: The MoveFiles action locates existing files on the user's computer and moves or copies those files to a new location.
ms.assetid: f08f751d-877b-4b17-8015-7108d5fd8195
title: MoveFiles Action
ms.topic: article
ms.date: 05/31/2018
---

# MoveFiles Action

The MoveFiles action locates existing files on the user's computer and moves or copies those files to a new location. The MoveFiles action queries the [MoveFile table](movefile-table.md) and moves files specified there if the component linked to the entries is specified to be install locally or is being run from source.

## Sequence Restrictions

The MoveFiles action must come after the [InstallValidate](installvalidate-action.md) action and before the [InstallFiles](installfiles-action.md) action.

## ActionData Messages



| Field | Description of action data                  |
|-------|---------------------------------------------|
| \[1\] | Identifier of moved file.                   |
| \[6\] | Size of installed file in bytes.            |
| \[9\] | Identifier of directory holding moved file. |



 

## Remarks

The MoveFiles table contain a column named "options" which specifies the source files to be moved or copied. A moved source file is deleted after it has been copied to a new location. For the exact syntax, see the [MoveFile table](movefile-table.md).

The SourceFolder and DestFolder columns of the MoveFile table are property names whose values are expected to resolve to fully qualified paths. These properties can be any of the directory entries in the [Directory](directory-table.md) table, any predefined folder property ([**FavoritesFolder**](favoritesfolder.md), for example), or a property set by any entry in the [AppSearch](appsearch-table.md) table. These properties may contain a full path containing the file name to a specific file. For example, the AppSearch table can be authored to search for a particular file and set a property to the full path to that file. In this example, the SourceName column in the MoveFile table can be left blank to indicate that the value in the SourceFolder property contains a full file path. The semicolon is the list delimiter for transforms, sources, and patches and should not be used in file names or paths.

The MoveFiles action does not act on entries in the MoveFile table in which either the SourceFolder or DestFolder property does not evaluate to a full path.

The MoveFiles action attempts to move or copy all files in the source directory that match the name given in the SourceName column of the MoveFiles table. The name in the SourceName column can include either the \* or ? wildcards which allow a group of files to be moved or copied. For example, the SourceName column may contain an entry of "\*.xls" and the MoveFiles action moves or copies every Microsoft Excel workbook from the source directory to the destination.

The name to be given to the destination file can be specified in the DestName column of the MoveFile table. The destination file name retains the source file name if this column is left blank.

If a "\*" wildcard is entered in the SourceName column of the [MoveFile table](movefile-table.md) and a destination file name is specified in the DestName column, all moved or copied files retain the names in the sources.

Files that are moved or copied by the MoveFiles action are not deleted when the product is uninstalled.

 

 



