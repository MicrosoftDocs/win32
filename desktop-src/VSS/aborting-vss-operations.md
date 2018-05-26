---
Description: Abort events can be generated during a backup operation in any of the following cases
ms.assetid: c2e39cdd-0ff8-4030-9bec-9e003b4d9520
title: Aborting VSS Operations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Aborting VSS Operations

[*Abort*](vssgloss-a.md#base-vssgloss-abort-event) events can be generated during a backup operation in any of the following cases:

-   A requester explicitly generates an [*Abort event*](vssgloss-a.md#base-vssgloss-abort-event) by calling [**IVssBackupComponents::AbortBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-abortbackup?branch=master).
-   A writer's [*Freeze*](vssgloss-f.md#base-vssgloss-freeze) and [*Thaw*](vssgloss-t.md#base-vssgloss-thaw-event) event handlers ([**CVssWriter::OnFreeze**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onfreeze?branch=master) and [**CVssWriter::OnThaw**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onthaw?branch=master)) return **false**, or cannot complete in the time window specified in [**CVssWriter::Initialize**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-initialize?branch=master).
-   There is any failure of the provider or VSS during the creation of a shadow copy following the [*PrepareForSnapshot*](vssgloss-p.md#base-vssgloss-preparesnapshot-event) event.

Aborts are not supported for restore operations.

## Requester Handling and Creation of Abort Events

An instance of the [**IVSSBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) interface can be used for only one backup, so if an error occurs in processing a backup it is generally best to release the current instance and start over.

A requester should explicitly signal that it is aborting a backup operation (using [**IVssBackupComponents::AbortBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-abortbackup?branch=master)) only after the actual preparation for a backup, involving writers, or the creation of a shadow copy has taken place.

Effectively, this means that any time a requester needs to stop a backup operation after generating a [*PrepareForBackup*](vssgloss-p.md#base-vssgloss-preparebackup-event) event by calling [**IVssBackupComponents::PrepareForBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup?branch=master), it should call [**IVssBackupComponents::AbortBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-abortbackup?branch=master) and await its return prior to releasing the current [**IVSSBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) instance.

For example, if a writer vetoed a backup operation, a requester should use [**IVssBackupComponents::AbortBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-abortbackup?branch=master) to notify all other writers that the backup operation will not be completed.

Prior to calling [**PrepareForBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup?branch=master), or if the call to **PrepareForBackup** fails, a requester can release the current instance of the [**IVSSBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) interface without needing to generate an Abort event.

For example, if the current instance of [**IVSSBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) is being used merely to obtain information by calling [**IVssBackupComponents::GatherWriterMetadata**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata?branch=master) and generating an [*Identify*](vssgloss-i.md#base-vssgloss-identify-event) event, once information has been returned the instance of **IVSSBackupComponents** can simply be released.

A requester generates a number of events ([*PrepareForSnapshot*](vssgloss-p.md#base-vssgloss-preparesnapshot-event), [*Freeze*](vssgloss-f.md#base-vssgloss-freeze), [*Thaw*](vssgloss-t.md#base-vssgloss-thaw-event), and [*PostSnapshot*](vssgloss-p.md#base-vssgloss-postsnapshot-event)) when it calls [**IVssBackupComponents::DoSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset?branch=master). While handling the Freeze and Thaw events, a writer may fail and can generate an Abort event on its own. Failure to handle PrepareForSnapshot and PostSnapshot events does not generate an Abort event.

It is not always possible for a requester to know if an Abort event was generated when [**IVssBackupComponents::DoSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset?branch=master) indicates failure. Therefore, a requester that needs to terminate a backup operation because the status of **IVssBackupComponents::DoSnapshotSet** indicates a problem should still call [**IVssBackupComponents::AbortBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-abortbackup?branch=master).

If a requester has called [**IVssBackupComponents::AbortBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-abortbackup?branch=master), it is not necessary to call [**IVssBackupComponents::BackupComplete**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-backupcomplete?branch=master) prior to releasing an instance of [**IVSSBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master).

## Writer Handling and Creation of Abort Events

As noted previously, a writer can receive an Abort event from a requester, or the provider can trigger one itself. Also, it is possible for a writer to receive multiple Abort events under certain circumstances. Writer developers should code any implementation of [**CVssWriter::OnAbort**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onabort?branch=master) with this in mind.

In handling an Abort event, a writer should attempt to restore whatever process it managed to its normal running state, as well as perform any error handling and logging.

This may mean that an implementation of [**CVssWriter::OnAbort**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onabort?branch=master) might have to perform many, if not all, of the same tasks as the Thaw event handler ([**CVssWriter::OnThaw**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onthaw?branch=master)) and the PostSnapshot event handler ([**CVssWriter::OnPostSnapshot**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onpostsnapshot?branch=master)), and these handlers can be called from within **CVssWriter::OnAbort**.

 

 



