---
description: MsiFiler.exe populates the File table with file versions, languages, and sizes based upon a source directory. It can also update the MsiFileHash table with file hashes.
ms.assetid: cc3db60b-0b1d-4582-8b40-0b55f83e00be
title: Msifiler.exe
ms.topic: article
ms.date: 05/31/2018
---

# Msifiler.exe

MsiFiler.exe populates the [File table](file-table.md) with file versions, languages, and sizes based upon a source directory. It can also update the [MsiFileHash table](msifilehash-table.md) with file hashes.

## Syntax

**msifiler.exe -d** *{database}* **\[-v\] \[-h\] \[-s ALTSOURCE\]**

## Command Line Options

Msifiler.exe uses the following case-insensitive command line options. A slash delimiter may also be used in place of a dash.



| Option | Parameter   | Description                                                                                                                                                                  |
|--------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -d     | *database*  | The database (.msi file) that is to be updated.                                                                                                                              |
| -v     |             | Use verbose mode.                                                                                                                                                            |
| -h     |             | Populate the [MsiFileHash table](msifilehash-table.md). This creates the table if it does not already exist. The MsiFileHash table can only be used with unversioned files. |
| -s     | *ALTSOURCE* | ALTSOURCE specifies an alternative directory to find the files.                                                                                                              |



 

This tool is only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

## Related topics

<dl> <dt>

[Windows Installer Development Tools](windows-installer-development-tools.md)
</dt> <dt>

[Using the Directory Table](using-the-directory-table.md)
</dt> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 



