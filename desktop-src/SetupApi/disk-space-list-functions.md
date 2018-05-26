---
Description: The following functions are used with the disk-space list.
ms.assetid: 18693b2d-6b0f-4f9c-b3cf-e50c36e2f2e1
title: Disk-Space List Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Disk-Space List Functions

The following functions are used with the disk-space list.



| Function                                                                                         | Description                                                                                                                          |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**SetupAdjustDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupadjustdiskspacelista?branch=master)                                     | Adjusts the amount of required space for a specified drive.                                                                          |
| [**SetupCreateDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupcreatediskspacelista?branch=master)                                     | Creates a disk-space list and allocates resources to it.                                                                             |
| [**SetupDestroyDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupdestroydiskspacelist?branch=master)                                   | Destroys a disk-space list, freeing the resources allocated to it.                                                                   |
| [**SetupDuplicateDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupduplicatediskspacelista?branch=master)                               | Duplicates a disk-space list as a new independent disk-space list.                                                                   |
| [**SetupQueryDrivesInDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupquerydrivesindiskspacelista?branch=master)                       | Fills a buffer with the drive specifications for all the drives listed in the disk-space list.                                       |
| [**SetupQuerySpaceRequiredOnDrive**](/windows/win32/Setupapi/nf-setupapi-setupqueryspacerequiredondrivea?branch=master)                         | Returns the total amount of disk space required to complete the file operations on a particular drive listed in the disk-space list. |
| [**SetupAddToDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupaddtodiskspacelista?branch=master)                                       | Adds a file copy or delete operation to the disk-space list.                                                                         |
| [**SetupAddSectionToDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupaddsectiontodiskspacelista?branch=master)                         | Adds all the file operations in a **Copy Files** or **Delete Files** section of an INF file to a disk-space list.                    |
| [**SetupAddInstallSectionToDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupaddinstallsectiontodiskspacelista?branch=master)           | Adds all the file operations in an **Install** section of an INF file to the disk-space list.                                        |
| [**SetupRemoveFromDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupremovefromdiskspacelista?branch=master)                             | Removes a file copy or delete operation from a disk-space list.                                                                      |
| [**SetupRemoveSectionFromDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupremovesectionfromdiskspacelista?branch=master)               | Removes all the file operations in a **Copy Files** or **Delete Files** section of an INF file from a disk-space list.               |
| [**SetupRemoveInstallSectionFromDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupremoveinstallsectionfromdiskspacelista?branch=master) | Removes all the file operations in the **Install** section of an INF file from the disk-space list.                                  |



 

 

 



