---
description: Requesters have primary responsibility for the life cycle of a Backup Components Document.
ms.assetid: 287b7b9a-ac04-4a74-83c1-2cdd4a571ac1
title: Backup Components Document Life Cycle
ms.topic: article
ms.date: 05/31/2018
---

# Backup Components Document Life Cycle

Requesters have primary responsibility for the life cycle of a Backup Components Document.

This control is exercised by an instance of the [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface object returned by [**CreateVssBackupComponents**](/windows/desktop/api/VsBackup/nf-vsbackup-createvssbackupcomponents).

A requester must initialize a Backup Components Document prior to a backup or restore by calling [**IVssBackupComponents::InitializeForBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-initializeforbackup) or [**IVssBackupComponents::InitializeForRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-initializeforrestore). The requester can initialize the document as empty, or it can load a previously stored copy of the document.

For backup operations, a Backup Components Document is typically initialized as empty. Its data will be filled in with cooperation from the system's writers in the course of processing the backup.

For restore operations, a Backup Components Document is typically initialized from a stored document generated during the initial backup. This allows the restore (in conjunction with examination of stored Writer Metadata Documents) to determine what data was initially backed up and how it should be restored.

Backing up [*transportable shadow copies*](vssgloss-t.md) is an exception to this rule. In this case, a shadow copy could have been moved from one system (where it was created along with the initial Backup Components Document) to another by means of reassigning a shared storage device's logical unit. To back up under these circumstances, a requester loads the stored backup state and proceeds from where the initial system left off. (For more information, see [Importing Transportable Shadow Copied Volumes](importing-transportable-shadow-copied-volumes.md).)

In the course of processing a backup, the requester decides which components to actually copy on the basis of which components are marked as [*selectable for backup*](vssgloss-s.md), the component's [*logical paths*](vssgloss-l.md), and its own internal logic.

Some of the components will be [*explicitly included*](vssgloss-e.md) in the backup operation; information about the component will be added to the Backup Components Document. Others will be [*implicitly included*](vssgloss-i.md) in the backup; information about the added components will not be added to the Backup Components Document.

All of a writer's nonselectable for backup components without a selectable ancestor in their logical path, and those selectable for backup components the requester chooses, will be added explicitly.

Both nonselectable and selectable for backup components can be added implicitly if they have a selectable ancestor in their logical path, which is explicitly included in the backup. These components ([*subcomponents*](vssgloss-s.md)) are members of [*component sets*](vssgloss-s.md) defined by their selectable ancestor.

When handling restore operations, the requester uses [*selectability for restore*](vssgloss-s.md) instead of selectability for backup in conjunction with logical path information and its own internal logic to decide which files to restore.

If a component that had been implicitly added to the backup is now to be explicitly added to the restore, the requester will update the Backup Components Document with that component's information.

Information about the stored components is available both to requesters and writers through instances of the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface.

It is through [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interfaces that writers can query and (until the end of [**PostSnapshot**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onpostsnapshot) and [**PostRestore**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onpostrestore) events) modify information in the Backup Components Document.

When the [**CVssWriter::OnPrepareBackup**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onpreparebackup), [**CVssWriter::OnPreRestore**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onprerestore), [**CVssWriter::OnPostSnapshot**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onpostsnapshot), [**CVssWriter::OnBackupComplete**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onbackupcomplete), or [**CVssWriter::OnPostRestore**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onpostrestore) event handler is called, a writer receives an instance of an [**IVssWriterComponents**](/windows/desktop/api/VsWriter/nl-vswriter-ivsswritercomponents) interface.

Note that upon generation of the [**BackupComplete**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-backupcomplete) event, the Backup Components Document is made read-only, and therefore [**CVssWriter::OnBackupComplete**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onbackupcomplete) cannot use the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface to modify it.

From the [**IVSSWriterComponents**](/windows/desktop/api/VsWriter/nl-vswriter-ivsswritercomponents) interface, the writer can retrieve instances of the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface that will allow it to access all of its components explicitly added to the Backup Components Document and to alter their state. For more information, see [Overview of Processing a Backup Under VSS](overview-of-processing-a-backup-under-vss.md) and [Overview of Processing a Restore Under VSS](overview-of-processing-a-restore-under-vss.md).

Backup Components Documents are removed from memory when the [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface is released, and must be stored using [**IVssBackupComponents::SaveAsXML**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-saveasxml), or all their information will be lost.

In addition, when an [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) document is properly released, a [**BackupShutdown**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onbackupshutdown) event is generated and[*auto-release shadow copies*](vssgloss-a.md) are deleted.

 

 



