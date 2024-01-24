---
description: During a Windows Installer installation, the installer can search for a file in a specific location on the user's system.
ms.assetid: 127d83a2-b651-42ef-ac7c-a7fa1b15cf27
title: Searching for a File in a Specific Location
ms.topic: article
ms.date: 05/31/2018
---

# Searching for a File in a Specific Location

**To search for a file in a specific location on a user system**

1.  List the file signature and name in the [Signature Table](signature-table.md). The remaining fields in this record can be null to search for any version of MyApp.exe.

    [Signature Table](signature-table.md)

    

    | Signature          | File name            |
    |--------------------|----------------------|
    | AppFile<br/> | MyApp.exe<br/> |

    

     

2.  Enter the property that the Installer is to set if MyApp.exe is installed.

    [AppSearch Table](appsearch-table.md) (partial)

    

    | Property         | Signature          |
    |------------------|--------------------|
    | MYAPP<br/> | AppFile<br/> |

    

     

3.  Use the [DrLocator Table](drlocator-table.md). Enter the full path to the file on the user system in the Path field. Enter a value of 0 into the Depth column to search the bin folder.

    [DrLocator Table](drlocator-table.md)

    

    | Signature          | Parent | Path                                                    | Depth        |
    |--------------------|--------|---------------------------------------------------------|--------------|
    | AppFile<br/> |        | C:\\Program Files\\MyProducts\\Projects\\bin<br/> | 0<br/> |

    

     

4.  Include the AppSearch action in the action sequence. If MyApp.exe is installed in C:\\Program Files\\MyProducts\\Projects\\bin, the Installer sets the property MYAPP to the location of file.

 

 




