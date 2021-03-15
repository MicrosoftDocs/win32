---
description: A requester needs to have a well-defined understanding about the status of the writer that participates with it during shadow copy creation, and during backup and restore operations.
ms.assetid: 676d5cff-bd28-43f0-a402-d184c96f0061
title: Determining Writer Status
ms.topic: article
ms.date: 05/31/2018
---

# Determining Writer Status

A requester needs to have a well-defined understanding about the status of the writer that participates with it during shadow copy creation, and during backup and restore operations. To do so, it is recommended:

-   Requesters use [**IVssBackupComponents::GatherWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwriterstatus), [**IVssBackupComponents::GetWriterStatusCount**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwriterstatuscount), and [**IVssBackupComponents::GetWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwriterstatus).
-   As described in [Overview of Processing a Backup Under VSS](overview-of-processing-a-backup-under-vss.md) and [Overview of Processing a Restore Under VSS](overview-of-processing-a-restore-under-vss.md), these methods are most useful when called in a well-defined backup or restore sequence. Typically, this means that the writers should be queried after a requester has completed one of its tasks and generated a VSS event.

    When processing a backup, a requester should query a writer following the completion of the following methods. Requesters must call [**GatherWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwriterstatus) after calling [**BackupComplete**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-backupcomplete) to cause the writer session to be set to a completed state.

    > [!Note]  
    > This is only necessary on Windows Server 2008 with Service Pack 2 (SP2) and earlier.

     

    <dl> <dt>

[**IVssBackupComponents::PrepareForBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup)
</dt> <dt>

[**IVssBackupComponents::DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset)
</dt> <dt>

[**IVssBackupComponents::BackupComplete**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-backupcomplete)
</dt> </dl>

During restore operations, a requester should query a writer after completion of these methods:
<dl> <dt>

[**IVssBackupComponents::PreRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prerestore)
</dt> <dt>

[**IVssBackupComponents::PostRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-postrestore)
</dt> </dl>

-   Calls to [**IVssBackupComponents::GatherWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwriterstatus) that are not part of a well-defined backup or restore sequence do not provide a reliable picture of writer status, because they might reflect conditions that do not indicate failure in the current operation, such as:
    -   A failure of a previous shadow copy creation
    -   An error in an early backup or restore operation
    -   An unresponsive writer currently processing an event

Therefore, developers should not rely on writer status returned by processes other then the requester or attempt to monitor the progress of one instance of the [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface with another (possibly in a separate thread).

Note that for backup operations, where it is necessary to examine writers' Writer Metadata Documents, there is no need for a requester call to [**IVssBackupComponents::GatherWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwriterstatus) and [**IVssBackupComponents::GetWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwriterstatus) following the generation and handling of the [*Identify*](vssgloss-i.md) event caused by [**IVssBackupComponents::GatherWriterMetdata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata).

[**IVssBackupComponents::GetWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwriterstatus) reports only the status of those writers whose metadata was provided to VSS by writers' [*Identify*](vssgloss-i.md) event handlers, [**CVssWriter::OnIdentify**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onidentify) (and returned to the requester by [**IVssBackupComponents::GetWriterMetadataCount**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritermetadatacount) and [**IVssBackupComponents::GetWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritermetadata)).

If a writer's implementation of [**CVssWriter::OnIdentify**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onidentify) fails, that writer's metadata will not be part of the list of Writer Metadata Documents provided to VSS, no status information will be available, and the call would be redundant.

For restore operations, where the requester does not need to examine Writer Metadata Documents of executing writers, calling [**IVssBackupComponents::GatherWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwriterstatus) and [**IVssBackupComponents::GetWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwriterstatus) may be a more efficient way to determine which writers are executing.

 

 



