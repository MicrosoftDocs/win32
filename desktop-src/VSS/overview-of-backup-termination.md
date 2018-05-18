---
Description: 'The following table shows the sequence of actions and events that are required for a backup operation to be terminated. For more information, see Overview of Processing a Backup Under VSS.'
ms.assetid: '12dcb2d1-614b-4c4c-a47c-342f79b20a62'
title: Overview of Backup Termination
---

# Overview of Backup Termination

The following table shows the sequence of actions and events that are required for a backup operation to be terminated. For more information, see [Overview of Processing a Backup Under VSS](overview-of-processing-a-backup-under-vss.md).



| Requester action                                                                                                                                                                                                              | Event                                                                 | Writer action                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The requester terminates the shadow copy by releasing the [**IVssBackupComponents**](ivssbackupcomponents.md) interface or by calling [**IVssBackupComponents::DeleteSnapshots**](ivssbackupcomponents-deletesnapshots.md). | None                                                                  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**IVssBackupComponents**](ivssbackupcomponents.md) is released by calling [**IUnknown::Release**](_com_iunknown_release).                                                                                                   | [*BackupShutdown*](vssgloss-b.md#base-vssgloss-backupshutdown-event) | The writer handles the event with [**CVssWriter::OnBackupShutdown**](cvsswriter-onbackupshutdown.md), which allows it to clean up any state related to the shadow copy set. If the backup operation failed—that is, it did not generate a [**BackupComplete**](ivssbackupcomponents-backupcomplete.md) event—the writer may also have to perform error handling. See [Handling BackupShutdown Events](handling-backupshutdown-events.md) for more information. |



 

Because an [**IVssBackupComponents**](ivssbackupcomponents.md) interface cannot be reused, and the destructor of the interface terminates the shadow copies, there is typically no reason to call [**IVssBackupComponents::DeleteSnapshots**](ivssbackupcomponents-deletesnapshots.md). This method is designed to be used in conjunction with error handling and aborting backups (see [Aborting VSS Operations](aborting-vss-operations.md)).

 

 



