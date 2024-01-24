---
description: After calling IVssBackupComponents::GatherWriterMetadata, a requester uses the instance of the IVssAsync interface returned from this call to determine when all writers on the system have finished constructing their Writer Metadata Documents.
ms.assetid: 04658d50-04f0-4189-8b88-ff152f1bf482
title: Overview of the Backup Discovery Phase
ms.topic: article
ms.date: 05/31/2018
---

# Overview of the Backup Discovery Phase

After calling [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata), a requester uses the instance of the [**IVssAsync**](/windows/desktop/api/Vss/nn-vss-ivssasync) interface returned from this call to determine when all writers on the system have finished constructing their Writer Metadata Documents. For more information, see [Overview of Processing a Backup Under VSS](overview-of-processing-a-backup-under-vss.md).

At this point, the requester can begin a discovery phase, examining metadata to determine what applications are running and which volumes must be shadow copied to get a complete backup. The following table shows the sequence of actions and events that are required for the backup discovery phase.



| Requester action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Event | Writer action                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|-----------------------------------------------------------------------------------|
| Retrieve Writer Metadata Documents (see [**IVssBackupComponents::GetWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritermetadata), [**IVssExamineWriterMetadata**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssexaminewritermetadata)).                                                                                                                                                                                                                                                                                                                                                 | None  | During this period, writers may be able to continue with their normal operations. |
| Use the list of components and their [*file sets*](vssgloss-f.md), as well as excluded files, to obtain a list of volumes and files involved in the backup (see [**IVssWMComponent**](/windows/desktop/api/VsBackup/nl-vsbackup-ivsswmcomponent), [**IVssWMFiledesc**](/windows/desktop/api/VsWriter/nl-vswriter-ivsswmfiledesc)).                                                                                                                                                                                                                                                                      | None  | None                                                                              |
| Choose which components in the writer's Writer Metadata Document to back up. Call [**IVssBackupComponents::AddComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent) for each component to add it to the Backup Components Document. (See [Working with Selectability for Backup](working-with-selectability-for-backup.md) and [Working with the Backup Components Document](working-with-the-backup-components-document.md).)                                                                                                                      | None  | None                                                                              |
| Initialize the shadow copy set, context and check for supported volumes (see [**IVssBackupComponents::StartSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-startsnapshotset), [**IVssBackupComponents::IsVolumeSupported**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-isvolumesupported)).                                                                                                                                                                                                                                                                                   | None  | None                                                                              |
| If performing a non-component backup, add the desired target volumes from the Writer Metadata Document to the shadow copy set by calling [**IVssBackupComponents::AddToSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addtosnapshotset) for each volume. Otherwise, for the components in the Writer Metadata Document that were already added to the Backup Components Document (by calling [**AddComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent)), the requester must also call **IVssBackupComponents::AddToSnapshotSet** for each affected volume. | None  | None                                                                              |



 

## Writer Actions during the Discovery Phase

Because the discovery phase of a backup consists primarily of a requester processing the information it has retrieved from Writer Metadata Documents, there are few if any requirements on a writer.

In theory, a writer could continue to run normally at this point. However, it may be desirable for writers to begin preparations for the coming shadow copy and backup operations.

## Requester Actions during the Discovery Phase

A requester uses the [**IVssExamineWriterMetadata**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssexaminewritermetadata) objects obtained through [**IVssBackupComponents::GetWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritermetadata) to iterate over all the writers' metadata and selecting those writers whose data it intends to back up.

At this point, the requester will need to generate an initial list of each writer's backup candidates by iterating over the writer's components using [**IVssExamineWriterMetadata::GetComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getcomponent). This provides the requester with [**IVssWMComponent**](/windows/desktop/api/VsBackup/nl-vsbackup-ivsswmcomponent) objects, from which you can get the specifications for the files to be backed up using [**IVssWMComponent::GetFile**](/windows/desktop/api/VsBackup/nf-vsbackup-ivsswmcomponent-getfile), [**IVssWMComponent::GetDatabaseFile**](/windows/desktop/api/VsBackup/nf-vsbackup-ivsswmcomponent-getdatabasefile), and [**IVssWMComponent::GetDatabaseLogFile**](/windows/desktop/api/VsBackup/nf-vsbackup-ivsswmcomponent-getdatabaselogfile).

Because the [**IVssWMFiledesc**](/windows/desktop/api/VsWriter/nl-vswriter-ivsswmfiledesc) object can use wildcard characters to hold file location information, it may be necessary to use functions such as [**FindFirstFile**](/windows/win32/api/fileapi/nf-fileapi-findfirstfilea), [**FindFirstFileEx**](/windows/win32/api/fileapi/nf-fileapi-findfirstfileexa), and [**FindNextFile**](/windows/win32/api/fileapi/nf-fileapi-findnextfilea).

Until the shadow copy has been completed, it is still possible for writers to add or remove files from disk in the normal course of their work, so you should not generate the actual list of files to be backed up at this time.

Instead, the initial list of files and volumes to be backed up is found at this point by doing the following:

1.  Examining all selectable for backup and nonselectable components in each writer's Writer Metadata Document (using [**IVssExamineWriterMetadata**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssexaminewritermetadata)) and organizing them into [*component sets*](vssgloss-c.md) use [*logical path*](vssgloss-l.md) (see [Working with Selectability and Logical Paths](working-with-selectability-and-logical-paths.md))
2.  [*Including explicitly*](vssgloss-e.md) all required components (nonselectable for backup components without selectable for backup ancestors) in the Backup Components Document using [**IVssBackupComponents::AddComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent)
3.  Choosing to explicitly include optional selectable for backup components that do not define a component set (using [**IVssBackupComponents::AddComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent))
4.  Selecting [*component sets*](vssgloss-c.md) for participation in a backup by explicitly adding their defining selectable for backup component (using [**IVssBackupComponents::AddComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent)), which [*implicitly includes*](vssgloss-i.md) the component set's [*subcomponents*](vssgloss-s.md).
5.  Using [*file set*](vssgloss-f.md) information in the selected writers' Writer Metadata Document and volume management functions, a requester determines the paths of files to be backed up and the volumes that will need to be shadow copied

Note that only the components explicitly included (using [**IVssBackupComponents::AddComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent)) in the backup and in the Backup Components Document will have instances of the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface added to that document. These instances will be used to examine and modify component settings for both explicitly included components and any of their implicitly included subcomponents (see [Selectability and Working with Component Properties](selectability-and-working-with-component-properties.md)).

If a writer includes any of a writer's components, it must add all of its required components. However, a requester is also free to entirely skip all of a writer's component sets. If none of a writer's components are explicitly selected, the writer is not selected, and VSS inhibits that writer from participating in the rest of the backup operation.

The requester initiates the shadow copy set that will contain the selected volumes by calling [**IVssBackupComponents::StartSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-startsnapshotset).

If the volume can participate in a shadow copy (which can be checked with [**IVssBackupComponents::IsVolumeSupported**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-isvolumesupported)), the requester can add that volume to the shadow copy set using [**IVssBackupComponents::AddToSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addtosnapshotset).

Although it is not generally useful, a requester can sometimes also choose which [*provider*](vssgloss-p.md) will maintain the shadow copy for a given volume (see [Selecting Providers](selecting-providers.md) for details).

Care should be given to the handling of a volume containing mounted folders or reparse points. A mounted folder or reparse point can appear in a shadow copy and can be backed up. However, a mounted folder or reparse point cannot be traversed on the shadow copied volume (see [Working with Mounted Folders and Reparse Points](working-with-reparse-and-mount-points.md)).

At this point in the backup, the Backup Components Document is initialized and filled. In future operations, writers and requesters can use the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface to communicate with each other.

Writers are given access to the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface when handling the [*PrepareForBackup*](vssgloss-p.md), [*PostSnapshot*](vssgloss-p.md), and [*BackupComplete*](vssgloss-b.md) events.

 

 
