---
Description: Before you can add or remove file operations from the disk-space list, you must create it by using the SetupCreateDiskSpaceList function.
ms.assetid: 287fd84a-dc8c-4a5c-b998-db5f2fbee5f1
title: Using the Disk-Space List
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the Disk-Space List

Before you can add or remove file operations from the disk-space list, you must create it by using the [**SetupCreateDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupcreatediskspacelista?branch=master) function.

After you create a disk-space list you can add individual file copy or delete operations to the list by using [**SetupAddToDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupaddtodiskspacelista?branch=master). To add all the file copy or delete operations in an entire INF section, use either the [**SetupAddSectionToDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupaddsectiontodiskspacelista?branch=master) or [**SetupAddInstallSectionToDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupaddinstallsectiontodiskspacelista?branch=master) function.

After you add all the installation operations to the disk-space list, you can query it to find out how much disk space is required for the specified installation by using the [**SetupQuerySpaceRequiredOnDrive**](/windows/win32/Setupapi/nf-setupapi-setupqueryspacerequiredondrivea?branch=master) function.

The [**SetupQueryDrivesInDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupquerydrivesindiskspacelista?branch=master) function returns the drive specifications for each target drive referenced in the file operations on the disk-space list. You can use this information to programmatically compare the available space on these drives with the space required by the installation.

To remove a file operation from the disk-space list, use the [**SetupRemoveFromDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupremovefromdiskspacelista?branch=master) function. To remove all file copy or delete operations from an entire INF section, use the [**SetupRemoveSectionFromDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupremovesectionfromdiskspacelista?branch=master) or [**SetupRemoveInstallSectionFromDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupremoveinstallsectionfromdiskspacelista?branch=master) function.

After the disk-space list is no longer required, you can release the resources allocated to it by calling the [**SetupDestroyDiskSpaceList**](/windows/win32/Setupapi/nf-setupapi-setupdestroydiskspacelist?branch=master) function.

 

 



