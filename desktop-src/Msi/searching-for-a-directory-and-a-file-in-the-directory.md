---
description: During a Windows Installer installation, the installer can search for a directory and a file in that directory.
ms.assetid: ddf624f9-6f85-4ef6-8dfc-8635a25915d0
title: Searching for a Directory and a File in the Directory
ms.topic: article
ms.date: 05/31/2018
---

# Searching for a Directory and a File in the Directory

**To search for a directory and then a file in that directory**

1.  First search for the directory.

    AppDir must be defined as the valid signature of the directory. If AppDir is not defined as a valid signature, AppSearch does not have a place to find the file, for example, if the search is for c:\\MyDir\\MyApp.exe, AppDir should be defined as c:\\MyDir. AppDir might be defined by including a record in the [DrLocator Table](drlocator-table.md), or by some other method. No record is included in the [Signature Table](signature-table.md) for the directory search. For the file search, list the file signature and name in the Signature Table. The remaining fields in this record can be null to search for any version of MyApp.exe.

    [Signature Table](signature-table.md) (partial)

    

    | Signature          | File Name            |
    |--------------------|----------------------|
    | AppFile<br/> | MyApp.exe<br/> |

    

     

2.  Use the [AppSearch Table](appsearch-table.md).

    Enter the property that the Installer is to set if the directory with the signature AppDir is installed. If the Installer finds this directory is installed, it sets MYDIR to the directory path. Enter the property that the Installer is to set if MyApp.exe is installed.

    [AppSearch Table](appsearch-table.md) (partial)

    

    | Property         | Signature          |
    |------------------|--------------------|
    | MYDIR<br/> | AppDir<br/>  |
    | MYAPP<br/> | AppFile<br/> |

    

     

3.  Use the [DrLocator Table](drlocator-table.md).

    Enter in the Parent column the signature, AppDir, that is defined as the path of the directory. Specify in the Depth column the number of subdirectory levels to search in this directory. AppDir must be defined as the directory signature. AppDir may be defined by including a record as shown here or by another method.

    [DrLocator Table](drlocator-table.md)

    

    | Signature | Parent | Path      | Depth |
    |-----------|--------|-----------|-------|
    | AppDir    |        | C:\\MyDir | 0     |
    | AppFile   | AppDir |           | 0     |

    

     

4.  Include the AppSearch action in the action sequence.

    If MyApp.exe is found to be installed in AppDir, the Installer sets the property MYAPP to the location of file.

## Related topics

<dl> <dt>

[Searching for Existing Applications, Files, Registry Entries or .ini File Entries](searching-for-existing-applications-files-registry-entries-or--ini-file-entries.md)
</dt> </dl>

 

 




