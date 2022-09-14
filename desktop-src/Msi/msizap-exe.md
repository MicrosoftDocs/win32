---
description: Msizap.exe is a command line utility that removes either all Windows Installer information for a product or all products installed on a computer. Products installed by the installer may fail to function after using Msizap.
ms.assetid: 0debb8ab-3ae7-447e-84fc-0466ec1b2f26
title: Msizap.exe
ms.topic: article
ms.date: 05/31/2018
---

# Msizap.exe

Msizap.exe is a command line utility that removes either all Windows Installer information for a product or all products installed on a computer. Products installed by the installer may fail to function after using Msizap.

On Windows 2000 and Windows XP, administrative privileges are required to use Msizap.exe.

This tool is only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md) and should not be redistributed. Use the recent version of Msizap.exe (version 3.1.4000.2726 or greater) that is available in the Windows SDK Components for Windows Installer Developers for Windows Vista or greater. Lesser versions of Msizap.exe can remove information about all updates that have been applied to other applications on the user's computer. If this information is removed, these other applications may need to be removed and reinstalled to receive additional updates.

## Syntax

**msizap T***\[WA!\]{product code}*

**msizap T***\[WA!\]\<msi package\>*

**msizap \****\[WA!\]* **ALLPRODUCTS**

**msizap PWSA?!**

## Command Line Options

Msizap.exe uses case-insensitive command line options shown in the following table.



| Option | Description                                                                                                                                                                                                                                                   |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \*     | Removes all Windows Installer folders and registry keys, adjusts shared DLL counts, and stops Windows Installer service. Also removes the In-Progress key and rollback information.                                                                           |
| a      | Only changes ACLs to Admin Full Control for any specified removal.                                                                                                                                                                                            |
| g      | For all users, removes any cached Windows Installer data files that have been orphaned.                                                                                                                                                                       |
| p      | Removes the In-Progress key.                                                                                                                                                                                                                                  |
| s      | Removes Rollback Information.                                                                                                                                                                                                                                 |
| t      | Removes all information for the specified product code. When using this option, enclose the Product Code in curly braces. This option may be used with either the full path to the .msi file or with the product code.                                        |
| w      | Removes Windows Installer information for all users. When this option is not set, only the information for the current user is removed. Use of this option requires that the user's profile be loaded so that the user's per-user registry hive be available. |
| ?      | Verbose help.                                                                                                                                                                                                                                                 |
| !      | Forces a 'yes' response to any prompt.                                                                                                                                                                                                                        |



 

## Related topics

<dl> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 



