---
title: Backup and Restore of Data Deduplication-Enabled Volumes
description: The data deduplication feature enables backup applications to perform optimized backup and restore of volumes that are enabled for data deduplication.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3D5214B5-21ED-4D0E-93A0-10CA5C28B6BE
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Backup and Restore of Data Deduplication-Enabled Volumes

The data deduplication feature enables backup applications to perform optimized backup and restore of volumes that are enabled for data deduplication. There are also situations where it is preferable to perform nonoptimized backup and restore.

In addition to reading this documentation, you should also study the [DedupBackupRestore sample](https://Code.MSDN.Microsoft.Com/windowsdesktop/DedupBackupRestore-sample-37200b48), which is useful for understanding multiple restore scenarios.

-   [Optimized Backup](#optimized-backup)
-   [Incremental Optimized Backup](#incremental-optimized-backup)
-   [Full Volume Restore from Optimized Backup](#full-volume-restore-from-optimized-backup)
-   [Selective Restore from Optimized Backup](#selective-restore-from-optimized-backup)
    -   [Selective Partial Volume Restore to Newly Formatted Volume](#selective-partial-volume-restore-to-newly-formatted-volume)
    -   [Selective Restore from a Data Deduplication-Enabled Backup Store](#selective-restore-from-a-data-deduplication-enabled-backup-store)
-   [Recalling a File to Disk](#recalling-a-file-to-disk)
-   [Nonoptimized Backup and Restore](#nonoptimized-backup-and-restore)
-   [Incremental Nonoptimized Backup](#incremental-nonoptimized-backup)
-   [The Deduplication VSS Writer](#the-deduplication-vss-writer)

## Optimized Backup

In optimized backup, the backup application does the following:

-   Uses a shadow copy of the optimized volume.
-   Specifies the **FILE\_FLAG\_OPEN\_REPARSE\_POINT** flag when opening the data deduplication-optimized files.
-   Copies the optimized files (reparse points) and chunk store container files as-is from the shadow copy to the backup store.

In many cases, such as a full volume backup (either block-level or file-level), performing an optimized backup will result in a smaller, faster backup than an unoptimized backup. In these cases the backup will be smaller, because the total size of the optimized files (reparse points), non-optimized files (not in-policy) and data deduplication store container files is significantly smaller than the full logical size of the volume. Optimized backups are faster, because there is less I/O (smaller backup) and because the optimized files are not "rehydrated" during the file copy operations. Selective backup, in which most of the volume is being backed up, may also benefit from using the optimized backup approach, if the logical size of the selected files is greater than the physical size of the selected files plus the chunk store files.

## Incremental Optimized Backup

A backup application can perform an incremental optimized backup as follows:

-   Back up only the changed user files, including reparse points that were created, modified, or deleted since the previous backup.
-   Back up the changed chunk store container files. Remember that new chunks are appended to the current chunk store container. When its size reaches about 1 GB, that container file is sealed and a new container file is created. Therefore, the data deduplication optimization job usually results in incremental changes to the chunk store— most files are untouched, some are appended, and some new ones may be created.
-   Because the data deduplication optimization job appends chunks to the chunk store container, backup applications may benefit from an incremental backup at the sub-file level, one that backs up new and modified file ranges instead of entire files.

## Full Volume Restore from Optimized Backup

File-level full volume restore can and should be performed in an optimized manner by essentially reversing the procedure described in the Optimized Backup section. The complete set of data deduplication metadata and container files are restored, then the complete set of data deduplication reparse points are restored, followed by restore of all non-deduplicated files. Restoring volumes in this manner has the advantage of faster recovery time as compared to full-volume restore from a nonoptimized backup store because the amount of copied data is much smaller. Also, the size of the restored data in an optimized full volume restore is known to fit on a volume of the original size. On the other hand, restoring to the original or equivalently-sized volume from a nonoptimized backup will likely reach a disk-full condition because the files will be replaced at their full logical (non-deduplicated) size.

Block-level restore from an Optimized Backup is automatically an optimized restore because the restore occurs underneath data deduplication, which works at the file level.

It is recommended to always perform full volume restore to a freshly formatted volume of equivalent or greater size than the original volume. The target volume can be the original reformatted volume or a freshly created volume. The volume may contain files, but it might not contain a data deduplication chunk store. If the target volume already has a data deduplication chunk store, then you should follow the guidelines for selective restore below, or stage the restore by restoring to an alternate location that does not have a deduplication chunk store.

Note that full volume restore procedures do not need to use the [Data Deduplication Backup/Restore API](data-deduplication-backup-restore-api-reference.md).

## Selective Restore from Optimized Backup

Selective restore from an optimized backup can be done by using one of the following approaches.

-   Selective partial volume restore to a newly formatted volume
-   Selective restore from a data deduplication-enabled backup store
-   [Selective File Restore Using Data Deduplication Backup/Restore API](selective-file-restore-using-data-deduplication-backup-restore-api.md)

### Selective Partial Volume Restore to Newly Formatted Volume

This approach is very similar to the file-level full volume restore described above where only a subset of the data deduplication reparse points are restored back to a freshly formatted volume. Note that this approach requires that all chunk store files be copied to the new volume. This approach is appropriate if most of the volume is being restored. The application can make a calculated decision about whether this is an appropriate technique by comparing the size of the data deduplication store files plus physical size of all the restored files to the total logical size of the target restore file set.

### Selective Restore from a Data Deduplication-Enabled Backup Store

If the backup store is located on a volume enabled with data deduplication, both the backup store and the original volume are optimized. (Note that the backup server must be Windows Server 2012 or later, and the backup volume must be an NTFS volume.) In this case, the backup application can simply copy the files as normal files back to the target volume. The files will be rehydrated in memory from the backup store, so the application will be subjected to increased I/O latency while reading the backup store. If the file on the target volume is missing, or has been fully recalled from the data deduplication store, there will be no increased latency on the target volume. However, to be sure, it is good practice to first delete the file, if it exists, from the target volume before restoring the file with this approach.

## Recalling a File to Disk

To recall a file to disk programmatically, use one of the following methods:

-   Open the file by creating a memory mapped writable section.
-   Open the file inside a TxF transaction.

## Nonoptimized Backup and Restore

In nonoptimized backup and restore, the backup application does not use the [Data Deduplication Backup/Restore API](data-deduplication-backup-restore-api-reference.md).

The backup application opens the files and copies them without specifying the **FILE\_FLAG\_OPEN\_REPARSE\_POINT** flag.

The optimized files are copied to the backup volume as normal files, not as optimized files. The conversion from optimized file to normal file is performed transparently in memory by the data deduplication feature when the backup application copies the files.

> [!Note]  
> Chunk store files should be excluded from the backup.

 

Restore from such a backup store is a normal file copy operation.

The size of the data in a nonoptimized backup is recommended to be much larger than the original optimized volume, because of the space savings from data deduplication. A full volume restore from a nonoptimized backup will usually not fit on the original or equivalently sized volume.

Nonoptimized backup is normally used only for the following:

-   Selective backup of a small portion of the file on the volume, where the logical size of the selected files is smaller than the physical size of the optimized files plus the chunk store container files.
-   To support restoring a Windows Server 2012 or later backup to an earlier version of Windows.
-   To support restoring a Windows Server 2012 or later backup to a non-Windows computer.

## Incremental Nonoptimized Backup

A backup application can perform an incremental optimized backup as follows:

-   Back up any changed user files.
-   Consider skipping reparse point changes. (These are marked with the **USN\_SOURCE\_DATA\_MANAGEMENT** flag.)
-   In unoptimized backup, the data deduplication chunk store is excluded, therefore changes to chunk store files can be ignored.

## The Deduplication VSS Writer

The deduplication VSS writer reports two components for each volume that contains a deduplication chunk store:



| Component name        | Component file location                            |
|-----------------------|----------------------------------------------------|
| "Chunk Store"         | \\System Volume Information\\Dedup\\ChunkStore\\\* |
| "Dedup Configuration" | \\System Volume Information\\Dedup\\Settings\\\*   |



 

Both components are marked as selectable-for-backup and selectable-for-restore. These components must be treated as follows in the backup:

-   In an optimized volume backup, both components must be backed up.
-   In a non-optimized volume backup, the "Chunk Store" component must be excluded.

Because deduplication is crash-consistent, the deduplication writer does not participate in Freeze events.

The deduplication writer does not participate in restore.

The deduplication schedules for the computer or cluster are reported by the Task Scheduler Writer, not the deduplication writer.

This writer is an in-box writer for Windows Server operating system versions; it does not ship in Windows Client.

The writer name string for this writer is "Dedup Writer".

The writer ID for the deduplication writer is 41DB4DBF-6046-470E-8AD5-D5081DFB1B70.

This writer's usage type is **VSS\_UT\_SYSTEMSERVICE**, because deduplication's ddpvssvc service is a system service.

Its backup schema includes the **VSS\_BS\_INDEPENDENT\_SYSTEM\_STATE** flag, because it doesn't depend on system state.

Its backup schema also includes the **VSS\_BS\_WRITER\_SUPPORTS\_NEW\_TARGET** flag, because it supports restoring to a different volume.

All components have the **VSS\_CF\_NOT\_SYSTEM\_STATE** flag set, because they are not part of system state.

All temporary and instance-related files are excluded from backup.

 

 




