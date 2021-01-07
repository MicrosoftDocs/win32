---
description: During a Windows Installer installation, the installer can search all fixed drives for a file.
ms.assetid: c8aa84a8-5525-4a12-898f-63dc30113b13
title: Searching All Fixed Drives for a File
ms.topic: article
ms.date: 05/31/2018
---

# Searching All Fixed Drives for a File

**To search all fixed drives for a file**

1.  Enter the file signature and name in the [Signature Table](signature-table.md). The remaining fields in this record can be null to search for any version of MyApp.exe.

    [Signature Table](signature-table.md) (partial)

    

    | Signature          | File Name            |
    |--------------------|----------------------|
    | AppFile<br/> | MyApp.exe<br/> |

    

     

2.  Enter the property that the Installer is to set if MyApp.exe is installed.

    [AppSearch Table](appsearch-table.md)

    

    | Property         | Signature          |
    |------------------|--------------------|
    | MYAPP<br/> | AppFile<br/> |

    

     

3.  Use the [DrLocator Table](drlocator-table.md). Leave the Parent and Path fields empty to search all fixed drives of the user system. Specify in the Depth column the number of subdirectory levels to search. For example, setting Depth to 0 detects c:\\MyApp.exe, but does not detect the file at a depth of 2, for example: c:\\Program Files\\MyApps\\MyApp.exe.

    [DrLocator Table](drlocator-table.md)

    

    | Signature          | Parent | Path | Depth        |
    |--------------------|--------|------|--------------|
    | AppFile<br/> |        |      | 3<br/> |

    

     

4.  Include the AppSearch action in the action sequence. If MyApp.exe is installed, the Installer sets the property MYAPP to the location of the file. If the file is installed, MYAPP evaluates as True in a conditional expression.

 

 




