---
description: Following a restore, writers check the status of the operation so that they can make use of the restored data and deal with errors.
ms.assetid: f9def67a-c4ea-4014-929f-51fbd10d770a
title: Overview of Restore Clean up and Termination
ms.topic: article
ms.date: 05/31/2018
---

# Overview of Restore Clean up and Termination

Following a restore, writers check the status of the operation so that they can make use of the restored data and deal with errors. The requester must wait for the completion of this activity. For more information, see [Overview of Processing a Restore Under VSS](overview-of-processing-a-restore-under-vss.md).

The following table shows the sequence of actions and events that are required after a restore operation has taken place.



| Requester action                                                                                                                                                                                                                                                                                                                                                              | Event                                                           | Writer action                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The requester indicates the end of the restore (see [**IVssBackupComponents::PostRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-postrestore)).                                                                                                                                                                                                                                           | [*PostRestore*](vssgloss-p.md) | The writer conducts post-restore cleanup, and handles restoration failures and files that have been restored to nonstandard locations (see [**CVssWriter::OnPostRestore**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onpostrestore), [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent)). |
| The requester waits on writers to handle the [**PostRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-postrestore) event with [**IVssAsync**](/windows/desktop/api/Vss/nn-vss-ivssasync). It should also verify writer status (see [**IVssBackupComponents::GatherWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwriterstatus), [**IVssBackupComponents::GetWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwriterstatus)). | None                                                            | None                                                                                                                                                                                                                                               |
| The requester releases the [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface.                                                                                                                                                                                                                                                                                    | None                                                            | None                                                                                                                                                                                                                                               |



 

## Requester Actions during Cleanup and Termination

At this point, a requester indicates the end of its file restoration activities by generating a [*PostRestore*](vssgloss-p.md) event by calling [**IVssBackupComponents::PostRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-postrestore).

The requester's actions are limited to waiting on the writers, which may need to perform some final cleanup and handle restore errors, and releasing the [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface after all writers have returned from handling the [*PostRestore*](vssgloss-p.md) event.

## Writer Actions during Cleanup and Termination

The [*PostRestore*](vssgloss-p.md) event is handled by the virtual method [**CVssWriter::OnPostRestore**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onpostrestore). The default implementation simply returns **true** without taking any action. If a writer needs to exercise more control of the post-restore situation, it can override this method.

In addition to any normal cleanup (such as removing temporary files) that a writer might perform in [**CVssWriter::OnPostRestore**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onpostrestore), it can handle the success or failure of restore operations.

How it handles restore errors, files restored to an alternate location, and the need for future restores are completely at the writer's discretion. Typical actions might include comparing files in alternate or new locations with files currently in use, merging data from multiple files, or starting new sessions connected to the new data files. VSS provides the following mechanisms for supporting this on a component-by-component basis:

-   Success or failure in restoring any component can be found with [**IVssComponent::GetFileRestoreStatus**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getfilerestorestatus).
-   The use of alternate location mappings in restoring files will be indicated by [**IVssComponent::GetAlternateLocationMapping**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getalternatelocationmapping).
-   Determining if a restore is incremental and will require further restores is done by calling [**IVssComponent::GetAdditionalRestores**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getadditionalrestores). Writers that need a complete restoration of their data should not restart until this method returns false.
-   Writers can determine if the requester has needed to restore files to a previously unspecified location using [**IVssComponent::GetNewTargetCount**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getnewtargetcount) and [**IVssComponent::GetNewTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getnewtarget)

(For more information on restoring files to non-default locations, see [Non-Default Backup and Restore Locations](non-default-backup-and-restore-locations.md).)

As with any [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) method, the information returned by a given instance applies to those components [*explicitly included*](vssgloss-e.md) for backup and any of its [*implicitly included*](vssgloss-i.md) for backup subcomponents, including those subcomponents explicitly included for restore by the requester using [**IVssBackupComponents::AddRestoreSubcomponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addrestoresubcomponent) (see [Working with Selectability For Restore and Subcomponents](working-with-selectability-for-restore-and-subcomponents.md) for details).

Because the writers will require access to the Backup Components Document, it is important that the requester not release the [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface until writers have finished processing.

 

 



