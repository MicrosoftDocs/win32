---
description: The VBScript file WiSumInf.vbs is provided in the Windows SDK Components for Windows Installer Developers. This sample script can be used to manage the summary information stream of a Windows Installer package.
ms.assetid: f7f1cf89-f211-4511-8260-b48c898c1cf6
title: Manage Summary Information
ms.topic: article
ms.date: 05/31/2018
---

# Manage Summary Information

The VBScript file WiSumInf.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample script can be used to manage the [summary information stream](summary-information-stream.md) of a Windows Installer package.

The sample demonstrates the use of:

-   [**SummaryInformation property (Installer Object)**](installer-summaryinformation.md)
-   [**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer object**](installer-object.md)

Using this sample requires the CScript.exe or WScript.exe version of Windows Script Host. To use CScript.exe to run this sample, type a command at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiSumInf.vbs \[path to database\]\[Property=value\]**

Specify the path to the Windows Installer database. If no other arguments are specified, the script lists all the summary properties for the package. Specify a list of summary properties and values to be updated using the format Property=value. You may specify the property by either the name or PID value shown below. Date and time fields use current locale format, or "Now" or "Date". For more information, see [Summary Information Stream Property Set](summary-information-stream-property-set.md).



| PID | Name        | Description                                                                                                                                                                                                                                                                                      |
|-----|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Codepage    | ANSI codepage of text strings in summary information. For more information, see [**Codepage Summary**](codepage-summary.md) Property.                                                                                                                                                           |
| 2   | Title       | Type of Windows Installer package. For more information, see [**Title Summary Property**](title-summary.md).                                                                                                                                                                                    |
| 3   | Subject     | Full Product name . For more information, see [**Subject Summary Property**](subject-summary.md).                                                                                                                                                                                               |
| 4   | Author      | Creator, typically vendor name. For more information, see [**Author Summary Property**](author-summary.md).                                                                                                                                                                                     |
| 5   | Keywords    | List of keywords for use by file browser. For more information, see [**Keywords Summary Property**](keywords-summary.md).                                                                                                                                                                       |
| 6   | Comments    | Description of purpose or use of package. For more information, see [**Comments Summary Property**](comments-summary.md).                                                                                                                                                                       |
| 7   | Template    | Supported platforms and languages. For more information, see [**Template Summary Property**](template-summary.md).                                                                                                                                                                              |
| 8   | LastAuthor  | Set only by the installer. For more information, see [**Last Saved By Summary Property**](last-saved-by-summary.md).                                                                                                                                                                            |
| 9   | Revision    | Package code GUID. For more information, see [**Revision Number Summary Property**](revision-number-summary.md).                                                                                                                                                                                |
| 11  | Printed     | Date and time of installation image. For more information, see [**Last Printed Summary Property**](last-printed-summary.md).                                                                                                                                                                    |
| 12  | Created     | Date and time of package creation. For more information, see [**Create Time/Date Summary Property**](create-time-date-summary.md).                                                                                                                                                              |
| 13  | Saved       | Date and time of last package modification. For more information, see [**Last Saved Time/Date Summary Property**](last-saved-time-date-summary.md).                                                                                                                                             |
| 14  | Pages       | Minimum version of Windows Installer required for this package. For more information, see [**Page Count Summary Property**](page-count-summary.md).                                                                                                                                             |
| 15  | Words       | Type of source file image. For more information, see [**Word Count Summary Property**](word-count-summary.md).Starting with Windows Installer version 4.0 on Windows Vista and Windows Server 2008, this property includes bits to specify whether elevated privileges are required.<br/> |
| 16  | Characters  | Used for transforms only. [**Character Count**](character-count-summary.md).                                                                                                                                                                                                                    |
| 18  | Application | Application associated with this file, i.e. "Windows Installer". For more information, see [**Creating Application Summary Property**](creating-application-summary.md).                                                                                                                        |
| 19  | Security    | Security setting. For more information, see [**Security Summary Property**](security-summary.md).                                                                                                                                                                                               |



 

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 




