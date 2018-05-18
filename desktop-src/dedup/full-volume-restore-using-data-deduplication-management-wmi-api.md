---
title: Lossless Full Volume Restore Using Data Deduplication Management WMI API
description: Lossless Full Volume Restore Using Data Deduplication Management WMI API
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'B9BD759C-C6CE-48D5-B3B7-65AEB17D9ED0'
ms.prod: 'windows-server-dev'
ms.technology:
- 'data-deduplication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# Lossless Full Volume Restore Using Data Deduplication Management WMI API

Some backup applications implement a version of full volume restore with the additional safeguards of retaining as much new and modified content since the backup time as possible. This is a file-level restore where new files are retained and modified files are either retained or restored based administrator input. The main idea is to restore the entire volume back to a previous backup time with minimal or controlled loss of the changes that have occurred since the backup, in essence a 'merge' of the current volume with its backup version.

This section describes a prescriptive approach to implement such a "lossless" full volume optimized restore even for a data deduplication-enabled volume. In full volume restore scenarios on a data deduplication-enabled volume, it is important that the entire set of data deduplication files (the reparse points) be kept in sync with the state of the chunk store which is restored in its entirety. If there are new or modified data deduplicated files present on the volume that are not present in the backup set that is selected for full volume restore, then these files need to be unoptimized (recalled) before the full volume restore. In other words, every file that was optimized or re-optimized after the backup time (the specific backup time being used for the restore), must be recalled to disk prior to restoring files.

The main idea of the lossless full volume restore procedure is to run a data deduplication unoptimization job with a timestamp parameter. The timestamp is the backup timestamp, provided to data deduplication by the backup application. The timestamp is used by the data deduplication unoptimization job to decide which data deduplication files to fully recall. Once the new and modified data deduplication files are recalled to be normal files, the backup application can proceed to fully restore the data deduplication chunk store and reparse points while leaving these new and modified files in place. Later, the files that were recalled by the unoptimization job will fall back into data deduplication policy and be optimized once again.

In many cases, the backup set selected for restore is for a fairly recent time such that there will be relatively few new and modified data deduplication files present on the volume. In these cases, the lossless full volume restore procedure is a good fit. When there are many new and modified data deduplication files, there may not be adequate space to recall all of the files back to their normal, unoptimized size. For those cases, the unoptimization may need to be done iteratively; alternatively unoptimizing the target files and moving them to an alternative staging volume before proceeding with the full volume restore. The main thing is to ensure that there are no data deduplication files present on the volume that are not present and restored from the selected backup set.

Applications can use the interfaces described in the [Data Deduplication Management WMI API Reference](data-deduplication-management-wmi-api-reference.md) to perform an optimized lossless restore by following the procedure outlined below.

1.  Disable deduplication jobs on the target volume by calling the [**MSFT\_DedupVolume::Disable**](msft-dedupvolume-disable.md) method, setting the *DataAccess* parameter to **FALSE**. This prevents new optimization, garbage collection, and scrubbing jobs from running on the volume while the restore is in progress. Jobs for other volumes, whether running or to-be-scheduled, are not affected.
2.  Stop any deduplication jobs that are running on the target volume by calling the [**MSFT\_DedupJob::Stop**](msft-dedupjob-stop.md) method.
3.  Unoptimize any new files that were added to the volume since the last backup by calling the [**MSFT\_DedupJob::Start**](msft-dedupjob-start.md) method as follows:

    1.  Set the *Type* parameter to **Unoptimization**.
    2.  Set the *TimeStamp* parameter to the time when the last backup was performed.

4.  Disable data access to deduplicated files on the volume by calling the [**MSFT\_DedupVolume::Disable**](msft-dedupvolume-disable.md) method, setting the *DataAccess* parameter to **TRUE**.

    > [!Note]  
    > The volume will be dismounted and remounted.

     

5.  Restore the deduplication chunk store files on the volume as follows:

    1.  Delete the entire directory tree that contains the deduplication chunk store files.
    2.  Restore the deduplication chunk store files from backup.

6.  Restore the target volume's files, directories, and deduplication reparse points from backup. In cases where a file, directory, or reparse point exists in the backup and on the target volume, your application will need to decide which copy of the item to keep.

    > [!Note]  
    > Do not include the deduplication chunk store files, because you restored these in the previous step.

     

7.  Reenable data access to deduplicated files on the volume by calling the [**MSFT\_DedupVolume::Enable**](msft-dedupvolume-enable.md) method, setting the *DataAccess* parameter to **TRUE**.

    > [!Note]  
    > The volume will be dismounted and remounted.

     

8.  Reenable deduplication jobs on the target volume by calling the [**MSFT\_DedupVolume::Enable**](msft-dedupvolume-enable.md) method, setting the *DataAccess* parameter to **FALSE**.
9.  Run garbage collection on the volume by calling the [**MSFT\_DedupJob::Start**](msft-dedupjob-start.md) method, setting the *Type* parameter to **GarbageCollection**.

## Full Volume Restore in a Clustered Environment

If a volume on a clustered disk fails over in the middle of a lossless restore, it is possible that the Data Deduplication filter driver on the original node will retain the disabled data access setting if it is set at the time of failover ([Disable-DedupVolume](http://go.microsoft.com/fwlink/p/?linkid=252531)-DataAccess). If, at a later time, the volume fails back to the original node, users will not be able to access Data Deduplication files until one of the following occurs.

-   The data access setting is re-enabled on the original node ([Enable-DedupVolume](http://go.microsoft.com/fwlink/p/?linkid=252532)-DataAccess).
-   The original node is restarted.

Verify the Deduplication File Server Role has been enabled on all nodes on the cluster before enabling deduplication on a Cluster Share Volume (CSV).

When migrating or restoring data from a backup volume image to a Cluster Share Volume (CSV) with deduplication enabled, first enable Maintenance Mode on the destination disk in the cluster. Restore the backup image to the destination and then disable Maintenance Mode to return the disk to the cluster.

## Related topics

<dl> <dt>

[DedupBackupRestore sample](https://Code.MSDN.Microsoft.Com/windowsdesktop/DedupBackupRestore-sample-37200b48)
</dt> </dl>

 

 




