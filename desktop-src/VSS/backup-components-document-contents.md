---
Description: 'The Backup Components Document is maintained by instances of the IVssBackupComponents interface.'
ms.assetid: '8c7ebba8-58c4-4733-ba59-802abf902c5e'
title: Backup Components Document Contents
---

# Backup Components Document Contents

The Backup Components Document is maintained by instances of the [**IVssBackupComponents**](ivssbackupcomponents.md) interface. This interface also contains numerous methods for controlling backup operations, manipulating shadow copies, and querying the system state. However, not all of the document's information is directly accessible through this interface.

The Backup Components Document consists of several sets of data:

-   Information about which components were explicitly included in a backup or restore operation
-   A representation of the stored component and writer information
-   State information about the backup/recover operation

While the component information is available to both the requester and the writer, only the writer has access to the state information.

## Component Inclusion Information

The Backup Components Document contains a list of those components explicitly included in backup and restore by the requester. The list contains the following:

-   Explicitly included [*selectable components*](vssgloss-s.md#base-vssgloss-selectable-component).

    The inclusion of these files in backup operations is indicated by [**IVssBackupComponents::AddComponent**](ivssbackupcomponents-addcomponent.md) and in restore operations by [**IVssBackupComponents::SetSelectedForRestore**](ivssbackupcomponents-setselectedforrestore.md).

-   Nonselectable for backup subcomponents without a selectable for backup component ancestor.

    All of these components must be included if any components of the writer are to be included in the operation. The inclusion of these files in backup operations is indicated by [**IVssBackupComponents::AddComponent**](ivssbackupcomponents-addcomponent.md) and in restore operations by [**IVssBackupComponents::SetSelectedForRestore**](ivssbackupcomponents-setselectedforrestore.md).

-   Components implicitly added to the backup ([*subcomponents*](vssgloss-s.md#base-vssgloss-subcomponent)) that are [*selectable for restore*](vssgloss-s.md#base-vssgloss-selectability-for-restore) and are explicitly added to the restore.

    These components may be either selectable or nonselectable, but have a selectable ancestor that was used to implicitly select them for backup. They are added to the Backup Components Document by [**IVssBackupComponents::AddRestoreSubcomponent**](ivssbackupcomponents-addrestoresubcomponent.md).

The identities of components implicitly included in the restore are not stored in the Backup Components Document.

VSS has access to information about component inclusion: writers with no components explicitly included in a restore or backup receive no VSS events following the generation of the [*PrepareForBackup*](vssgloss-p.md#base-vssgloss-prepareforbackup-event) or [*PreRestore*](vssgloss-p.md#base-vssgloss-prerestore-event) events.

Writers cannot directly query this information. This is not a significant limitation because by design, individual VSS writers should not require detailed information about the status of other writers on the system and, as noted above, those with no included components will not have to participate in the VSS operation.

A requester can determine which components have been explicitly included in an operation.

The [**IVssBackupComponents::GetWriterComponentsCount**](ivssbackupcomponents-getwritercomponentscount.md) method returns the number of writers with component information stored in the Backup Components Document (and not the number of components in the document).

The requester indexes through the stored writer information using [**IVssBackupComponents::GetWriterComponents**](ivssbackupcomponents-getwritercomponents.md), which returns instances of the [**IVssWriterComponentsExt**](ivsswritercomponentsext.md) interface. The **IVssWriterComponentsExt** interface allows the requester to obtain the [*writer class*](vssgloss-w.md#base-vssgloss-writer-class) and [*writer instance*](vssgloss-w.md#base-vssgloss-writer-instance) of participating writers, as well as to access information about those of its components stored in the Backup Components Document.

## Information on Included Components

The Backup Components Document's representation of the component data (which does not include path and file specification information), which is accessed through instances of the [**IVssComponent**](ivsscomponent.md) interface.

Requesters and writers obtain access to instances of the [**IVssComponent**](ivsscomponent.md) interface in different ways.

A requester examines component data on a writer by writer basis by using instances of the [**IVssWriterComponentsExt**](ivsswritercomponentsext.md) interface returned by [**IVssBackupComponents::GetWriterComponents**](ivssbackupcomponents-getwritercomponents.md).

In addition to the writer identification information, the [**IVssWriterComponentsExt**](ivsswritercomponentsext.md) interface provides an array of instances of the [**IVssComponent**](ivsscomponent.md) interface—one for each of the selected writers included components.

As noted in [Backup Components Document Life Cycle](backup-components-document-life-cycle.md), the writers can gain access to the same information through the [**IVssWriterComponents**](ivsswritercomponents.md) interface when handling the PrepareForBackup, PrepareForSnapshot, PostSnapshot, BackupComplete, PreRestore, or PostRestore event.

[**IVssComponent**](ivsscomponent.md) allows both writer and requesters to get the following information:

-   A component's name, type, and [*logical path*](vssgloss-l.md#base-vssgloss-logical-path) ([**GetComponentName**](ivsscomponent-getcomponentname.md), [**GetComponentType**](ivsscomponent-getcomponenttype.md), [**GetLogicalPath**](ivsscomponent-getlogicalpath.md))
-   How a component should be restored as indicated by the [*restore target*](vssgloss-r.md#base-vssgloss-restore-target) ([**IVssComponent::GetRestoreTarget**](ivsscomponent-getrestoretarget.md))
-   If an alternate location was used in restoring a file ([**GetAlternateLocationMapping**](ivsscomponent-getalternatelocationmapping.md), [**GetAlternateLocationMappingCount**](ivsscomponent-getalternatelocationmappingcount.md))
-   New target information, if any ([**GetNewTarget**](ivsscomponent-getnewtarget.md), [**GetNewTargetCount**](ivsscomponent-getnewtargetcount.md))
-   Pre-and post-restore error messages ([**GetPreRestoreFailureMsg**](ivsscomponent-getprerestorefailuremsg.md), [**GetPostRestoreFailureMsg**](ivsscomponent-getpostrestorefailuremsg.md))
-   If a [*selectable for backup*](vssgloss-s.md#base-vssgloss-selectability-for-backup) component defining a component set has been selected for restore ([**IsSelectedForRestore**](ivsscomponent-isselectedforrestore.md))
-   Whether a backup or restore succeeded ([**GetBackupSucceeded**](ivsscomponent-getbackupsucceeded.md), [**GetFileRestoreStatus**](ivsscomponent-getfilerestorestatus.md))
-   Any writer-specific backup or restore options that may have been set by [**IVssBackupComponents::SetBackupOptions**](ivssbackupcomponents-setbackupoptions.md) or [**IVssBackupComponents::SetRestoreOptions**](ivssbackupcomponents-setrestoreoptions.md) ([**GetBackupOptions**](ivsscomponent-getbackupoptions.md), [**GetRestoreOptions**](ivsscomponent-getrestoreoptions.md))
-   Any writer-specific metadata backup or restore metadata ([**GetBackupMetadata**](ivsscomponent-getbackupmetadata.md)), [**GetRestoreMetadata**](ivsscomponent-getrestoremetadata.md))
-   Time-stamp information ([**GetBackupStamp**](ivsscomponent-getbackupstamp.md), [**GetPreviousBackupStamp**](ivsscomponent-getpreviousbackupstamp.md))
-   Information about backup subcomponents explicitly included in a restore ([**GetRestoreSubcomponent**](ivsscomponent-getrestoresubcomponent.md), [**GetRestoreSubcomponentCount**](ivsscomponent-getrestoresubcomponentcount.md))

Unlike requesters, writers can change certain information in the Backup Components Document via the [**IVssComponent**](ivsscomponent.md) interface:

-   How a component should be restored as indicated by the restore target ([**IVssComponent::SetRestoreTarget**](ivsscomponent-setrestoretarget.md))
-   Writer-specific backup and restore metadata ([**IVssComponent::SetBackupMetadata**](ivsscomponent-setbackupmetadata.md), [**IVssComponent::SetRestoreMetadata**](ivsscomponent-setrestoremetadata.md))
-   Time-stamp information ([**SetBackupStamp**](ivsscomponent-setbackupstamp.md))
-   Pre- and post-restore error messages ([**SetPreRestoreFailureMsg**](ivsscomponent-setprerestorefailuremsg.md), [**SetPostRestoreFailureMsg**](ivsscomponent-setpostrestorefailuremsg.md))

## Requester State Information

Requesters insert information about the state of a backup or restore operation into the Backup Components Document using the [**IVssBackupComponents**](ivssbackupcomponents.md) interface. Writer applications are able to query for this information through the [**CVssWriter**](cvsswriter.md) class.

State information stored in the Backup Components Document includes the following:

General Information about the Backup

-   The overall backup type (incremental, differential, or full)<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetBackupState**](ivssbackupcomponents-setbackupstate.md)
</dt> <dt>

Retrieved by writers using [**CVssWriter::GetBackupType**](cvsswriter-getbackuptype.md)
</dt> </dl>
-   Whether component operations are supported<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetBackupState**](ivssbackupcomponents-setbackupstate.md)
</dt> <dt>

Retrieved by writers using [**CVssWriter::AreComponentsSelected**](cvsswriter-arecomponentsselected.md)
</dt> </dl>
-   Whether the bootable system state is backed up<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetBackupState**](ivssbackupcomponents-setbackupstate.md)
</dt> <dt>

Retrieved by writers using [**CVssWriter::IsBootableStateBackedUp**](cvsswriter-isbootablestatebackedup.md)
</dt> </dl>
-   Whether partial file operations are supported<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetBackupState**](ivssbackupcomponents-setbackupstate.md)
</dt> <dt>

Retrieved by writers using [**CVssWriter::IsPartialFileSupportEnabled**](cvsswriter-ispartialfilesupportenabled.md)
</dt> </dl>

General Information about the Restore

-   The overall restore type (whether restore is by copy or import)<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetRestoreState**](ivssbackupcomponents-setrestorestate.md)
</dt> <dt>

Retrieved by writers using [**CVssWriter::GetRestoreType**](cvsswriter-getrestoretype.md)
</dt> </dl>

Information about Supporting Files

-   The location of ranges files used by a specific component in partial file operations<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetRangesFilePath**](ivssbackupcomponents-setrangesfilepath.md)
</dt> <dt>

Retrieved by writers (or requesters) using [**IVssComponent::GetPartialFile**](ivsscomponent-getpartialfile.md)
</dt> </dl>

Status of Information

-   Indicate whether one of a given writer's components was successfully backed up<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetBackupSucceeded**](ivssbackupcomponents-setbackupsucceeded.md)
</dt> <dt>

Retrieved by writers and requesters using [**IVssComponent::GetBackupSucceeded**](ivsscomponent-getbackupsucceeded.md)
</dt> </dl>
-   Indicate whether one of a given writer's components was successfully restored<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetFileRestoreStatus**](ivssbackupcomponents-setfilerestorestatus.md)
</dt> <dt>

Retrieved by writers and requester using [**IVssComponent::GetFileRestoreStatus**](ivsscomponent-getfilerestorestatus.md)
</dt> </dl>

Writer-Settable Information

-   Additional backup specification for one of a given writer's components<dl> <dt>

Set by writers using [**IVssComponent::SetBackupMetadata**](ivsscomponent-setbackupmetadata.md)
</dt> <dt>

Retrieved by writers and requesters using [**IVssComponent::GetBackupMetadata**](ivsscomponent-getbackupmetadata.md)
</dt> </dl>
-   Additional restore specification for one of a given writer's components<dl> <dt>

Set by writers using [**IVssComponent::SetRestoreMetadata**](ivsscomponent-setrestoremetadata.md)
</dt> <dt>

Retrieved by writers and requesters using [**IVssComponent::GetRestoreMetadata**](ivsscomponent-getrestoremetadata.md)
</dt> </dl>
-   A backup stamp that indicates, in a writer's own specific format, the time of the current backup of one of its component's backups<dl> <dt>

Set by writers using [**IVssComponent::SetBackupStamp**](ivsscomponent-setbackupstamp.md)
</dt> <dt>

Retrieved by writers and requesters using [**IVssComponent::GetBackupStamp**](ivsscomponent-getbackupstamp.md)
</dt> </dl>
-   A backup stamp that indicates, in a writer's own specific format, the time of the last backup of one of its components' backups using a backup stamp initially set by [**IVssComponent::SetBackupStamp**](ivsscomponent-setbackupstamp.md)<dl> <dt>

Stored and set by requesters for a specific component using [**IVssBackupComponents::SetPreviousBackupStamp**](ivssbackupcomponents-setpreviousbackupstamp.md)
</dt> <dt>

Retrieved by writers and requesters using [**IVssComponent::GetPreviousBackupStamp**](ivsscomponent-getpreviousbackupstamp.md)
</dt> </dl>
-   Error messages for failure before and after restore operations<dl> <dt>

Set by writers using [**IVssComponent::SetPreRestoreFailureMsg**](ivsscomponent-setprerestorefailuremsg.md) or [**IVssComponent::SetPostRestoreFailureMsg**](ivsscomponent-setpostrestorefailuremsg.md)
</dt> <dt>

Retrieved by writers and requesters using [**IVssComponent::GetPreRestoreFailureMsg**](ivsscomponent-getprerestorefailuremsg.md) or [**IVssComponent::GetPostRestoreFailureMsg**](ivsscomponent-getpostrestorefailuremsg.md)
</dt> </dl>

 

 



