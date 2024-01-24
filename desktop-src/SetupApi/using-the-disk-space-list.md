---
description: Before you can add or remove file operations from the disk-space list, you must create it by using the SetupCreateDiskSpaceList function.
ms.assetid: 287fd84a-dc8c-4a5c-b998-db5f2fbee5f1
title: Using the Disk-Space List
ms.topic: article
ms.date: 05/31/2018
---

# Using the Disk-Space List

Before you can add or remove file operations from the disk-space list, you must create it by using the [**SetupCreateDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupcreatediskspacelista) function.

After you create a disk-space list you can add individual file copy or delete operations to the list by using [**SetupAddToDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupaddtodiskspacelista). To add all the file copy or delete operations in an entire INF section, use either the [**SetupAddSectionToDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupaddsectiontodiskspacelista) or [**SetupAddInstallSectionToDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupaddinstallsectiontodiskspacelista) function.

After you add all the installation operations to the disk-space list, you can query it to find out how much disk space is required for the specified installation by using the [**SetupQuerySpaceRequiredOnDrive**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueryspacerequiredondrivea) function.

The [**SetupQueryDrivesInDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupquerydrivesindiskspacelista) function returns the drive specifications for each target drive referenced in the file operations on the disk-space list. You can use this information to programmatically compare the available space on these drives with the space required by the installation.

To remove a file operation from the disk-space list, use the [**SetupRemoveFromDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupremovefromdiskspacelista) function. To remove all file copy or delete operations from an entire INF section, use the [**SetupRemoveSectionFromDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupremovesectionfromdiskspacelista) or [**SetupRemoveInstallSectionFromDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupremoveinstallsectionfromdiskspacelista) function.

After the disk-space list is no longer required, you can release the resources allocated to it by calling the [**SetupDestroyDiskSpaceList**](/windows/desktop/api/Setupapi/nf-setupapi-setupdestroydiskspacelist) function.

 

 



