---
description: Msimerg.exe is a command line utility that uses MsiDatabaseMerge to merge a reference database into a base database.
ms.assetid: db0c9ae5-a8e8-4eff-ae14-67dcce352483
title: Msimerg.exe
ms.topic: article
ms.date: 05/31/2018
---

# Msimerg.exe

Msimerg.exe is a command line utility that uses [**MsiDatabaseMerge**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabasemergea) to [merge](merges-and-transforms.md) a reference database into a base database.

This tool is only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

## Syntax

**Msimerg** *{base database}{reference database}*

If there is a merge conflict between the two databases, the conflict information is placed in the \_MergeErrors table.

## Command Line Options

None.

## Related topics

<dl> <dt>

[Windows Installer Development Tools](windows-installer-development-tools.md)
</dt> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 



