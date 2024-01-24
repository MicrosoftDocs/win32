---
description: The VBScript file WiLangID.vbs is provided in the Windows SDK Components for Windows Installer Developers.
ms.assetid: 319e9ffd-ff9f-4b4c-913e-2c571f2ec9ee
title: Manage Language and Codepage
ms.topic: article
ms.date: 05/31/2018
---

# Manage Language and Codepage

The VBScript file WiLangID.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample shows how script is used to access a package's language information and codepage. For more information, see [Localizing a Windows Installer Package](localizing-a-windows-installer-package.md) and [Code Page Handling (Windows Installer)](code-page-handling-windows-installer-.md).

The sample demonstrates the use of:

-   [**OpenDatabase method (Installer Object)**](installer-opendatabase.md)
-   [**CreateRecord method**](installer-createrecord.md)
-   [**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer object**](installer-object.md)
-   [**OpenView method**](database-openview.md)
-   [**SummaryInformation property (Database Object)**](database-summaryinformation.md) of the [**Database object**](database-object.md)

Using this sample requires the CScript.exe or WScript.exe version of Windows Script Host. To use CScript.exe to run this sample, type a command at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiLangID.vbs \[path to database\]\[keyword\]\[value\]**

Specify the path to the Windows Installer database. To change a value specify one of the following keywords followed by the new value. If no value is specified the sample returns the current value.



| Keyword      | Description                                                                                                                                                                                |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Package**  | The language versions supported by the database. For information, see [**Template Summary**](template-summary.md) property.                                                               |
| **Product**  | Language the installer should use for any strings in the user interface that are not authored into the database. For information, see [**ProductLanguage**](productlanguage.md) property. |
| **Codepage** | Single ANSI code page for the string pool. For information, see [Code Page Handling (Windows Installer)](code-page-handling-windows-installer-.md).                                       |



 

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host see [Windows Installer Development Tools](windows-installer-development-tools.md).

For more information, see [Determining an Installation Database's Code Page](determining-an-installation-database-s-code-page.md) and [Setting the Code Page of a Database](setting-the-code-page-of-a-database.md).

 

 



