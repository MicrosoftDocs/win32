---
description: Processing one of a component's file sets may require a requester to traverse a directory tree recursively, which can require the requester to handle mounted folders and reparse points (such as links) that point to data that is not on the current volume.
ms.assetid: d0e08598-a8a2-489b-9cb2-e989bed1ce53
title: Working with Mounted Folders and Reparse Points
ms.topic: article
ms.date: 05/31/2018
---

# Working with Mounted Folders and Reparse Points

Processing one of a component's file sets may require a requester to traverse a directory tree recursively, which can require the requester to handle mounted folders and reparse points (such as links) that point to data that is not on the current volume.

Requesters are expected to follow mounted folders and reparse points when traversing a directory tree, and VSS has well-defined guidelines for handling them for backup and restore operations.

To illustrate these guidelines, consider the following example:

-   The volume \\\\?\\Volume{GUID\_1} has the drive letter C:\\.
-   A file set has a path of C:\\WriterData.
-   A file specification \*.dat is used by the file set.
-   The file set's recursion is set to **TRUE**.
-   The directory C:\\WriterData is located on the volume \\\\?\\Volume{GUID\_1}.
-   The directory C:\\WriterData\\Archive is a mounted folder.
-   The volume \\\\?\\Volume{GUID\_2} is associated with the mounted folder C:\\WriterData\\Archive.

## Handling Mounted Folders and Reparse Points during Backup

The basic rules for handling mounted folders and reparse points under VSS when performing a recursive backup can be summarized as follows:

-   Paths are followed across mounted folders and reparse points.
-   If a mounted folder or reparse point points to a volume, that volume should be shadow copied.
-   If a volume contains mounted folders or reparse points, these will appear in the shadow copy of the volume.
-   Data that is under the mounted folder or reparse point is captured in the shadow copy of the volume that the mounted folder or reparse point points to.

To illustrate using the example above, because the recursive flag is set, the requester must examine all data under C:\\WriterData\\Archive and below.

The requester must add both the volume with drive letter C:\\ (\\\\?\\Volume{GUID\_1}) and the volume associated with the mounted folder C:\\WriterData\\Archive (\\\\?\\Volume{GUID\_2}) to the shadow copy set using [**IVssBackupComponents::AddToSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addtosnapshotset).

The mounted folder C:\\WriterData\\Archive appears in the shadow copy of volume \\\\?\\Volume{GUID\_1}, which has a device object named deviceObject1.

However, VSS will not copy any data under that mounted folder (data on \\\\?\\Volume{GUID\_2}) to the shadow copy referenced by deviceObject1. Instead, that data is captured in the shadow copy of \\\\?\\Volume{GUID\_2}, which has a device object named deviceObject2.

Therefore, a requester that is backing up shadow copied files under C:\\WriterData will use a path of deviceObject1\\WriterData to search for files matching C:\\WriterData\\\*.dat.

To back up shadow copied files under C:\\WriterData\\Archive, the requester will use a path of deviceObject2 (because the root directory of \\\\?\\Volume{GUID\_2} was associated with the mounted folder C:\\Writer\\Archive) to search for files matching C:\\WriterData\\Archive\\\*.dat.

Note that a reparse point is handled in the same way as a mounted folder. The reparse point appears in the shadow copy of the first volume. The data under the reparse point appears in the shadow copy of the second volume.

During backup, requesters should store information about mounted folders and the volumes associated with them as well as reparse points and their targets to ensure that all data is backed up and restored correctly.

## Handling Mount and Reparse Points during Restore

When restoring files, the requester must follow guidelines somewhat different from those that were used during backup (ignoring issues such as [*alternate location mapping*](vssgloss-a.md) and [*new target location*](vssgloss-n.md)):

-   As before, if recursion is required, paths are followed across mounted folders and reparse points.
-   Mounted folders are to be restored.
-   The restoration locations of mounted folders and reparse points are those determined by their original paths.

If the volume names persist between backup and restore—that is, you do not re-create the volumes—restored mounted folders and reparse points should point to the correct volumes.

Therefore, in the example discussed above, if the mounted folder C:\\WriterData\\Archive was restored to (\\\\?\\Volume{GUID\_1}) and the volume previously associated with it was restored to (\\\\?\\Volume{GUID\_2}), the restored files and file structure would be correct and consistent.

It may happen that data is restored to a system where volume names changed. This could be due to disk crashes, where you might need to perform a manual system recovery and re-create volumes. In this type of situation, mounted folders and reparse points will no longer be valid after restore. To re-create the files and file structure on the restored volume will require deleting the restored mounted folders and reparse points and re-creating them on disk. It is up to the backup application to decide whether this is appropriate.

Note that it is possible that the restore destination for a mounted folder is already occupied. For example, C:\\WriterData\\Archive might already contain some files. It is up to the backup application to decide how to handle this situation.

 

 



