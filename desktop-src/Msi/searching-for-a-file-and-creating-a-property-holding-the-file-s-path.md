---
description: During a Windows Installer installation, the installer can search for a file and create a property containing the file's path.
ms.assetid: 6587b349-852d-4d4e-a8d4-76dfb0ef0f0b
title: Searching for a File and Creating a Property Holding the File's Path
ms.topic: article
ms.date: 05/31/2018
---

# Searching for a File and Creating a Property Holding the File's Path

**To search for a file and create a property holding the path of that file**

1.  First do a search for the file by listing the file signature and name in the [Signature Table](signature-table.md).

    The remaining fields of this record can be left empty to specify a search for any version of MyApp.exe.

    [Signature Table](signature-table.md) (partial)

    

    | Signature          | File name            |
    |--------------------|----------------------|
    | AppFile<br/> | MyApp.exe<br/> |

    

     

2.  Next, specify the path of the file that is being searched for in the [DrLocator Table](drlocator-table.md).

    Because AppFolder is not listed in the [Signature Table](signature-table.md), the Installer determines that AppFolder is a folder rather than a file.

    [DrLocator Table](drlocator-table.md)

    

    | Signature            | Parent             | Path | Depth |
    |----------------------|--------------------|------|-------|
    | AppFile<br/>   |                    |      |       |
    | AppFolder<br/> | AppFile<br/> |      |       |

    

     

3.  Finally, populate the [AppSearch Table](appsearch-table.md) so that the [AppSearch Action](appsearch-action.md) returns the path of AppFolder.

    After the Installer executes the AppSearch action, the value of MYFOLDER is the full path of AppFolder.

    [AppSearch Table](appsearch-table.md) (partial)

    

    | Property            | Signature            |
    |---------------------|----------------------|
    | MYFOLDER<br/> | AppFolder<br/> |

    

     

 

 




