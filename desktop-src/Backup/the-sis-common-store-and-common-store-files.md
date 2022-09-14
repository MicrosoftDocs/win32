---
title: The SIS Common Store and Common-Store Files
description: All backing files maintained by single-instance store (SIS) backup are called common-store files.
ms.assetid: c6231c30-9d5a-428d-a94d-9dc8db933432
keywords:
- common stores Backup
- single-instance store (SIS) Backup , common stores
ms.topic: article
ms.date: 05/31/2018
---

# The SIS Common Store and Common-Store Files

All backing files maintained by single-instance store (SIS) backup are called *common-store files*. One *common store* exists on each SIS-maintained volume and contains all of the common-store files that exist on that volume. This directory is located in the root directory of the volume and is named "\\SIS Common Store". The common store is implemented as a directory that is protected against normal user access, because common-store files are intended to be accessed directly only by SIS backup API functions and not backup and restore applications.

The properties of a common-store file are the following:

-   A common-store file may have one or more links pointing to it.
-   After it is created, the contents of a common-store file never change.
-   The names of common-store files are globally unique—that is, they are unique across all volumes across all systems in the world, and the binding between a common-store file name and its data is globally static.

When SIS is enabled on a volume, one copy of the duplicate files is then created to the common store, and all of the duplicate files are replaced with [SIS links](sis-links-and-reparse-points.md) pointing to the common-store file. For more information, see [Enabling or Disabling SIS on a Volume](/previous-versions/windows/it-pro/windows-server-storage-solutions/dd573313(v=ws.10)) in the TechNet documentation.

When one of the SIS links is accessed for a write operation, the SIS filter first restores the original contents of the SIS link file from the common-store file, the reparse point linking the SIS link file to the common store is removed, and then the write operation is performed on the original destination file.

The common-store file is removed only when the last SIS link pointing to it is deleted.

 

 