---
description: The following Setup API functions are used with INF Files.
ms.assetid: fb4263fc-5f59-460a-a7d9-93f10729c02a
title: INF File Setup Functions
ms.topic: article
ms.date: 05/31/2018
---

# INF File Setup Functions

The following Setup API functions are used with INF Files.



| Function                                                                         | Description                                                                                                                                                                                            |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SetupCloseInfFile**](/windows/desktop/api/Setupapi/nf-setupapi-setupcloseinffile)                                   | Frees resources and closes the INF handle.                                                                                                                                                             |
| [**SetupDecompressOrCopyFile**](/windows/desktop/api/Setupapi/nf-setupapi-setupdecompressorcopyfilea)                   | Copies a file and, if necessary, decompresses it.                                                                                                                                                      |
| [**SetupFindFirstLine**](/windows/desktop/api/Setupapi/nf-setupapi-setupfindfirstlinea)                                 | Finds the first line in a section of an INF file or, if a key is specified, the first line that matches that key. It updates the **Line** member of an [**INFCONTEXT**](/windows/desktop/api/Setupapi/ns-setupapi-infcontext) structure. |
| [**SetupFindNextLine**](/windows/desktop/api/Setupapi/nf-setupapi-setupfindnextline)                                   | Returns the next line in a section relative to the **Line** member of the specified [**INFCONTEXT**](/windows/desktop/api/Setupapi/ns-setupapi-infcontext) structure.                                                                    |
| [**SetupFindNextMatchLine**](/windows/desktop/api/Setupapi/nf-setupapi-setupfindnextmatchlinea)                         | Returns the next line in a section relative to the **Line** member of the specified [**INFCONTEXT**](/windows/desktop/api/Setupapi/ns-setupapi-infcontext) that matches a specified key.                                                 |
| [**SetupGetBinaryField**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetbinaryfield)                               | Retrieves data from a line whose fields are in binary format.                                                                                                                                          |
| [**SetupGetFieldCount**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetfieldcount)                                 | Returns the number of fields in a line.                                                                                                                                                                |
| [**SetupGetFileCompressionInfo**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetfilecompressioninfoa)               | Retrieves file compression information from an INF file.                                                                                                                                               |
| [**SetupGetInfFileList**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetinffilelista)                               | Gets a list of the types of INF files in a specified directory.                                                                                                                                        |
| [**SetupGetInfInformation**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetinfinformationa)                         | Returns information about an INF file (by **Line** member of an [**INFCONTEXT**](/windows/desktop/api/Setupapi/ns-setupapi-infcontext) or filename).                                                                                     |
| [**SetupGetIntField**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetintfield)                                     | Returns the specified integer field of a line in an INF file.                                                                                                                                          |
| [**SetupGetLineByIndex**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetlinebyindexa)                               | Updates the **Line** member of an [**INFCONTEXT**](/windows/desktop/api/Setupapi/ns-setupapi-infcontext) for the line at a specified index in the specified section.                                                                     |
| [**SetupGetLineCount**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetlinecounta)                                   | Returns the number of lines in the specified section.                                                                                                                                                  |
| [**SetupGetLineText**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetlinetexta)                                     | Retrieves the content of a specified line from an INF file.                                                                                                                                            |
| [**SetupGetMultiSzField**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetmultiszfielda)                             | Returns a list of strings, starting at the specified field of a line in an INF file.                                                                                                                   |
| [**SetupGetSourceFileLocation**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetsourcefilelocationa)                 | Gets the source disk ordinal and path (relative to source root) where the source file is located                                                                                                       |
| [**SetupGetSourceFileSize**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetsourcefilesizea)                         | Gets the file size for an individual source file or a **Copy Files** section of an INF file.                                                                                                           |
| [**SetupGetSourceInfo**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetsourceinfoa)                                 | Retrieves the path, tag file, or description for a source.                                                                                                                                             |
| [**SetupGetStringField**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetstringfielda)                               | Returns the specified string field of a line in an INF file.                                                                                                                                           |
| [**SetupGetTargetPath**](/windows/desktop/api/Setupapi/nf-setupapi-setupgettargetpatha)                                 | Gets the target path for a **Copy Files** section in an INF file.                                                                                                                                      |
| [**SetupInstallFile**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfilea)                                     | Installs a file.                                                                                                                                                                                       |
| [**SetupInstallFileEx**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfileexa)                                 | Installs a file and returns a variable indicating whether or not the file was in use.                                                                                                                  |
| [**SetupInstallFilesFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfilesfrominfsectiona)       | Queues all the files specified in the **Copy Files**, **Delete Files**, and **Rename Files** sections that are listed by an **Install** section.                                                       |
| [**SetupInstallFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfrominfsectiona)                 | Performs the directives specified in an INF file **Install** section.                                                                                                                                  |
| [**SetupInstallServicesFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallservicesfrominfsectiona) | Performs service installation and deletion operations as specified in a **Service** section of an INF file.                                                                                            |
| [**SetupOpenAppendInfFile**](/windows/desktop/api/Setupapi/nf-setupapi-setupopenappendinffilea)                         | Opens an INF file and append it to an existing INF handle.                                                                                                                                             |
| [**SetupOpenInfFile**](/windows/desktop/api/Setupapi/nf-setupapi-setupopeninffilea)                                     | Opens an INF file and returns a handle to it.                                                                                                                                                          |
| [**SetupOpenMasterInf**](/windows/desktop/api/Setupapi/nf-setupapi-setupopenmasterinf)                                 | Opens the INF file that contains file and layout information for files shipped with the system.                                                                                                        |
| [**SetupQueryInfFileInformation**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueryinffileinformationa)             | Queries an INF information structure about its associated INF filenames.                                                                                                                               |
| [**SetupQueryInfVersionInformation**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueryinfversioninformationa)       | Queries an INF information structure for version information on one of its constituent INF files.                                                                                                      |
| [**SetupSetDirectoryId**](/windows/desktop/api/Setupapi/nf-setupapi-setupsetdirectoryida)                               | Associates a new directory identifier with a particular directory.                                                                                                                                     |



 

 

 



