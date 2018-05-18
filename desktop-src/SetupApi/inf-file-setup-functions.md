---
Description: 'The following Setup API functions are used with INF Files.'
ms.assetid: 'fb4263fc-5f59-460a-a7d9-93f10729c02a'
title: INF File Setup Functions
---

# INF File Setup Functions

The following Setup API functions are used with INF Files.



| Function                                                                         | Description                                                                                                                                                                                            |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SetupCloseInfFile**](setupcloseinffile.md)                                   | Frees resources and closes the INF handle.                                                                                                                                                             |
| [**SetupDecompressOrCopyFile**](setupdecompressorcopyfile.md)                   | Copies a file and, if necessary, decompresses it.                                                                                                                                                      |
| [**SetupFindFirstLine**](setupfindfirstline.md)                                 | Finds the first line in a section of an INF file or, if a key is specified, the first line that matches that key. It updates the **Line** member of an [**INFCONTEXT**](infcontext-str.md) structure. |
| [**SetupFindNextLine**](setupfindnextline.md)                                   | Returns the next line in a section relative to the **Line** member of the specified [**INFCONTEXT**](infcontext-str.md) structure.                                                                    |
| [**SetupFindNextMatchLine**](setupfindnextmatchline.md)                         | Returns the next line in a section relative to the **Line** member of the specified [**INFCONTEXT**](infcontext-str.md) that matches a specified key.                                                 |
| [**SetupGetBinaryField**](setupgetbinaryfield.md)                               | Retrieves data from a line whose fields are in binary format.                                                                                                                                          |
| [**SetupGetFieldCount**](setupgetfieldcount.md)                                 | Returns the number of fields in a line.                                                                                                                                                                |
| [**SetupGetFileCompressionInfo**](setupgetfilecompressioninfo.md)               | Retrieves file compression information from an INF file.                                                                                                                                               |
| [**SetupGetInfFileList**](setupgetinffilelist.md)                               | Gets a list of the types of INF files in a specified directory.                                                                                                                                        |
| [**SetupGetInfInformation**](setupgetinfinformation.md)                         | Returns information about an INF file (by **Line** member of an [**INFCONTEXT**](infcontext-str.md) or filename).                                                                                     |
| [**SetupGetIntField**](setupgetintfield.md)                                     | Returns the specified integer field of a line in an INF file.                                                                                                                                          |
| [**SetupGetLineByIndex**](setupgetlinebyindex.md)                               | Updates the **Line** member of an [**INFCONTEXT**](infcontext-str.md) for the line at a specified index in the specified section.                                                                     |
| [**SetupGetLineCount**](setupgetlinecount.md)                                   | Returns the number of lines in the specified section.                                                                                                                                                  |
| [**SetupGetLineText**](setupgetlinetext.md)                                     | Retrieves the content of a specified line from an INF file.                                                                                                                                            |
| [**SetupGetMultiSzField**](setupgetmultiszfield.md)                             | Returns a list of strings, starting at the specified field of a line in an INF file.                                                                                                                   |
| [**SetupGetSourceFileLocation**](setupgetsourcefilelocation.md)                 | Gets the source disk ordinal and path (relative to source root) where the source file is located                                                                                                       |
| [**SetupGetSourceFileSize**](setupgetsourcefilesize.md)                         | Gets the file size for an individual source file or a **Copy Files** section of an INF file.                                                                                                           |
| [**SetupGetSourceInfo**](setupgetsourceinfo.md)                                 | Retrieves the path, tag file, or description for a source.                                                                                                                                             |
| [**SetupGetStringField**](setupgetstringfield.md)                               | Returns the specified string field of a line in an INF file.                                                                                                                                           |
| [**SetupGetTargetPath**](setupgettargetpath.md)                                 | Gets the target path for a **Copy Files** section in an INF file.                                                                                                                                      |
| [**SetupInstallFile**](setupinstallfile.md)                                     | Installs a file.                                                                                                                                                                                       |
| [**SetupInstallFileEx**](setupinstallfileex.md)                                 | Installs a file and returns a variable indicating whether or not the file was in use.                                                                                                                  |
| [**SetupInstallFilesFromInfSection**](setupinstallfilesfrominfsection.md)       | Queues all the files specified in the **Copy Files**, **Delete Files**, and **Rename Files** sections that are listed by an **Install** section.                                                       |
| [**SetupInstallFromInfSection**](setupinstallfrominfsection.md)                 | Performs the directives specified in an INF file **Install** section.                                                                                                                                  |
| [**SetupInstallServicesFromInfSection**](setupinstallservicesfrominfsection.md) | Performs service installation and deletion operations as specified in a **Service** section of an INF file.                                                                                            |
| [**SetupOpenAppendInfFile**](setupopenappendinffile.md)                         | Opens an INF file and append it to an existing INF handle.                                                                                                                                             |
| [**SetupOpenInfFile**](setupopeninffile.md)                                     | Opens an INF file and returns a handle to it.                                                                                                                                                          |
| [**SetupOpenMasterInf**](setupopenmasterinf.md)                                 | Opens the INF file that contains file and layout information for files shipped with the system.                                                                                                        |
| [**SetupQueryInfFileInformation**](setupqueryinffileinformation.md)             | Queries an INF information structure about its associated INF filenames.                                                                                                                               |
| [**SetupQueryInfVersionInformation**](setupqueryinfversioninformation.md)       | Queries an INF information structure for version information on one of its constituent INF files.                                                                                                      |
| [**SetupSetDirectoryId**](setupsetdirectoryid.md)                               | Associates a new directory identifier with a particular directory.                                                                                                                                     |



 

 

 



