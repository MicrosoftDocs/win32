---
Description: 'It is possible for a backup application (requester) to terminate and not generate a BackupComplete event.'
ms.assetid: '8e6a1f4f-ba62-46ea-965e-b0c6526ece89'
title: Handling BackupShutdown Events
---

# Handling BackupShutdown Events

It is possible for a backup application (requester) to terminate and not generate a [*BackupComplete*](vssgloss-b.md#base-vssgloss-backupcomplete-event) event. The backup application could crash, or be terminated (from the Task Manager, for example) and not be able to call [**IVssBackupComponents::BackupComplete**](ivssbackupcomponents-backupcomplete.md).

Therefore, the VSS infrastructure (rather than the requester) generates a [*BackupShutdown*](vssgloss-b.md#base-vssgloss-backupshutdown-event) event whenever an instance of [**IVssBackupComponents**](ivssbackupcomponents.md) participating in a backup is released, whether it is released by the requester or by the system.

If a backup proceeds properly, a writer will receive a BackupComplete event followed by a BackupShutdown event.

If the operation aborts (the requester generates an [*Abort event*](vssgloss-a.md#base-vssgloss-abort-event) by calling [**IVssBackupComponents::AbortBackup**](ivssbackupcomponents-abortbackup.md)) or fails abruptly, a writer may receive only a BackupShutdown event, and it may not receive other events that perform cleanup operations. It is up to a writer to determine whether a BackupShutdown event follows a proper sequence of events, or represents an unexpected failure of the backup operations.

The BackupShutdown event handler, [**CVssWriter::OnBackupShutdown**](cvsswriter-onbackupshutdown.md), receives the VSS\_ID (GUID) of the shadow copy set of the backup operation being shut down. The writer can use this to determine which backup operation is being shut down, if it has stored the shadow copy set ID during its backup sequence (for example, from within [**CVssWriter::OnFreeze**](cvsswriter-onfreeze.md), [**CVssWriter::OnThaw**](cvsswriter-onthaw.md), or [**CVssWriter::OnPostSnapshot**](cvsswriter-onpostsnapshot.md)) by using [**CVssWriter::GetCurrentSnapshotSetId**](cvsswriter-getcurrentsnapshotsetid.md).

However, a writer should not call [**CVssWriter::GetCurrentSnapshotSetId**](cvsswriter-getcurrentsnapshotsetid.md) from within [**CVssWriter::OnBackupShutdown**](cvsswriter-onbackupshutdown.md). Also, **CVssWriter::GetCurrentSnapshotSetId** cannot be called after [**CVssWriter::OnPostSnapshot**](cvsswriter-onpostsnapshot.md) returns.

It is possible for the writer to be involved in multiple backup operations, and if a BackupShutdown event is called because of an abrupt shutdown of a requester, the VSS\_ID returned could be that of another backup operation the writer was participating in.

 

 



