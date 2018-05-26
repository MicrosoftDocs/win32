---
Description: The following Setup API functions are used with INF Files.
ms.assetid: fb4263fc-5f59-460a-a7d9-93f10729c02a
title: INF File Setup Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INF File Setup Functions

The following Setup API functions are used with INF Files.



| Function                                                                         | Description                                                                                                                                                                                            |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SetupCloseInfFile**](/windows/win32/Setupapi/nf-setupapi-setupcloseinffile?branch=master)                                   | Frees resources and closes the INF handle.                                                                                                                                                             |
| [**SetupDecompressOrCopyFile**](/windows/win32/Setupapi/nf-setupapi-setupdecompressorcopyfilea?branch=master)                   | Copies a file and, if necessary, decompresses it.                                                                                                                                                      |
| [**SetupFindFirstLine**](/windows/win32/Setupapi/nf-setupapi-setupfindfirstlinea?branch=master)                                 | Finds the first line in a section of an INF file or, if a key is specified, the first line that matches that key. It updates the **Line** member of an [**INFCONTEXT**](/windows/win32/Setupapi/ns-setupapi-_infcontext?branch=master) structure. |
| [**SetupFindNextLine**](/windows/win32/Setupapi/nf-setupapi-setupfindnextline?branch=master)                                   | Returns the next line in a section relative to the **Line** member of the specified [**INFCONTEXT**](/windows/win32/Setupapi/ns-setupapi-_infcontext?branch=master) structure.                                                                    |
| [**SetupFindNextMatchLine**](/windows/win32/Setupapi/nf-setupapi-setupfindnextmatchlinea?branch=master)                         | Returns the next line in a section relative to the **Line** member of the specified [**INFCONTEXT**](/windows/win32/Setupapi/ns-setupapi-_infcontext?branch=master) that matches a specified key.                                                 |
| [**SetupGetBinaryField**](/windows/win32/Setupapi/nf-setupapi-setupgetbinaryfield?branch=master)                               | Retrieves data from a line whose fields are in binary format.                                                                                                                                          |
| [**SetupGetFieldCount**](/windows/win32/Setupapi/nf-setupapi-setupgetfieldcount?branch=master)                                 | Returns the number of fields in a line.                                                                                                                                                                |
| [**SetupGetFileCompressionInfo**](/windows/win32/Setupapi/nf-setupapi-setupgetfilecompressioninfoa?branch=master)               | Retrieves file compression information from an INF file.                                                                                                                                               |
| [**SetupGetInfFileList**](/windows/win32/Setupapi/nf-setupapi-setupgetinffilelista?branch=master)                               | Gets a list of the types of INF files in a specified directory.                                                                                                                                        |
| [**SetupGetInfInformation**](/windows/win32/Setupapi/nf-setupapi-setupgetinfinformationa?branch=master)                         | Returns information about an INF file (by **Line** member of an [**INFCONTEXT**](/windows/win32/Setupapi/ns-setupapi-_infcontext?branch=master) or filename).                                                                                     |
| [**SetupGetIntField**](/windows/win32/Setupapi/nf-setupapi-setupgetintfield?branch=master)                                     | Returns the specified integer field of a line in an INF file.                                                                                                                                          |
| [**SetupGetLineByIndex**](/windows/win32/Setupapi/nf-setupapi-setupgetlinebyindexa?branch=master)                               | Updates the **Line** member of an [**INFCONTEXT**](/windows/win32/Setupapi/ns-setupapi-_infcontext?branch=master) for the line at a specified index in the specified section.                                                                     |
| [**SetupGetLineCount**](/windows/win32/Setupapi/nf-setupapi-setupgetlinecounta?branch=master)                                   | Returns the number of lines in the specified section.                                                                                                                                                  |
| [**SetupGetLineText**](/windows/win32/Setupapi/nf-setupapi-setupgetlinetexta?branch=master)                                     | Retrieves the content of a specified line from an INF file.                                                                                                                                            |
| [**SetupGetMultiSzField**](/windows/win32/Setupapi/nf-setupapi-setupgetmultiszfielda?branch=master)                             | Returns a list of strings, starting at the specified field of a line in an INF file.                                                                                                                   |
| [**SetupGetSourceFileLocation**](/windows/win32/Setupapi/nf-setupapi-setupgetsourcefilelocationa?branch=master)                 | Gets the source disk ordinal and path (relative to source root) where the source file is located                                                                                                       |
| [**SetupGetSourceFileSize**](/windows/win32/Setupapi/nf-setupapi-setupgetsourcefilesizea?branch=master)                         | Gets the file size for an individual source file or a **Copy Files** section of an INF file.                                                                                                           |
| [**SetupGetSourceInfo**](/windows/win32/Setupapi/nf-setupapi-setupgetsourceinfoa?branch=master)                                 | Retrieves the path, tag file, or description for a source.                                                                                                                                             |
| [**SetupGetStringField**](/windows/win32/Setupapi/nf-setupapi-setupgetstringfielda?branch=master)                               | Returns the specified string field of a line in an INF file.                                                                                                                                           |
| [**SetupGetTargetPath**](/windows/win32/Setupapi/nf-setupapi-setupgettargetpatha?branch=master)                                 | Gets the target path for a **Copy Files** section in an INF file.                                                                                                                                      |
| [**SetupInstallFile**](/windows/win32/Setupapi/nf-setupapi-setupinstallfilea?branch=master)                                     | Installs a file.                                                                                                                                                                                       |
| [**SetupInstallFileEx**](/windows/win32/Setupapi/nf-setupapi-setupinstallfileexa?branch=master)                                 | Installs a file and returns a variable indicating whether or not the file was in use.                                                                                                                  |
| [**SetupInstallFilesFromInfSection**](/windows/win32/Setupapi/nf-setupapi-setupinstallfilesfrominfsectiona?branch=master)       | Queues all the files specified in the **Copy Files**, **Delete Files**, and **Rename Files** sections that are listed by an **Install** section.                                                       |
| [**SetupInstallFromInfSection**](/windows/win32/Setupapi/nf-setupapi-setupinstallfrominfsectiona?branch=master)                 | Performs the directives specified in an INF file **Install** section.                                                                                                                                  |
| [**SetupInstallServicesFromInfSection**](/windows/win32/Setupapi/nf-setupapi-setupinstallservicesfrominfsectiona?branch=master) | Performs service installation and deletion operations as specified in a **Service** section of an INF file.                                                                                            |
| [**SetupOpenAppendInfFile**](/windows/win32/Setupapi/nf-setupapi-setupopenappendinffilea?branch=master)                         | Opens an INF file and append it to an existing INF handle.                                                                                                                                             |
| [**SetupOpenInfFile**](/windows/win32/Setupapi/nf-setupapi-setupopeninffilea?branch=master)                                     | Opens an INF file and returns a handle to it.                                                                                                                                                          |
| [**SetupOpenMasterInf**](/windows/win32/Setupapi/nf-setupapi-setupopenmasterinf?branch=master)                                 | Opens the INF file that contains file and layout information for files shipped with the system.                                                                                                        |
| [**SetupQueryInfFileInformation**](/windows/win32/Setupapi/nf-setupapi-setupqueryinffileinformationa?branch=master)             | Queries an INF information structure about its associated INF filenames.                                                                                                                               |
| [**SetupQueryInfVersionInformation**](/windows/win32/Setupapi/nf-setupapi-setupqueryinfversioninformationa?branch=master)       | Queries an INF information structure for version information on one of its constituent INF files.                                                                                                      |
| [**SetupSetDirectoryId**](/windows/win32/Setupapi/nf-setupapi-setupsetdirectoryida?branch=master)                               | Associates a new directory identifier with a particular directory.                                                                                                                                     |



 

 

 



