---
title: Version Information
description: This section discusses the version-information resource.
ms.assetid: '63fb6c0f-11b3-4d70-b1ba-56086cb02847'
keywords: ["resources,version information", "version information", "version numbers"]
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
| [**GetFileVersionInfo**](getfileversioninfo.md)             | Retrieves version information for the specified file. <br/>                                                                                                                                                                                                                                                                                                     |
| [**GetFileVersionInfoEx**](getfileversioninfoex.md)         | Retrieves version information for the specified file.<br/>                                                                                                                                                                                                                                                                                                      |
| [**GetFileVersionInfoSize**](getfileversioninfosize.md)     | Determines whether the operating system can retrieve version information for a specified file. If version information is available, [**GetFileVersionInfoSize**](getfileversioninfosize.md) returns the size, in bytes, of that information. <br/>                                                                                                             |
| [**GetFileVersionInfoSizeEx**](getfileversioninfosizeex.md) | Determines whether the operating system can retrieve version information for a specified file. If version information is available, [**GetFileVersionInfoSizeEx**](getfileversioninfosizeex.md) returns the size, in bytes, of that information.<br/>                                                                                                          |
| [**VerFindFile**](verfindfile.md)                           | Determines where to install a file based on whether it locates another version of the file in the system. The values [**VerFindFile**](verfindfile.md) returns in the specified buffers are used in a subsequent call to the [**VerInstallFile**](verinstallfile.md) function. <br/>                                                                          |
| [**VerInstallFile**](verinstallfile.md)                     | Installs the specified file based on information returned from the [**VerFindFile**](verfindfile.md) function. [**VerInstallFile**](verinstallfile.md) decompresses the file, if necessary, assigns a unique filename, and checks for errors, such as outdated files. <br/>                                                                                   |
| [**VerLanguageName**](verlanguagename.md)                   | Retrieves a description string for the language associated with a specified binary Microsoft language identifier.<br/>                                                                                                                                                                                                                                          |
| [**VerQueryValue**](verqueryvalue.md)                       | Retrieves specified version information from the specified version-information resource. To retrieve the appropriate resource, before you call [**VerQueryValue**](verqueryvalue.md), you must first call the [**GetFileVersionInfoSize**](getfileversioninfosize.md) function, and then the [**GetFileVersionInfo**](getfileversioninfo.md) function. <br/> |



 

### Version Information Structures



| Name                                          | Description                                                                                                                                                                                                                      |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**String**](string-str.md)                  | Depicts the organization of data in a file-version resource. It contains a string that describes a specific aspect of a file, for example, a file's version, its copyright notices, or its trademarks.<br/>                |
| [**StringFileInfo**](stringfileinfo.md)      | Depicts the organization of data in a file-version resource. It contains version information that can be displayed for a particular language and code page.<br/>                                                           |
| [**StringTable**](stringtable.md)            | Depicts the organization of data in a file-version resource. It contains language and code page formatting information for the strings specified by the **Children** member. A code page is an ordered character set.<br/> |
| [**Var**](var-str.md)                        | Depicts the organization of data in a file-version resource. It typically contains a list of language and code page identifier pairs that the version of the application or DLL supports.<br/>                             |
| [**VarFileInfo**](varfileinfo.md)            | Depicts the organization of data in a file-version resource. It contains version information not dependent on a particular language and code page combination.<br/>                                                        |
| [**VS\_FIXEDFILEINFO**](vs-fixedfileinfo.md) | Contains version information about a file. This information is language and code page independent. <br/>                                                                                                                   |
| [**VS\_VERSIONINFO**](vs-versioninfo.md)     | Depicts the organization of data in a file-version resource. It is the root structure that contains all other file-version information structures.<br/>                                                                    |



 

 

 





