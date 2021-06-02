---
description: A requester is any application that uses the VSS API (specifically the IVssBackupComponents interface) to request the services of the Volume Shadow Copy Service to create and manage shadow copies and shadow copy sets of one or more volumes.
ms.assetid: e49920d0-5b66-4aa1-b3ca-641629df5f8a
title: Requesters
ms.topic: article
ms.date: 05/31/2018
---

# Requesters

A [*requester*](vssgloss-r.md) is any application that uses the VSS API (specifically the [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface) to request the services of the Volume Shadow Copy Service to create and manage shadow copies and shadow copy sets of one or more volumes.

The most typical example of a requester (and the only one addressed in this documentation) is a VSS-aware backup/restore application, which uses shadow-copied data as a stable source for its backup operations.

In addition to initiating shadow copies, backup/recover requester applications communicate with data producers (writers) to gather information on the system and to signal writers to prepare their data for backup.

## Requester State

A requester maintains its state information in an XML-based metadata object called the Backup Components Document. The requester metadata is necessary, but not sufficient to allow a requester to back up and then restore a file system. The reasons for this are the following:

-   During a backup operation, only a subset of all the components involved in the backup—[*nonselectable for backup*](vssgloss-s.md) components without selectable for backup ancestors and selectable for backup components that have been [*included explicitly*](vssgloss-e.md) in the backup—have had their information added to the requester's Backup Components Document.
-   The information even for those components added to the Backup Components Document is incomplete—file and path specifications are not included.
-   During restore operations, a component [*implicitly included*](vssgloss-i.md) in the backup may be [*selectable for restore*](vssgloss-s.md) and therefore can be explicitly included in the restore. This will require the updating of the requester's Backup Components Document with information from stored copies of a writer's Writer Metadata Document.

To allow for full specification of a backup or restore operation, the VSS API allows the requester to query running writers' metadata (during backups) or examine stored writer metadata (during restores). In addition, a writer can modify component information in the Backup Components Document in the course of a backup or restore operation.

Using the information about which components have been selected for backup and restore and the rules regarding component selection (for more information, see [Setting up Component Organization](definition-of-components-by-writers.md) and [Working with Selectability and Logical Paths](working-with-selectability-and-logical-paths.md)), a requester can determine which files of which writer it needs to back up or restore, and where it can find those files.

As part of a backup, both requester and writer metadata must be stored so that it can be used in the restore. Conversely, restore operations require the retrieval of the old Backup Components and Writer Metadata Documents to obtain full instructions on restoring files.

## Requester Interprocess Communication

The requester maintains control over VSS backup and restore operations by generating COM events through various calls in the requester API. These calls can do the following:

-   Make requests of the providers, for example, [**IVssBackupComponents::DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset) causes the provider to create a shadow copy of the selected volume.
-   Trigger the writers to return information, for example, [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata) enables the requester to obtain each writer's Writer Metadata Document.
-   Require writers to prepare for or handle various phases of the shadow copy and backup operations, for example, [**IVssBackupComponents::PrepareForBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup) signals writers to set up for the I/O freeze.

A requester receives information from the writers through live or stored Writer Metadata Documents and through the use of the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface, which the writer can update.

## Life Cycle of a Requester during Backup

The following is a summary of the requester life cycle for backup:

1.  Instantiate and initialize VSS API interfaces.
2.  Contact writers and retrieve their information.
3.  Choose data to back up.
4.  Request a shadow copy of the provider.
5.  Back up the data.
6.  Release the interface and the shadow copy.

## Life Cycle of a Requester during Restore

The restore life cycle does not require a shadow copy, but still requires writer cooperation:

1.  Instantiate VSS API interfaces.
2.  Initialize the requester for the restore operation by loading a stored Backup Components Document.
3.  Retrieve stored Writer Metadata and Backup Components Documents.
4.  Contact the writers to initialize cooperation.
5.  Check for writer updates to the Backup Components Document.
6.  Restore the data.

 

 



