---
description: The Windows SDK Components for Windows Installer Developers contains VBScript files that show you how the Windows Installer automation interface is used to modify Windows Installer packages.
ms.assetid: 93747a8d-32e0-4f31-a5cf-f95fb26b97df
title: Windows Installer Scripting Examples
ms.topic: article
ms.date: 05/31/2018
---

# Windows Installer Scripting Examples

The [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md) contains VBScript files that show you how the Windows Installer automation interface is used to modify Windows Installer packages.

The script samples identified in this topic are not supported by Microsoft Corporation, and they are provided only as a potentially useful reference. Running these samples requires the Windows Script Host. For more information about Windows Script Host, see the [Windows Script Host](/previous-versions//9bbdkx3k(v=vs.85)) section of the Microsoft Windows Software Development Kit (SDK).



| Sample Script File | Description                                                                                                 |
|--------------------|-------------------------------------------------------------------------------------------------------------|
| WiLstPrd.vbs       | [List Products, Properties, Features, and Components](list-products-properties-features-and-components.md) |
| WiImport.vbs       | [Import Files](import-files.md)                                                                            |
| WiExport.vbs       | [Export Files](export-files.md)                                                                            |
| WiSubStg.vbs       | [Manage Substorages](manage-substorages.md)                                                                |
| WiStream.vbs       | [Manage Binary Streams](manage-binary-streams.md)                                                          |
| WiMerge.vbs        | [Merge Two Databases](merge-two-databases.md)                                                              |
| WiGenXfm.vbs       | [Generate a Transform](generate-a-transform.md)                                                            |
| WiUseXfm.vbs       | [Apply a Transform](apply-a-transform.md)                                                                  |
| WiLstXfm.vbs       | [View a Transform](view-a-transform.md) (CSCRIPT only)                                                     |
| WiDiffDb.vbs       | [View Differences Between Two Databases](view-differences-between-two-databases.md) (CSCRIPT only)         |
| WiLstScr.vbs       | [View Installer Script](view-installer-script.md) (CSCRIPT only)                                           |
| WiSumInf.vbs       | [Manage Summary Information](manage-summary-information.md)                                                |
| WiPolicy.vbs       | [Manage Policy Settings](manage-policy-settings.md)                                                        |
| WiLangId.vbs       | [Manage Language and Codepage](manage-language-and-codepage.md)                                            |
| WiToAnsi.vbs       | [Copy a Unicode File to an Ansi File](copy-a-unicode-file-to-an-ansi-file.md)                              |
| WiFilVer.vbs       | [Manage File Sizes and Versions](manage-file-sizes-and-versions.md)                                        |
| WiMakCab.vbs       | [Generate File Cabinet](generate-file-cabinet.md)                                                          |
| WiRunSQL.vbs       | [Execute SQL Statements](execute-sql-statements.md)                                                        |
| WiTextIn.vbs       | [Copy ANSI File Into a Database Field](copy-ansi-file-into-a-database-field.md)                            |
| WiCompon.vbs       | [List Components](list-components.md)                                                                      |
| WiFeatur.vbs       | [List Features](list-features.md)                                                                          |
| WiDialog.vbs       | [Preview User Interface](preview-user-interface.md)                                                        |



 

All these scripts display a help screen that describes their command line arguments. To display the help screen in Windows double-click the file. To display the help screen from a command line enter a ? as the first argument, or enter fewer arguments than required. Scripts return a value of 0 for success, 1 if help is invoked, and 2 if in case of failure.

These samples require Windows Script Host to run. Windows Script Host is actually two hosts:

-   CScript.exe is the version that enables you to run scripts from the command prompt, and provides command-line switches for setting script properties.
-   WScript.exe is the version of Windows Script Host that enables you to run scripts from Windows. For more information, see the [Windows Script Host](/previous-versions//9bbdkx3k(v=vs.85)) section in the Windows SDK.

The Makecab.exe utility is included with the patching samples in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

For information about WMI, see [Using Windows Installer with WMI](using-windows-installer-with-wmi.md).

 

 
