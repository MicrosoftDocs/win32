---
title: Version Information
description: This section discusses the version-information resource.
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\resources\versioninformation.htm'
keywords:
- resources,version information
- version information
- version numbers
ms.topic: article
ms.date: 05/31/2018
---

# Version Information

Version information makes it easier for applications to install files properly and enables setup programs to analyze files currently installed. The version-information resource contains the version number of the file, its intended operating system, and the original file name.

### In This Section



| Name                                                               | Description                                                        |
|--------------------------------------------------------------------|--------------------------------------------------------------------|
| [About Version Information](about-version-information.md)         | Discusses the version information functions.<br/>            |
| [Using Version Information](using-version-information.md)         | Discusses how to use the version information functions.<br/> |
| [Version Information Reference](version-information-reference.md) | Contains the API reference.<br/>                             |



 

### Version Information Functions



| Name                                                         | Description                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetFileVersionInfo**](/windows/desktop/api/Winver/nf-winver-getfileversioninfoa)             | Retrieves version information for the specified file. <br/>                                                                                                                                                                                                                                                                                                     |
| [**GetFileVersionInfoEx**](/windows/desktop/api/Winver/nf-winver-getfileversioninfoexa)         | Retrieves version information for the specified file.<br/>                                                                                                                                                                                                                                                                                                      |
| [**GetFileVersionInfoSize**](/windows/desktop/api/Winver/nf-winver-getfileversioninfosizea)     | Determines whether the operating system can retrieve version information for a specified file. If version information is available, [**GetFileVersionInfoSize**](/windows/desktop/api/Winver/nf-winver-getfileversioninfosizea) returns the size, in bytes, of that information. <br/>                                                                                                             |
| [**GetFileVersionInfoSizeEx**](/windows/desktop/api/Winver/nf-winver-getfileversioninfosizeexa) | Determines whether the operating system can retrieve version information for a specified file. If version information is available, [**GetFileVersionInfoSizeEx**](/windows/desktop/api/Winver/nf-winver-getfileversioninfosizeexa) returns the size, in bytes, of that information.<br/>                                                                                                          |
| [**VerFindFile**](/windows/desktop/api/Winver/nf-winver-verfindfilea)                           | Determines where to install a file based on whether it locates another version of the file in the system. The values [**VerFindFile**](/windows/desktop/api/Winver/nf-winver-verfindfilea) returns in the specified buffers are used in a subsequent call to the [**VerInstallFile**](/windows/desktop/api/Winver/nf-winver-verinstallfilea) function. <br/>                                                                          |
| [**VerInstallFile**](/windows/desktop/api/Winver/nf-winver-verinstallfilea)                     | Installs the specified file based on information returned from the [**VerFindFile**](/windows/desktop/api/Winver/nf-winver-verfindfilea) function. [**VerInstallFile**](/windows/desktop/api/Winver/nf-winver-verinstallfilea) decompresses the file, if necessary, assigns a unique filename, and checks for errors, such as outdated files. <br/>                                                                                   |
| [**VerLanguageName**](/windows/desktop/api/Winver/nf-winver-verlanguagenamea)                   | Retrieves a description string for the language associated with a specified binary Microsoft language identifier.<br/>                                                                                                                                                                                                                                          |
| [**VerQueryValue**](/windows/desktop/api/Winver/nf-winver-verqueryvaluea)                       | Retrieves specified version information from the specified version-information resource. To retrieve the appropriate resource, before you call [**VerQueryValue**](/windows/desktop/api/Winver/nf-winver-verqueryvaluea), you must first call the [**GetFileVersionInfoSize**](/windows/desktop/api/Winver/nf-winver-getfileversioninfosizea) function, and then the [**GetFileVersionInfo**](/windows/desktop/api/Winver/nf-winver-getfileversioninfoa) function. <br/> |



 

### Version Information Structures



| Name                                          | Description                                                                                                                                                                                                                      |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**String**](string-str.md)                  | Depicts the organization of data in a file-version resource. It contains a string that describes a specific aspect of a file, for example, a file's version, its copyright notices, or its trademarks.<br/>                |
| [**StringFileInfo**](stringfileinfo.md)      | Depicts the organization of data in a file-version resource. It contains version information that can be displayed for a particular language and code page.<br/>                                                           |
| [**StringTable**](stringtable.md)            | Depicts the organization of data in a file-version resource. It contains language and code page formatting information for the strings specified by the **Children** member. A code page is an ordered character set.<br/> |
| [**Var**](var-str.md)                        | Depicts the organization of data in a file-version resource. It typically contains a list of language and code page identifier pairs that the version of the application or DLL supports.<br/>                             |
| [**VarFileInfo**](varfileinfo.md)            | Depicts the organization of data in a file-version resource. It contains version information not dependent on a particular language and code page combination.<br/>                                                        |
| [**VS\_FIXEDFILEINFO**](/windows/win32/api/verrsrc/ns-verrsrc-vs_fixedfileinfo) | Contains version information about a file. This information is language and code page independent. <br/>                                                                                                                   |
| [**VS\_VERSIONINFO**](vs-versioninfo.md)     | Depicts the organization of data in a file-version resource. It is the root structure that contains all other file-version information structures.<br/>                                                                    |



 

 

 





