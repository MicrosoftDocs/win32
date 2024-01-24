---
description: The PatchFiles action queries the Patch table to determine which patches are to be applied. The PatchFiles action also performs the byte-wise patching of the files.
ms.assetid: 4026755e-a006-40c0-8816-de5358f4582e
title: PatchFiles Action
ms.topic: article
ms.date: 05/31/2018
---

# PatchFiles Action

The PatchFiles action queries the [Patch table](patch-table.md) to determine which patches are to be applied. The PatchFiles action also performs the byte-wise patching of the files.

## Sequence Restrictions

If the file that is to be patched is not installed, the PatchFiles action must come after the [InstallFiles action](installfiles-action.md) that installs the file. Previously installed files may be patched at any point in the action sequence. The [DuplicateFiles Action](duplicatefiles-action.md) must come after the PatchFiles action to prevent duplicating the unpatched version of the file.

## ActionData Messages



| Field | Description of action data                    |
|-------|-----------------------------------------------|
| \[1\] | Identifier of patched file.                   |
| \[2\] | Identifier of directory holding patched file. |
| \[3\] | Size of patch in bytes.                       |



 

 

 



