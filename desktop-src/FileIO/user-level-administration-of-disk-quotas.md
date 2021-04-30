---
description: How to get more free disk space after exceeding the quota allowance.
ms.assetid: a73b6a11-36f1-4437-a83d-e89918b1b0ae
title: User-level Administration of Disk Quotas
ms.topic: article
ms.date: 05/31/2018
---

# User-level Administration of Disk Quotas

Disk quotas are transparent to the user. When a user asks how much space is free on a disk, the system reports only the available quota allowance the user has available. If the user exceeds this allowance, the system returns the **ERROR\_DISK\_FULL** error, just as it would to indicate that the disk was full.

To obtain more free disk space after exceeding the quota allowance, the user must do one of the following:

-   Delete some files.
-   Have another user claim ownership of some files.
-   Have the administrator increase the quota allowance.

Programs that need to retrieve the actual amount of free disk space can call the [**GetDiskFreeSpaceEx**](/windows/desktop/api/FileAPI/nf-fileapi-getdiskfreespaceexa) function and look at the *TotalNumberOfFreeBytes* parameter.

 

 



