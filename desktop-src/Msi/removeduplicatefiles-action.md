---
description: The RemoveDuplicateFiles action deletes files installed by the DuplicateFiles action.
ms.assetid: 3d8ba4c5-775f-471e-a479-32fa6f7a1bf0
title: RemoveDuplicateFiles Action
ms.topic: article
ms.date: 05/31/2018
---

# RemoveDuplicateFiles Action

The RemoveDuplicateFiles action deletes files installed by the [DuplicateFiles](duplicatefiles-action.md) action.

## Sequence Restrictions

The RemoveDuplicateFiles action must occur after the [InstallValidate](installvalidate-action.md) action and before the [InstallFiles](installfiles-action.md) action.

## ActionData Messages



| Field | Description of action data                    |
|-------|-----------------------------------------------|
| \[1\] | Identifier of removed file.                   |
| \[9\] | Identifier of directory holding removed file. |



 

## Remarks

To delete a file duplicated with the [DuplicateFiles action](duplicatefiles-action.md) using the RemoveDuplicateFiles action, the component associated with the file's entry in the DuplicateFile table must be selected for removal.

Use the DestFolder column of the [DuplicateFile table](duplicatefile-table.md) to specify the property name whose value identifies the destination folder.

 

 



