---
Description: 'In preparing for a restore, a requester uses the stored Writer Metadata Documents in conjunction with its own retrieved Backup Components Document to determine what is to be restored and how.'
ms.assetid: '36cf188f-fce6-467c-a200-cbd9dc8f31a6'
title: Overview of Preparing for Restore
---

# Overview of Preparing for Restore

In preparing for a restore, a requester uses the stored Writer Metadata Documents in conjunction with its own retrieved Backup Components Document to determine what is to be restored and how. For more information, see [Overview of Processing a Restore Under VSS](overview-of-processing-a-restore-under-vss.md).

Following the selection of restore candidate components, writers currently running on the system access the requester's Backup Components Document. Writers use this access to indicate how to cause minimum difficulty for running services due to the restore.

After this is completed, the requester has enough information to determine which files will need to be restored, as well as where and how they should be restored. (For more information, see [Generating a Restore Set](generating-a-restore-set.md).)

The following table shows the sequence of actions and events that are required to prepare for a restore operation.



| Requester action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Event                                                         | Writer action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Retrieve information from the Backup Components Document about the components [*explicitly included*](vssgloss-e.md#base-vssgloss-explicit-component-inclusion) in the backup operation (see [**IVssBackupComponents::GetWriterComponents**](ivssbackupcomponents-getwritercomponents.md)) Examine retrieved Writer Metadata Documents to get details about those components explicitly included in the backup, and any find [*implicitly included*](vssgloss-i.md#base-vssgloss-implicit-component-inclusion) subcomponents. (See [**IVssExamineWriterMetadata**](ivssexaminewritermetadata.md), [**IVssWMComponent**](ivsswmcomponent.md).)<br/> | None                                                          | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Select components and component sets to be restored (see [**IVssBackupComponents::SetSelectedForRestore**](ivssbackupcomponents-setselectedforrestore.md) and [**IVssBackupComponents::AddRestoreSubcomponent**](ivssbackupcomponents-addrestoresubcomponent.md).)                                                                                                                                                                                                                                                                                                                                                                                          | None                                                          | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| The requester allows the writer to update the Backup Components Document and may optionally communicate any special restore options to the writer. (See [**IVssBackupComponents::SetRestoreOptions**](ivssbackupcomponents-setrestoreoptions.md), [**IVssBackupComponents::AddNewTarget**](ivssbackupcomponents-addnewtarget.md), and [**IVssBackupComponents::PreRestore**](ivssbackupcomponents-prerestore.md).)                                                                                                                                                                                                                                         | [*PreRestore*](vssgloss-p.md#base-vssgloss-prerestore-event) | The writer determines participation in the restore, prepares files to restore, and optionally modifies Backup Components Document if necessary. (See [**CVssWriter::OnPreRestore**](cvsswriter-onprerestore.md), [**IVssComponent**](ivsscomponent.md), [**IVssComponent::IsSelectedForRestore**](ivsscomponent-isselectedforrestore.md), [**IVssComponent::GetRestoreOptions**](ivsscomponent-getrestoreoptions.md), [**IVssComponent::SetRestoreTarget**](ivsscomponent-setrestoretarget.md), [**IVssComponent::SetRestoreMetadata**](ivsscomponent-setrestoremetadata.md), [**IVssComponent::AddDirectedTarget**](ivsscomponent-adddirectedtarget.md).) |
| The requester waits on writers to handle the [**PreRestore**](ivssbackupcomponents-prerestore.md) event with [**IVssAsync**](ivssasync.md). It should also verify writer status. (See [**IVssBackupComponents::GatherWriterStatus**](ivssbackupcomponents-gatherwriterstatus.md), [**IVssBackupComponents::GetWriterStatus**](ivssbackupcomponents-getwriterstatus.md).)                                                                                                                                                                                                                                                                                  | None                                                          | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |



 

## Requester Actions during Restore Preparations

To determine which components are candidates for restore, the requester must do the following:

-   Establish the component and the [*component set*](vssgloss-c.md#base-vssgloss-component-set) structure used to make the backup.
-   Examine the components' [*selectability for restore*](vssgloss-s.md#base-vssgloss-selectability-for-restore).
-   Use selectability guidelines ([Working with Selectability for Restore and Subcomponents](working-with-selectability-for-restore-and-subcomponents.md)) to choose components to include.
-   Use component [*file set*](vssgloss-f.md#base-vssgloss-file-set) information to determine which files on the backup media must be restored.

To do this, the requester needs to examine [*explicitly included*](vssgloss-e.md#base-vssgloss-explicit-component-inclusion) components in the stored Backup Components Document. This component information is available on a writer-by-writer basis using [**IVssBackupComponents::GetWriterComponents**](ivssbackupcomponents-getwritercomponents.md), which returns instances of the [**IVssWriterComponentsExt**](ivsswritercomponentsext.md) interface, from which both writer information and instances of the [**IVssComponent**](ivsscomponent.md) interface can be retrieved.

As noted elsewhere ([Use of Components by the Requester](use-of-components-by-the-requestor.md)), the Backup Components Document and the **IVssComponent** interface do not contain enough information to support the backup. Therefore, the requester must examine the corresponding stored Writer Metadata Document by using [**IVssExamineWriterMetadata**](ivssexaminewritermetadata.md) (see [Writer Identification Information](writer-metadata-document-contents.md#-win32-writer-identification-information)).

The number of components each writer manages is returned by [**IVssExamineWriterMetadata::GetFileCounts**](ivssexaminewritermetadata-getfilecounts.md). The requester can then use [**IVssExamineWriterMetadata::GetComponent**](ivssexaminewritermetadata-getcomponent.md) to get an [**IVssWMComponent**](ivsswmcomponent.md) interface for each component a writer manages.

By examining the components' [*selectability for backup*](vssgloss-s.md#base-vssgloss-selectability-for-backup) and [*logical paths*](vssgloss-l.md#base-vssgloss-logical-path) (see [Working with Selectability and Logical Paths](working-with-selectability-and-logical-paths.md)), a requester is able to identify the components that defined backup-time component sets (explicitly included components), and the subcomponents members of those sets (implicitly included components).

Requesters indicate through the Backup Components Document if a component is to be explicitly restored, using either [**IVssBackupComponents::SetSelectedForRestore**](ivssbackupcomponents-setselectedforrestore.md) or [**IVssBackupComponents::AddRestoreSubcomponent**](ivssbackupcomponents-addrestoresubcomponent.md). The choice of method will depend on how the component was originally backed up and its [*selectability for restore*](vssgloss-s.md#base-vssgloss-selectability-for-restore). These components explicitly included for restore designate other components which are implicitly included (see [Working with Selectability for Restore and Subcomponents](working-with-selectability-for-restore-and-subcomponents.md) for details).

A requester may explicitly include none of a currently executing writer's components for restore using [**IVssBackupComponents::SetSelectedForRestore**](ivssbackupcomponents-setselectedforrestore.md) or [**IVssBackupComponents::AddRestoreSubcomponent**](ivssbackupcomponents-addrestoresubcomponent.md). In this case, that writer will not receive any VSS events for the remainder of the restore operation.

Explicitly using either [**IVssBackupComponents::SetSelectedForRestore**](ivssbackupcomponents-setselectedforrestore.md) or [**IVssBackupComponents::AddRestoreSubcomponent**](ivssbackupcomponents-addrestoresubcomponent.md) to select a component of a writer that is not currently running returns a VSS\_E\_OBJECT\_NOT\_FOUND error. See [Restores without Writer Participation](restores-without-writer-participation.md) for information on restoring the data of missing writers.

To enable a writer to have complete information upon which to act, writer-specific restore options and indication of an incremental restore can be sent to the writers by requester calls to [**IVssBackupComponents::SetRestoreOptions**](ivssbackupcomponents-setrestoreoptions.md) and [**IVssBackupComponents::SetAdditionalRestores**](ivssbackupcomponents-setadditionalrestores.md), respectively.

At this point, a requester has finished its preparation, and it generates a **PreRestore** event by calling [**IVssBackupComponents::PreRestore**](ivssbackupcomponents-prerestore.md), allowing writers to prepare for the actual restore.

## Writer Actions during Restore Preparations

Writer preparation for the restore operation occurs when handling the [**PreRestore**](ivssbackupcomponents-prerestore.md) event with the virtual method [**CVssWriter::OnPreRestore**](cvsswriter-onprerestore.md). The default implementation simply returns without taking any action. Writers may choose to override the default implementation to exercise more control by:

-   Overriding [*restore methods*](vssgloss-r.md#base-vssgloss-restore-method) with [*restore targets*](vssgloss-r.md#base-vssgloss-restore-target)
-   Defining [*directed targets*](vssgloss-d.md#base-vssgloss-directed-targeting)
-   Creating error messages and additional data
-   Supplying backup stamp information

The event handler [**CVssWriter::OnPreRestore**](cvsswriter-onprerestore.md) receives an instance of the [**IVssWriterComponents**](ivsswritercomponents.md), from which it can obtain [**IVssComponent**](ivsscomponent.md) interfaces for those of its components explicitly included in the Backup Components Document during backup.

Information about subcomponents implicitly included in backup operations and explicitly included in restores by using an instance of the **IVssComponent** corresponding to the component that defined its backup [*component set*](vssgloss-c.md#base-vssgloss-component-set).

The [**IVssComponent::IsSelectedForRestore**](ivsscomponent-isselectedforrestore.md) method is used to determine whether an explicitly included for backup component is to be restored.

To determine if a backup subcomponent was explicitly included in the restore, writers use [**IVssComponent::GetRestoreSubcomponent**](ivsscomponent-getrestoresubcomponent.md).

The writer should examine the [*file set*](vssgloss-f.md#base-vssgloss-file-set) in each component and determine if it needs to take actions to support the restore. The writer will need to evaluate if it wants its current files overwritten, or if it will require restoration to new locations. Actions can include the following:

-   Getting and acting on any writer- or requester-specific options governing restore operations (see [**IVssComponent::GetRestoreOptions**](ivsscomponent-getrestoreoptions.md))
-   Closing and making writable any currently open files
-   Updating the restore target (for instance, to force restoration to an alternate location mapping). See [**IVssComponent::SetRestoreTarget**](ivsscomponent-setrestoretarget.md).
-   Communicating with the requester via private metadata (see [**IVssComponent::SetRestoreMetadata**](ivsscomponent-setrestoremetadata.md))
-   Indicating that a file should be restored by remapping through the definition of [*directed targets*](vssgloss-d.md#base-vssgloss-directed-targeting) (see [**IVssComponent::AddDirectedTarget**](ivsscomponent-adddirectedtarget.md))

The instance of [**IVssComponent**](ivsscomponent.md) used will either be that created by the component's explicit inclusion in the Backup Components Document during backup, or that of the component defining the backup component set of which it was a member (see [Working with Selectability For Restore and Subcomponents](working-with-selectability-for-restore-and-subcomponents.md)).

 

 




