---
description: The following table shows the sequence of actions and events that are required for a backup operation to be terminated. For more information, see Overview of Processing a Backup Under VSS.
ms.assetid: 12dcb2d1-614b-4c4c-a47c-342f79b20a62
title: Overview of Backup Termination
ms.topic: article
ms.date: 05/31/2018
---

# Overview of Backup Termination

The following table shows the sequence of actions and events that are required for a backup operation to be terminated. For more information, see [Overview of Processing a Backup Under VSS](overview-of-processing-a-backup-under-vss.md).



| Requester action                                                                                                                                                                                                              | Event                                                                 | Writer action                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The requester terminates the shadow copy by releasing the [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface or by calling [**IVssBackupComponents::DeleteSnapshots**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-deletesnapshots). | None                                                                  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) is released by calling [**IUnknown::Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release).                                                                                                   | [*BackupShutdown*](vssgloss-b.md) | The writer handles the event with [**CVssWriter::OnBackupShutdown**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onbackupshutdown), which allows it to clean up any state related to the shadow copy set. If the backup operation failed—that is, it did not generate a [**BackupComplete**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-backupcomplete) event—the writer may also have to perform error handling. See [Handling BackupShutdown Events](handling-backupshutdown-events.md) for more information. |



 

Because an [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface cannot be reused, and the destructor of the interface terminates the shadow copies, there is typically no reason to call [**IVssBackupComponents::DeleteSnapshots**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-deletesnapshots). This method is designed to be used in conjunction with error handling and aborting backups (see [Aborting VSS Operations](aborting-vss-operations.md)).

 

 
