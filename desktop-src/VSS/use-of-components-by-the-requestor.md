---
description: In addition to performing a backup or restore, and supervising shadow copies, a requester must manage information about the components of the writers it interacts with.
ms.assetid: 641abfbe-fc72-4468-9ef6-69c452adb1b3
title: Use of Components by the Requester
ms.topic: article
ms.date: 05/31/2018
---

# Use of Components by the Requester

In addition to performing a backup or restore, and supervising shadow copies, a requester must manage information about the components of the writers it interacts with. Component selectability and logical path are used to include or exclude data from a backup, and to decide what component information is included in the Backup Components Document.

## Requester Component Selection during Backup

During backup operations, a requester imports writer metadata component data using the [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata) and [**IVssBackupComponents::GetWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritermetadata) methods (see [Overview of Backup Initialization](overview-of-backup-initialization.md) for more information).

After examining writer information with the [**IVssExamineWriterMetadata**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssexaminewritermetadata) interface, a requester decides which writers it will back up and, to a limited extent, which of a given writer's components it will back up.

When backing up a writer, a requester:

-   Must [*explicitly include*](vssgloss-e.md) all of a writer's nonselectable for backup components without selectable for backup ancestors using [**IVssBackupComponents::AddComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent) to add the component to the Backup Components Document
-   May explicitly include any of a writer's selectable for backup components using [**IVssBackupComponents::AddComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent) to add the component to the Backup Components Document
-   If a selectable for backup component defines a [*component set*](vssgloss-c.md), its explicit inclusion [*implicitly includes*](vssgloss-i.md) all the component set's members—whether selectable for backup or not. These components are not added to the Backup Components Document.

In adding a selectable for backup component or a nonselectable for backup components without selectable for backup ancestors to its Backup Components Document, a requester specifies the following:

-   The instance of the writer managing the component
-   The writer's class identifier
-   The [*logical path*](vssgloss-l.md) of the component (which may be **NULL**)
-   The component's name

If a component does not match the specification, an error will be returned.

If such a component exists, VSS creates an [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface for the component in the Backup Components Document. This information will be accessible and modifiable by the writer and requester. For a selectable component that defines a [*component set*](vssgloss-c.md), it describes not only properties of the component but also all the subcomponents it contains.

Information about implicitly added components is not available in the Backup Components Document. In addition, no file information is available in the Backup Components Document. To obtain that information, the requester will have to examine the Writer Metadata Documents (which will have already been read) in the context of the selected stored components in the Backup Components Document.

## Requester Component Selection during Restore

During restore operations, a requester should not import component information from the writers currently active on the system via [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata), because the state of currently executing processes will not necessarily reflect the state of processes when a backup was made.

It should still generate an [*Identify event*](vssgloss-i.md) via [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata), both to create an *Identify event* and to determine which writers are currently on the system and their status.

The requester retrieves the stored Backup Components Document during its initialization as well as stored Writer Metadata Documents (see [Overview of Restore Initialization](overview-of-restore-initialization.md) for more information) .

Inclusion of components during backup is largely the same as that for restore, except that you must consider [*selectable for restore*](vssgloss-s.md) along with [*logical path*](vssgloss-l.md)—not [*selectable for backup*](vssgloss-s.md).

There are, however, some differences:

-   If a component has already been [*explicitly included*](vssgloss-e.md) to the Backup Components Document during backup, if it is included for restore (either explicitly or implicitly), [**IVssBackupComponents::SetSelectedForRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setselectedforrestore) is used to explicitly add it to the Backup Components Document for restore.
-   If a component was [*implicitly included*](vssgloss-i.md) to the backup, and is nonselectable for restore with no selectable for restore ancestors—which in the backup case would imply the need for explicit inclusion—the component is not explicitly included (that is, it is not added to the Backup Components Document using [**IVssBackupComponents::SetSelectedForRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setselectedforrestore)). Such a component should be considered implicitly selected for restore.
-   Of those components implicitly selected for backup (whether that component was selectable for backup or not), only those that are selectable for restore can be added to the Backup Components Document using [**IVssBackupComponents::AddRestoreSubcomponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addrestoresubcomponent).
-   Selectable for restore components may define a [*component set*](vssgloss-c.md) for restore—just as selectable for backup components do. This selectable for restore component then defines this component set for the restore operation.

A writer with no components explicitly selected for restore prior to the generation of a [*PreRestore*](vssgloss-p.md) event will not receive any VSS events.

Requesters and writers can access stored component information using the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface. Through the **IVssComponent** interface, writers can modify some of the settings of those of its components explicitly included in the Backup Components Document to support a restore (such as the [*restore target*](vssgloss-r.md)). If it defines a component set, writer modifications of an explicitly included component will propagate to its [*subcomponents*](vssgloss-s.md). In addition, the interface provides a mechanism for passing information about restore success and failure between writer and requester.

As during backup, there is insufficient information in the Backup Components Document itself to implement the restore. Again, the Writer Metadata Documents will be required to supply information about the actual paths of files to be restored and to discover what nonselectable components are part of the selectable components component set and therefore need to be restored.

See [Working with Selectability and Logical Paths](working-with-selectability-and-logical-paths.md) for information about the types of selectability and their usage.

## Use of Writer Component Document Information by the Requester

Each component is uniquely identified by the [*Writer Class ID*](vssgloss-w.md) of its parent writer, its name, and its [*logical path*](vssgloss-l.md).

The requester can use the [**IVssWriterComponentsExt**](/windows/win32/api/vsbackup/nl-vsbackup-ivsswritercomponentsext) interface returned by the [**IVssBackupComponents::GetWriterComponents**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritercomponents) method to obtain information about each stored component.

The component's name and logical path (among other items) can be found via the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface returned by [**IVssWriterComponentsExt::GetComponent**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswritercomponents-getcomponent).

> [!Note]  
> During the restore phase, the requester should call [**IVssWriterComponentsExt::GetComponent**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswritercomponents-getcomponent) or [**IVssWriterComponentsExt::GetComponentCount**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswritercomponents-getcomponentcount) only after the call to [**IVssBackupComponents::PreRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prerestore) has returned, to allow time for the writer to update the Backup Components Document. One example of such an update would be to change the restore target.

 

Information about each stored selectable component's parent writer can be found using [**IVssWriterComponentsExt::GetWriterInfo**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswritercomponents-getwriterinfo).

With this information, the Writer Metadata Documents can be queried and the matching document identified. Then, by using the [*logical path*](vssgloss-l.md), the requester can identify the dependent nonselectable components for each selectable component—that is, identify all members of the selectable component's [*component set*](vssgloss-c.md).

Using the [**IVssExamineWriterMetadata**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssexaminewritermetadata) interface, the requester now has full component information—including path specification (from the [**IVssWMComponent**](/windows/desktop/api/VsBackup/nl-vsbackup-ivsswmcomponent) interface)—for both selectable and nonselectable components it needs to back up or restore.

This is one reason why it is vital for a requester to save both the state of its own Backup Components Document and the Writer Metadata Documents of the writers it is backing up.

See [Working with Selectability and Logical Paths](working-with-selectability-and-logical-paths.md) for more detailed information.

 

 
