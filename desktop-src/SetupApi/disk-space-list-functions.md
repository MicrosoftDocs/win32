---
description: The following functions are used with the disk-space list.
ms.assetid: 18693b2d-6b0f-4f9c-b3cf-e50c36e2f2e1
title: Disk-Space List Functions
ms.topic: article
ms.date: 05/31/2018
---

# Disk-Space List Functions

The following functions are used with the disk-space list.



| Function                                                                                         | Description                                                                                                                          |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**SetupAdjustDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupadjustdiskspacelista)                                     | Adjusts the amount of required space for a specified drive.                                                                          |
| [**SetupCreateDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupcreatediskspacelista)                                     | Creates a disk-space list and allocates resources to it.                                                                             |
| [**SetupDestroyDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupdestroydiskspacelist)                                   | Destroys a disk-space list, freeing the resources allocated to it.                                                                   |
| [**SetupDuplicateDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupduplicatediskspacelista)                               | Duplicates a disk-space list as a new independent disk-space list.                                                                   |
| [**SetupQueryDrivesInDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupquerydrivesindiskspacelista)                       | Fills a buffer with the drive specifications for all the drives listed in the disk-space list.                                       |
| [**SetupQuerySpaceRequiredOnDrive**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueryspacerequiredondrivea)                         | Returns the total amount of disk space required to complete the file operations on a particular drive listed in the disk-space list. |
| [**SetupAddToDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupaddtodiskspacelista)                                       | Adds a file copy or delete operation to the disk-space list.                                                                         |
| [**SetupAddSectionToDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupaddsectiontodiskspacelista)                         | Adds all the file operations in a **Copy Files** or **Delete Files** section of an INF file to a disk-space list.                    |
| [**SetupAddInstallSectionToDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupaddinstallsectiontodiskspacelista)           | Adds all the file operations in an **Install** section of an INF file to the disk-space list.                                        |
| [**SetupRemoveFromDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupremovefromdiskspacelista)                             | Removes a file copy or delete operation from a disk-space list.                                                                      |
| [**SetupRemoveSectionFromDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupremovesectionfromdiskspacelista)               | Removes all the file operations in a **Copy Files** or **Delete Files** section of an INF file from a disk-space list.               |
| [**SetupRemoveInstallSectionFromDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupremoveinstallsectionfromdiskspacelista) | Removes all the file operations in the **Install** section of an INF file from the disk-space list.                                  |



 

 

 



