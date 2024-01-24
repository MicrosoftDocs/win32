---
description: The RemoveFiles action removes files previously installed by the InstallFiles action.
ms.assetid: 1079be89-515c-443e-8927-46ddf7891a59
title: RemoveFiles Action
ms.topic: article
ms.date: 05/31/2018
---

# RemoveFiles Action

The RemoveFiles action removes files previously installed by the [InstallFiles](installfiles-action.md) action. Each of these files is gated by a link to an entry in the [Component](component-table.md) table. Only those files with components resolved to either the *msiInstallStateAbsent* state or the *msiInstallStateLocal* state if the component is installed locally, are removed.

## Sequence Restrictions

The [InstallValidate](installvalidate-action.md) action must be called before calling RemoveFiles. If an [InstallFiles](installfiles-action.md) action is used, it must appear after RemoveFiles.

## ActionData Messages



| Field | Description of action data                    |
|-------|-----------------------------------------------|
| \[1\] | Identifier of removed file.                   |
| \[9\] | Identifier of directory holding removed file. |



 

## Remarks

The [RemoveFile](removefile-table.md) table can be omitted from the installer database if there are no miscellaneous files to remove.

The RemoveFiles action can also remove author-specified files that are not installed by the InstallFiles action. These files are specified in the [RemoveFile](removefile-table.md) table. Each of these files is gated by a link to an entry in the [Component](component-table.md) table. Those files whose components are resolved to any active Action state (that is, not in the Off or Null state) are removed if the file exists in the specified directory. The removal of files specified in the RemoveFile table is attempted when the linked component is first installed, during a reinstall, and again when the linked component is removed.

The RemoveFiles action can also remove folders. An empty folder is removed if the value in the FileName column of the RemoveFile table is null.

When removing previously installed files, the RemoveFiles action queries the same fields in the same tables as those queried by the [InstallFiles](installfiles-action.md) action with the exception that the [Media table](media-table.md) is not used by the RemoveFiles action.

The target file name can be specified in localized text in the FileName column of the RemoveFile table.

 

 



