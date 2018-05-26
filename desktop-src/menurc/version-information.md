---
title: Version Information
description: This section discusses the version-information resource.
ms.assetid: 63fb6c0f-11b3-4d70-b1ba-56086cb02847
keywords:
- resources,version information
- version information
- version numbers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| [**GetFileVersionInfo**](/windows/win32/Winver/nf-winver-getfileversioninfoa?branch=master)             | Retrieves version information for the specified file. <br/>                                                                                                                                                                                                                                                                                                     |
| [**GetFileVersionInfoEx**](/windows/win32/Winver/nf-winver-getfileversioninfoexa?branch=master)         | Retrieves version information for the specified file.<br/>                                                                                                                                                                                                                                                                                                      |
| [**GetFileVersionInfoSize**](/windows/win32/Winver/nf-winver-getfileversioninfosizea?branch=master)     | Determines whether the operating system can retrieve version information for a specified file. If version information is available, [**GetFileVersionInfoSize**](/windows/win32/Winver/nf-winver-getfileversioninfosizea?branch=master) returns the size, in bytes, of that information. <br/>                                                                                                             |
| [**GetFileVersionInfoSizeEx**](/windows/win32/Winver/nf-winver-getfileversioninfosizeexa?branch=master) | Determines whether the operating system can retrieve version information for a specified file. If version information is available, [**GetFileVersionInfoSizeEx**](/windows/win32/Winver/nf-winver-getfileversioninfosizeexa?branch=master) returns the size, in bytes, of that information.<br/>                                                                                                          |
| [**VerFindFile**](/windows/win32/Winver/nf-winver-verfindfilea?branch=master)                           | Determines where to install a file based on whether it locates another version of the file in the system. The values [**VerFindFile**](/windows/win32/Winver/nf-winver-verfindfilea?branch=master) returns in the specified buffers are used in a subsequent call to the [**VerInstallFile**](/windows/win32/Winver/nf-winver-verinstallfilea?branch=master) function. <br/>                                                                          |
| [**VerInstallFile**](/windows/win32/Winver/nf-winver-verinstallfilea?branch=master)                     | Installs the specified file based on information returned from the [**VerFindFile**](/windows/win32/Winver/nf-winver-verfindfilea?branch=master) function. [**VerInstallFile**](/windows/win32/Winver/nf-winver-verinstallfilea?branch=master) decompresses the file, if necessary, assigns a unique filename, and checks for errors, such as outdated files. <br/>                                                                                   |
| [**VerLanguageName**](/windows/win32/Winver/nf-winver-verlanguagenamea?branch=master)                   | Retrieves a description string for the language associated with a specified binary Microsoft language identifier.<br/>                                                                                                                                                                                                                                          |
| [**VerQueryValue**](/windows/win32/Winver/nf-winver-verqueryvaluea?branch=master)                       | Retrieves specified version information from the specified version-information resource. To retrieve the appropriate resource, before you call [**VerQueryValue**](/windows/win32/Winver/nf-winver-verqueryvaluea?branch=master), you must first call the [**GetFileVersionInfoSize**](/windows/win32/Winver/nf-winver-getfileversioninfosizea?branch=master) function, and then the [**GetFileVersionInfo**](/windows/win32/Winver/nf-winver-getfileversioninfoa?branch=master) function. <br/> |



 

### Version Information Structures



| Name                                          | Description                                                                                                                                                                                                                      |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**String**](string-str.md)                  | Depicts the organization of data in a file-version resource. It contains a string that describes a specific aspect of a file, for example, a file's version, its copyright notices, or its trademarks.<br/>                |
| [**StringFileInfo**](stringfileinfo.md)      | Depicts the organization of data in a file-version resource. It contains version information that can be displayed for a particular language and code page.<br/>                                                           |
| [**StringTable**](stringtable.md)            | Depicts the organization of data in a file-version resource. It contains language and code page formatting information for the strings specified by the **Children** member. A code page is an ordered character set.<br/> |
| [**Var**](var-str.md)                        | Depicts the organization of data in a file-version resource. It typically contains a list of language and code page identifier pairs that the version of the application or DLL supports.<br/>                             |
| [**VarFileInfo**](varfileinfo.md)            | Depicts the organization of data in a file-version resource. It contains version information not dependent on a particular language and code page combination.<br/>                                                        |
| [**VS\_FIXEDFILEINFO**](/windows/win32/VerRsrc/ns-verrsrc-tagvs_fixedfileinfo?branch=master) | Contains version information about a file. This information is language and code page independent. <br/>                                                                                                                   |
| [**VS\_VERSIONINFO**](vs-versioninfo.md)     | Depicts the organization of data in a file-version resource. It is the root structure that contains all other file-version information structures.<br/>                                                                    |



 

 

 





