---
title: Selective File Restore Using Data Deduplication Backup/Restore API
description: Applications can use the interfaces described in the Data Deduplication Backup/Restore API Reference to perform selective restore of file data from an optimized backup.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4338C92B-A66E-4E21-8FA8-995EAC605958
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Selective File Restore Using Data Deduplication Backup/Restore API

Applications can use the interfaces described in the [Data Deduplication Backup/Restore API Reference](data-deduplication-backup-restore-api-reference.md) to perform selective restore of file data from an optimized backup.

Applications that need to perform single or multi-file restore from an optimized backup may use the [Data Deduplication Backup/Restore API](data-deduplication-backup-restore-api-reference.md). If one of the approaches described in [Backup and Restore of Data Deduplication-Enabled Volumes](backup-and-restore-of-data-deduplication-enabled-volumes.md) cannot be used—for example, if the target volume already contains a data deduplication chunk store, this approach may be the only alternative.

Because the Data Deduplication on-disk schema is not publicly documented, Data Deduplication drives the restore process by relying on the application to perform required read I/O requests on its behalf. In response to each read request serviced by the application against Data Deduplication files in the backup store, Data Deduplication will interpret its own metadata and data, which may result in further read requests in some cases.

The backup application provides read access to Data Deduplication files in the backup store by using a COM callback mechanism. The overall process of restoring a file from an optimized backup store proceeds as follows.

1.  The backup application must ensure that the following prerequisites are in place:

    -   The Data Deduplication feature must be installed on the computer that holds the target volume.
    -   The target volume must be formatted with NTFS, but does not need to be data deduplication-enabled.

2.  The backup application copies the reparse points for the target files from the backup store.

    > [!Note]  
    > Because the restore process described here has multiple steps, the application may choose to restore the target files to a temporary location in order to prevent end-user access attempts while the files are being restored.

     

3.  The backup application initiates a file restore operation using [**IDedupBackupSupport::RestoreFiles**](https://msdn.microsoft.com/library/hh449224). The application specifies the full path to the reparse point files specified in the previous step. The application also provides Data Deduplication with an instance of [**IDedupReadFileCallback**](/windows/previous-versions/DdpBackup/nn-ddpbackup-idedupreadfilecallback?branch=master) that is ready to accept incoming calls from the Data Deduplication restore engine.
4.  The backup application receives one or more of the following calls from Data Deduplication on each of the following methods of the callback interface. The callbacks are serviced by the same application process that called [**IDedupBackupSupport::RestoreFiles**](https://msdn.microsoft.com/library/hh449224).

    -   [**IDedupReadFileCallback::ReadBackupFile**](/windows/previous-versions/DdpBackup/nf-ddpbackup-idedupreadfilecallback-readbackupfile?branch=master) – this method issues read requests targeting a Data Deduplication metadata or container file located in the application's backup store. The application ultimately issues the actual I/O to satisfy the read request by whatever means necessary. The application does not need to understand the file format or parse it in any way. The application only needs to be able to read the specified ranges of the files from the backup media.
    -   [**IDedupReadFileCallback::OrderContainersRestore**](/windows/previous-versions/DdpBackup/nf-ddpbackup-idedupreadfilecallback-ordercontainersrestore?branch=master) – this method provides the application with the ability to influence the order of the pending reads to multiple container files that are required to retrieve the target file data. Implementation of this method by the application is optional. Providing an implementation may be important in order to achieve acceptable restore performance from sequential access backup media such as tape or to otherwise improve restore performance. If the application does not provide an ordered set of container extents, Data Deduplication will generate one extent per container file (full file extents) in an arbitrary order.
    -   [**IDedupReadFileCallback::PreviewContainerRead**](/windows/previous-versions/DdpBackup/nf-ddpbackup-idedupreadfilecallback-previewcontainerread?branch=master) – this method provides the application with a preview of the sequence of reads that are pending for a given container file extent reported by [**OrderContainersRestore**](/windows/previous-versions/DdpBackup/nf-ddpbackup-idedupreadfilecallback-ordercontainersrestore?branch=master) (or generated by Data Deduplication, if the application does not implement **OrderContainersRestore**). The application may use this per-container extent read plan to increase the efficiency of the pending reads through read-ahead, caching or other mechanisms. Implementation of this method by the application is optional.

5.  Using the callback methods described above, Data Deduplication reads metadata and target file data in an iterative manner, according to a read plan optionally influenced by the application, and writes the file data back to the target file data stream. In this manner, Data Deduplication reconstructs the target file piece by piece until the entire file is restored at the target location in its original, non-deduplicated form.
6.  Data Deduplication removes the reparse point and metadata that were copied by the application in step 1.

    > [!Note]  
    > If the files were restored to a temporary location, the application should rename the files to their target destination.

     

 

 




