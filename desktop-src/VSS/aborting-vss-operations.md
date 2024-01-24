---
description: 'Abort events can be generated during a backup operation in any of the following cases:'
ms.assetid: c2e39cdd-0ff8-4030-9bec-9e003b4d9520
title: Aborting VSS Operations
ms.topic: article
ms.date: 05/31/2018
---

# Aborting VSS Operations

[*Abort*](vssgloss-a.md) events can be generated during a backup operation in any of the following cases:

-   A requester explicitly generates an [*Abort event*](vssgloss-a.md) by calling [**IVssBackupComponents::AbortBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-abortbackup).
-   A writer's [*Freeze*](vssgloss-f.md) and [*Thaw*](vssgloss-t.md) event handlers ([**CVssWriter::OnFreeze**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onfreeze) and [**CVssWriter::OnThaw**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onthaw)) return **false**, or cannot complete in the time window specified in [**CVssWriter::Initialize**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-initialize).
-   There is any failure of the provider or VSS during the creation of a shadow copy following the [*PrepareForSnapshot*](vssgloss-p.md) event.

Aborts are not supported for restore operations.

## Requester Handling and Creation of Abort Events

An instance of the [**IVSSBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface can be used for only one backup, so if an error occurs in processing a backup it is generally best to release the current instance and start over.

A requester should explicitly signal that it is aborting a backup operation (using [**IVssBackupComponents::AbortBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-abortbackup)) only after the actual preparation for a backup, involving writers, or the creation of a shadow copy has taken place.

Effectively, this means that any time a requester needs to stop a backup operation after generating a [*PrepareForBackup*](vssgloss-p.md) event by calling [**IVssBackupComponents::PrepareForBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup), it should call [**IVssBackupComponents::AbortBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-abortbackup) and await its return prior to releasing the current [**IVSSBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) instance.

For example, if a writer vetoed a backup operation, a requester should use [**IVssBackupComponents::AbortBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-abortbackup) to notify all other writers that the backup operation will not be completed.

Prior to calling [**PrepareForBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup), or if the call to **PrepareForBackup** fails, a requester can release the current instance of the [**IVSSBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface without needing to generate an Abort event.

For example, if the current instance of [**IVSSBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) is being used merely to obtain information by calling [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata) and generating an [*Identify*](vssgloss-i.md) event, once information has been returned the instance of **IVSSBackupComponents** can simply be released.

A requester generates a number of events ([*PrepareForSnapshot*](vssgloss-p.md), [*Freeze*](vssgloss-f.md), [*Thaw*](vssgloss-t.md), and [*PostSnapshot*](vssgloss-p.md)) when it calls [**IVssBackupComponents::DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset). While handling the Freeze and Thaw events, a writer may fail and can generate an Abort event on its own. Failure to handle PrepareForSnapshot and PostSnapshot events does not generate an Abort event.

It is not always possible for a requester to know if an Abort event was generated when [**IVssBackupComponents::DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset) indicates failure. Therefore, a requester that needs to terminate a backup operation because the status of **IVssBackupComponents::DoSnapshotSet** indicates a problem should still call [**IVssBackupComponents::AbortBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-abortbackup).

If a requester has called [**IVssBackupComponents::AbortBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-abortbackup), it is not necessary to call [**IVssBackupComponents::BackupComplete**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-backupcomplete) prior to releasing an instance of [**IVSSBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents).

## Writer Handling and Creation of Abort Events

As noted previously, a writer can receive an Abort event from a requester, or the provider can trigger one itself. Also, it is possible for a writer to receive multiple Abort events under certain circumstances. Writer developers should code any implementation of [**CVssWriter::OnAbort**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onabort) with this in mind.

In handling an Abort event, a writer should attempt to restore whatever process it managed to its normal running state, as well as perform any error handling and logging.

This may mean that an implementation of [**CVssWriter::OnAbort**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onabort) might have to perform many, if not all, of the same tasks as the Thaw event handler ([**CVssWriter::OnThaw**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onthaw)) and the PostSnapshot event handler ([**CVssWriter::OnPostSnapshot**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onpostsnapshot)), and these handlers can be called from within **CVssWriter::OnAbort**.

 

 



