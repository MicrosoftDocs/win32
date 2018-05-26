---
Description: This stage of the backup initializes both the writer and the requester, filling in their internal data structures, specifying the backup and establishes writer/requester communication through the required call to IVssBackupComponentsGatherWriterMetadata. For more information, see Overview of Processing a Backup Under VSS.
ms.assetid: 1fc46062-c4a0-4aa2-ae05-3d7cded18584
title: Overview of Backup Initialization
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Overview of Backup Initialization

This stage of the backup initializes both the writer and the requester, filling in their internal data structures, specifying the backup and establishes writer/requester communication through the required call to [**IVssBackupComponents::GatherWriterMetadata**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata?branch=master). For more information, see [Overview of Processing a Backup Under VSS](overview-of-processing-a-backup-under-vss.md).

The following table shows the sequence of actions and events that are required for backup initialization.



| Requester action                                                                                                                                                                                                                                                                                                                            | Event                                                     | Writer action                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Creates an [**IVssBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) interface and initializes it to manage a backup (see [**CreateVssBackupComponents**](/windows/win32/VsBackup/nf-vsbackup-createvssbackupcomponents?branch=master), [**IVssBackupComponents::InitializeForBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-initializeforbackup?branch=master)) and optionally enable or disable writers on the system. | None                                                      | None                                                                                                                                                                                                                                                       |
| Optionally set the context for shadow copy operations and optionally query the system about the providers and shadow copies it supports (see [**IVssBackupComponents::SetContext**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setcontext?branch=master), [**IVssBackupComponents::Query**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-query?branch=master)).                                               | None                                                      | None                                                                                                                                                                                                                                                       |
| The requester can provide additional information on handling backup and restore operations (see [**IVssBackupComponents::SetBackupState**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupstate?branch=master))                                                                                                                                                        | None                                                      | None                                                                                                                                                                                                                                                       |
| Initiates asynchronous contact with writers (see [**IVssBackupComponents::GatherWriterMetadata**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata?branch=master))                                                                                                                                                                                           | [*Identify*](vssgloss-i.md#base-vssgloss-identify-event) | Creates a Writer Metadata Document (see [Working with the Writer Metadata Document](working-with-the-writer-metadata-document.md), [**CVssWriter::OnIdentify**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onidentify?branch=master), [**IVssCreateWriterMetadata**](/windows/win32/VsWriter/nl-vswriter-ivsscreatewritermetadata?branch=master)) |



 

## Requester Actions during Backup Initialization

An [**IVssBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) object can be used for only one backup. Therefore, a requester must proceed through to the end of the backup, including releasing the **IVssBackupComponents** interface. If the backup needs to terminate prematurely, the requester needs to call [**IVssBackupComponents::AbortBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-abortbackup?branch=master) and then release the **IVssBackupComponents** object (see [Aborting VSS Operations](aborting-vss-operations.md) for more information). Do not attempt to resume the **IVssBackupComponents** interface.

Typically, a requester's Backup Components Document is initialized as empty. A stored Backup Components Document can be loaded when [**IVssBackupComponents::InitializeForBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-initializeforbackup?branch=master) is called, typically in support of transportable shadow copied volumes. In this case, the writer-requester communication will be somewhat different than what is described below. (See [Importing Transportable Shadow Copied Volumes](importing-transportable-shadow-copied-volumes.md) for more information.)

To add volumes to the shadow copy set, a requester must first set the context for the shadow copy operation by calling [**IVssBackupComponents::SetContext**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setcontext?branch=master). If this method is not called, the default context for shadow copies, VSS\_CTX\_BACKUP, is used. For information about setting the shadow copy context, see [Shadow Copy Context Configurations](shadow-copy-context-configurations.md).

To begin the completion of its setup prior to backup, a requester must call [**IVssBackupComponents::SetBackupState**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupstate?branch=master). By doing this, a requester indicates to the writers:

-   The type of backup (as defined in [**VSS\_BACKUP\_TYPE**](/windows/win32/Vss/ne-vss-_vss_backup_type?branch=master))
-   Whether the backup includes a bootable system state
-   Whether the requester supports the selection of individual components or backs up entire volumes.

All requesters participating in backup and restore operations must always call [**IVssBackupComponents::GatherWriterMetadata**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata?branch=master). This method initiates writer-requester communication by generating a VSS [*Identify*](vssgloss-i.md#base-vssgloss-identify-event) event, in response to which a writer creates its metadata document.

Prior to calling [**IVssBackupComponents::GatherWriterMetadata**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata?branch=master), a requester has an opportunity to explicitly enable or disable certain specific writers and writer classes using [**IVssBackupComponents::EnableWriterClasses**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-enablewriterclasses?branch=master), [**IVssBackupComponents::DisableWriterInstances**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-disablewriterinstances?branch=master), and [**IVssBackupComponents::DisableWriterClasses**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-disablewriterclasses?branch=master) (by default, all classes are enabled). After **IVssBackupComponents::GatherWriterMetadata** is called, these calls have no effect.

Because there is no way to obtain a list of writers on the system prior to calling [**IVssBackupComponents::GatherWriterMetadata**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata?branch=master), requesters may consider creating and then deleting a second instance of [**IVssBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) to obtain the list.

It is not necessary to call [**IVssBackupComponents::GatherWriterStatus**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwriterstatus?branch=master) following the completion of [**IVssBackupComponents::GatherWriterMetadata**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata?branch=master). Writers that fail to process the [*Identify*](vssgloss-i.md#base-vssgloss-identify-event) event generated by the calls will not be part of the list of writers providing metadata found by [**IVssBackupComponents::GetWriterMetadataCount**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritermetadatacount?branch=master) and [**IVssBackupComponents::GetWriterMetadata**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritermetadata?branch=master) (see [Determining Writer Status](determining-writer-status.md)).

## Writer Actions during Backup Initialization

In response to the Identify event, VSS calls each writer's virtual handler method, [**CVssWriter::OnIdentify**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onidentify?branch=master). A writer creates its Writer Metadata Document by overriding the default implementation of **CVssWriter::OnIdentify** and using the [**IVssCreateWriterMetadata**](/windows/win32/VsWriter/nl-vswriter-ivsscreatewritermetadata?branch=master) interface.

Note that applications other than the current requester (for instance, system applications) can generate Identify events that must be handled by the writer. In addition, there is no way for a writer to determine from within [**CVssWriter::OnIdentify**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onidentify?branch=master) which application has generated the Identify event.

This being the case, given that a writer may receive several Identify events while processing a backup operation, a writer should never set state information in the [**CVssWriter::OnIdentify**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onidentify?branch=master) handler.

Instead, [**CVssWriter::OnIdentify**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onidentify?branch=master) should perform a consistent algorithm to create the writer's Writer Metadata Document, particularly because after a writer creates the document, neither the requester nor the writer can modify it. From this point forward, it is a read-only document.

This means that the number and type of [*components*](vssgloss-c.md#base-vssgloss-component) associated with a writer, which files are part of each component, and the explicit exclusion of files from backup or restore operations cannot be changed after a writer returns from processing the Identify event.

All writers participating with VSS are required to do the following:

1.  Indicate a restore method for all components managed by the writer using [**IVssCreateWriterMetadata::SetRestoreMethod**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-setrestoremethod?branch=master).
2.  Add at least one component using [**IVssCreateWriterMetadata::AddComponent**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-addcomponent?branch=master) (see [Definition of Components by Writers](definition-of-components-by-writers.md) for more information on component specification).

A writer indicates the files to participate in a backup or restore operation by adding [*file sets*](vssgloss-f.md#base-vssgloss-file-set)—a combination of a path, file specification, and a recursion flag—to a given component using [**IVssCreateWriterMetadata::AddFilesToFileGroup**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-addfilestofilegroup?branch=master), [**IVssCreateWriterMetadata::AddDatabaseFiles**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabasefiles?branch=master), or [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles?branch=master), depending on type (See [Adding Files to Components](definition-of-components-by-writers.md#adding-files-to-a-component).)

A writer may also have one or more empty components, components to which no files have been added. These are very useful in organizing the writer's components. (See [Logical Pathing of Components](logical-pathing-of-components.md).)

A writer uses [**IVssCreateWriterMetadata::AddExcludeFiles**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-addexcludefiles?branch=master) to explicitly prevent files from being included in the backup. This explicit exclusion is useful because wildcard characters can be used to specify files for inclusion (see [Exclude File List Specification](writer-metadata-document-contents.md#exclude-file-list-specification)). Note that the exclude file list takes precedence over component files lists.

[**IVssCreateWriterMetadata::AddAlternateLocationMapping**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-addalternatelocationmapping?branch=master) is used to create [*alternate location mappings*](vssgloss-a.md#base-vssgloss-alternate-location-mapping) for specified file sets that have been added to one of the writer's components. These mappings are used during file restore when restoring to a file's original location is not possible or desirable. (See [Overview of Actual File Restoration](overview-of-actual-file-restoration.md) and [Non-Default Backup and Restore Locations](non-default-backup-and-restore-locations.md).)

Because the backup file set is specified in the Writer Metadata Document, it cannot later be modified. Therefore, a writer should be coded so that the file set's definition will include all files needed in the backup, either by name or through wildcard characters. Conceivably, this may include some files that might be created after the Identify event.

 

 



