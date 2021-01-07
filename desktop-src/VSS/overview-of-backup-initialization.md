---
description: This stage of the backup initializes both the writer and the requester, filling in their internal data structures, specifying the backup and establishes writer/requester communication through the required call to IVssBackupComponents::GatherWriterMetadata. For more information, see Overview of Processing a Backup Under VSS.
ms.assetid: 1fc46062-c4a0-4aa2-ae05-3d7cded18584
title: Overview of Backup Initialization
ms.topic: article
ms.date: 05/31/2018
---

# Overview of Backup Initialization

This stage of the backup initializes both the writer and the requester, filling in their internal data structures, specifying the backup and establishes writer/requester communication through the required call to [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata). For more information, see [Overview of Processing a Backup Under VSS](overview-of-processing-a-backup-under-vss.md).

The following table shows the sequence of actions and events that are required for backup initialization.



| Requester action                                                                                                                                                                                                                                                                                                                            | Event                                                     | Writer action                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Creates an [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface and initializes it to manage a backup (see [**CreateVssBackupComponents**](/windows/desktop/api/VsBackup/nf-vsbackup-createvssbackupcomponents), [**IVssBackupComponents::InitializeForBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-initializeforbackup)) and optionally enable or disable writers on the system. | None                                                      | None                                                                                                                                                                                                                                                       |
| Optionally set the context for shadow copy operations and optionally query the system about the providers and shadow copies it supports (see [**IVssBackupComponents::SetContext**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setcontext), [**IVssBackupComponents::Query**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-query)).                                               | None                                                      | None                                                                                                                                                                                                                                                       |
| The requester can provide additional information on handling backup and restore operations (see [**IVssBackupComponents::SetBackupState**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupstate))                                                                                                                                                        | None                                                      | None                                                                                                                                                                                                                                                       |
| Initiates asynchronous contact with writers (see [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata))                                                                                                                                                                                           | [*Identify*](vssgloss-i.md) | Creates a Writer Metadata Document (see [Working with the Writer Metadata Document](working-with-the-writer-metadata-document.md), [**CVssWriter::OnIdentify**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onidentify), [**IVssCreateWriterMetadata**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscreatewritermetadata)) |



 

## Requester Actions during Backup Initialization

An [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) object can be used for only one backup. Therefore, a requester must proceed through to the end of the backup, including releasing the **IVssBackupComponents** interface. If the backup needs to terminate prematurely, the requester needs to call [**IVssBackupComponents::AbortBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-abortbackup) and then release the **IVssBackupComponents** object (see [Aborting VSS Operations](aborting-vss-operations.md) for more information). Do not attempt to resume the **IVssBackupComponents** interface.

Typically, a requester's Backup Components Document is initialized as empty. A stored Backup Components Document can be loaded when [**IVssBackupComponents::InitializeForBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-initializeforbackup) is called, typically in support of transportable shadow copied volumes. In this case, the writer-requester communication will be somewhat different than what is described below. (See [Importing Transportable Shadow Copied Volumes](importing-transportable-shadow-copied-volumes.md) for more information.)

To add volumes to the shadow copy set, a requester must first set the context for the shadow copy operation by calling [**IVssBackupComponents::SetContext**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setcontext). If this method is not called, the default context for shadow copies, VSS\_CTX\_BACKUP, is used. For information about setting the shadow copy context, see [Shadow Copy Context Configurations](shadow-copy-context-configurations.md).

To begin the completion of its setup prior to backup, a requester must call [**IVssBackupComponents::SetBackupState**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupstate). By doing this, a requester indicates to the writers:

-   The type of backup (as defined in [**VSS\_BACKUP\_TYPE**](/windows/desktop/api/Vss/ne-vss-vss_backup_type))
-   Whether the backup includes a bootable system state
-   Whether the requester supports the selection of individual components or backs up entire volumes.

All requesters participating in backup and restore operations must always call [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata). This method initiates writer-requester communication by generating a VSS [*Identify*](vssgloss-i.md) event, in response to which a writer creates its metadata document.

Prior to calling [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata), a requester has an opportunity to explicitly enable or disable certain specific writers and writer classes using [**IVssBackupComponents::EnableWriterClasses**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-enablewriterclasses), [**IVssBackupComponents::DisableWriterInstances**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-disablewriterinstances), and [**IVssBackupComponents::DisableWriterClasses**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-disablewriterclasses) (by default, all classes are enabled). After **IVssBackupComponents::GatherWriterMetadata** is called, these calls have no effect.

Because there is no way to obtain a list of writers on the system prior to calling [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata), requesters may consider creating and then deleting a second instance of [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) to obtain the list.

It is not necessary to call [**IVssBackupComponents::GatherWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwriterstatus) following the completion of [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata). Writers that fail to process the [*Identify*](vssgloss-i.md) event generated by the calls will not be part of the list of writers providing metadata found by [**IVssBackupComponents::GetWriterMetadataCount**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritermetadatacount) and [**IVssBackupComponents::GetWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritermetadata) (see [Determining Writer Status](determining-writer-status.md)).

## Writer Actions during Backup Initialization

In response to the Identify event, VSS calls each writer's virtual handler method, [**CVssWriter::OnIdentify**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onidentify). A writer creates its Writer Metadata Document by overriding the default implementation of **CVssWriter::OnIdentify** and using the [**IVssCreateWriterMetadata**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscreatewritermetadata) interface.

Note that applications other than the current requester (for instance, system applications) can generate Identify events that must be handled by the writer. In addition, there is no way for a writer to determine from within [**CVssWriter::OnIdentify**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onidentify) which application has generated the Identify event.

This being the case, given that a writer may receive several Identify events while processing a backup operation, a writer should never set state information in the [**CVssWriter::OnIdentify**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onidentify) handler.

Instead, [**CVssWriter::OnIdentify**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onidentify) should perform a consistent algorithm to create the writer's Writer Metadata Document, particularly because after a writer creates the document, neither the requester nor the writer can modify it. From this point forward, it is a read-only document.

This means that the number and type of [*components*](vssgloss-c.md) associated with a writer, which files are part of each component, and the explicit exclusion of files from backup or restore operations cannot be changed after a writer returns from processing the Identify event.

All writers participating with VSS are required to do the following:

1.  Indicate a restore method for all components managed by the writer using [**IVssCreateWriterMetadata::SetRestoreMethod**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-setrestoremethod).
2.  Add at least one component using [**IVssCreateWriterMetadata::AddComponent**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addcomponent) (see [Definition of Components by Writers](definition-of-components-by-writers.md) for more information on component specification).

A writer indicates the files to participate in a backup or restore operation by adding [*file sets*](vssgloss-f.md)—a combination of a path, file specification, and a recursion flag—to a given component using [**IVssCreateWriterMetadata::AddFilesToFileGroup**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addfilestofilegroup), [**IVssCreateWriterMetadata::AddDatabaseFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabasefiles), or [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles), depending on type (See [Adding Files to Components](definition-of-components-by-writers.md).)

A writer may also have one or more empty components, components to which no files have been added. These are very useful in organizing the writer's components. (See [Logical Pathing of Components](logical-pathing-of-components.md).)

A writer uses [**IVssCreateWriterMetadata::AddExcludeFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addexcludefiles) to explicitly prevent files from being included in the backup. This explicit exclusion is useful because wildcard characters can be used to specify files for inclusion (see [Exclude File List Specification](writer-metadata-document-contents.md)). Note that the exclude file list takes precedence over component files lists.

[**IVssCreateWriterMetadata::AddAlternateLocationMapping**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addalternatelocationmapping) is used to create [*alternate location mappings*](vssgloss-a.md) for specified file sets that have been added to one of the writer's components. These mappings are used during file restore when restoring to a file's original location is not possible or desirable. (See [Overview of Actual File Restoration](overview-of-actual-file-restoration.md) and [Non-Default Backup and Restore Locations](non-default-backup-and-restore-locations.md).)

Because the backup file set is specified in the Writer Metadata Document, it cannot later be modified. Therefore, a writer should be coded so that the file set's definition will include all files needed in the backup, either by name or through wildcard characters. Conceivably, this may include some files that might be created after the Identify event.

 

 



