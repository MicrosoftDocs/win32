---
title: SIS Links and Reparse Points
description: SIS is an NTFS filter driver that replaces duplicate files with copy-on-write links (referred to as SIS links) that point to a single backing file, reducing the disk and cache overhead of those files.
ms.assetid: 1600a9ff-413c-4059-b04c-c862f6cf8f32
keywords:
- reparse points Backup
- single-instance store (SIS) Backup , SIS links
- single-instance store (SIS) Backup , reparse points
ms.topic: article
ms.date: 05/31/2018
---

# SIS Links and Reparse Points

SIS is an NTFS filter driver that replaces duplicate files with copy-on-write links (referred to as SIS links) that point to a single backing file, reducing the disk and cache overhead of those files. This backing file is contained in a [common store](the-sis-common-store-and-common-store-files.md). The implementation of the SIS architecture makes use of [reparse points](/windows/desktop/FileIO/reparse-points) that contain information about the SIS links.

SIS links are implemented as sparse files, usually with most ranges of the file unallocated, and a reparse point. The structure and contents of a reparse point is opaque to your backup and restore applications; however, your applications send and retrieve the data within these reparse points to and from SIS API functions that process the information in them. The information in a reparse point refers to a single backing file that contains the actual file data. This backing file is called a [common-store file](the-sis-common-store-and-common-store-files.md), and it exists in the common store.

When restoring a SIS link, your restore application should perform the following steps:

1.  Determine the common-store file or files to which the SIS link points.
2.  If the file or files do not exist in the common store, restore the file or files along with the SIS link.
3.  If the SIS link points to a common-store file or files that exist on the disk, then restore only the SIS link. Recall that the data in common-store files never changes, so if a given common-store file is still on the disk at restore time, it has the same contents as when it was backed up and there is no need to overwrite it.

The only additional overhead required for SIS-assisted backups is that your backup application must back up the SIS link and the data associated with the backing files. All SIS backup and restore operations are local to a specific volume.

 

 