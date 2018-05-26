---
Description: The Backup Components Document is maintained by instances of the IVssBackupComponents interface.
ms.assetid: 8c7ebba8-58c4-4733-ba59-802abf902c5e
title: Backup Components Document Contents
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Backup Components Document Contents

The Backup Components Document is maintained by instances of the [**IVssBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) interface. This interface also contains numerous methods for controlling backup operations, manipulating shadow copies, and querying the system state. However, not all of the document's information is directly accessible through this interface.

The Backup Components Document consists of several sets of data:

-   Information about which components were explicitly included in a backup or restore operation
-   A representation of the stored component and writer information
-   State information about the backup/recover operation

While the component information is available to both the requester and the writer, only the writer has access to the state information.

## Component Inclusion Information

The Backup Components Document contains a list of those components explicitly included in backup and restore by the requester. The list contains the following:

-   Explicitly included [*selectable components*](vssgloss-s.md#base-vssgloss-selectable-component).

    The inclusion of these files in backup operations is indicated by [**IVssBackupComponents::AddComponent**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent?branch=master) and in restore operations by [**IVssBackupComponents::SetSelectedForRestore**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setselectedforrestore?branch=master).

-   Nonselectable for backup subcomponents without a selectable for backup component ancestor.

    All of these components must be included if any components of the writer are to be included in the operation. The inclusion of these files in backup operations is indicated by [**IVssBackupComponents::AddComponent**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent?branch=master) and in restore operations by [**IVssBackupComponents::SetSelectedForRestore**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setselectedforrestore?branch=master).

-   Components implicitly added to the backup ([*subcomponents*](vssgloss-s.md#base-vssgloss-subcomponent)) that are [*selectable for restore*](vssgloss-s.md#base-vssgloss-selectability-for-restore) and are explicitly added to the restore.

    These components may be either selectable or nonselectable, but have a selectable ancestor that was used to implicitly select them for backup. They are added to the Backup Components Document by [**IVssBackupComponents::AddRestoreSubcomponent**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addrestoresubcomponent?branch=master).

The identities of components implicitly included in the restore are not stored in the Backup Components Document.

VSS has access to information about component inclusion: writers with no components explicitly included in a restore or backup receive no VSS events following the generation of the [*PrepareForBackup*](vssgloss-p.md#base-vssgloss-prepareforbackup-event) or [*PreRestore*](vssgloss-p.md#base-vssgloss-prerestore-event) events.

Writers cannot directly query this information. This is not a significant limitation because by design, individual VSS writers should not require detailed information about the status of other writers on the system and, as noted above, those with no included components will not have to participate in the VSS operation.

A requester can determine which components have been explicitly included in an operation.

The [**IVssBackupComponents::GetWriterComponentsCount**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritercomponentscount?branch=master) method returns the number of writers with component information stored in the Backup Components Document (and not the number of components in the document).

The requester indexes through the stored writer information using [**IVssBackupComponents::GetWriterComponents**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritercomponents?branch=master), which returns instances of the [**IVssWriterComponentsExt**](/windows/win32/VsBackup/?branch=master) interface. The **IVssWriterComponentsExt** interface allows the requester to obtain the [*writer class*](vssgloss-w.md#base-vssgloss-writer-class) and [*writer instance*](vssgloss-w.md#base-vssgloss-writer-instance) of participating writers, as well as to access information about those of its components stored in the Backup Components Document.

## Information on Included Components

The Backup Components Document's representation of the component data (which does not include path and file specification information), which is accessed through instances of the [**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master) interface.

Requesters and writers obtain access to instances of the [**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master) interface in different ways.

A requester examines component data on a writer by writer basis by using instances of the [**IVssWriterComponentsExt**](/windows/win32/VsBackup/?branch=master) interface returned by [**IVssBackupComponents::GetWriterComponents**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritercomponents?branch=master).

In addition to the writer identification information, the [**IVssWriterComponentsExt**](/windows/win32/VsBackup/?branch=master) interface provides an array of instances of the [**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master) interface—one for each of the selected writers included components.

As noted in [Backup Components Document Life Cycle](backup-components-document-life-cycle.md), the writers can gain access to the same information through the [**IVssWriterComponents**](/windows/win32/VsWriter/nl-vswriter-ivsswritercomponents?branch=master) interface when handling the PrepareForBackup, PrepareForSnapshot, PostSnapshot, BackupComplete, PreRestore, or PostRestore event.

[**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master) allows both writer and requesters to get the following information:

-   A component's name, type, and [*logical path*](vssgloss-l.md#base-vssgloss-logical-path) ([**GetComponentName**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getcomponentname?branch=master), [**GetComponentType**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getcomponenttype?branch=master), [**GetLogicalPath**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getlogicalpath?branch=master))
-   How a component should be restored as indicated by the [*restore target*](vssgloss-r.md#base-vssgloss-restore-target) ([**IVssComponent::GetRestoreTarget**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getrestoretarget?branch=master))
-   If an alternate location was used in restoring a file ([**GetAlternateLocationMapping**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getalternatelocationmapping?branch=master), [**GetAlternateLocationMappingCount**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getalternatelocationmappingcount?branch=master))
-   New target information, if any ([**GetNewTarget**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getnewtarget?branch=master), [**GetNewTargetCount**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getnewtargetcount?branch=master))
-   Pre-and post-restore error messages ([**GetPreRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getprerestorefailuremsg?branch=master), [**GetPostRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getpostrestorefailuremsg?branch=master))
-   If a [*selectable for backup*](vssgloss-s.md#base-vssgloss-selectability-for-backup) component defining a component set has been selected for restore ([**IsSelectedForRestore**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-isselectedforrestore?branch=master))
-   Whether a backup or restore succeeded ([**GetBackupSucceeded**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getbackupsucceeded?branch=master), [**GetFileRestoreStatus**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getfilerestorestatus?branch=master))
-   Any writer-specific backup or restore options that may have been set by [**IVssBackupComponents::SetBackupOptions**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupoptions?branch=master) or [**IVssBackupComponents::SetRestoreOptions**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setrestoreoptions?branch=master) ([**GetBackupOptions**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getbackupoptions?branch=master), [**GetRestoreOptions**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getrestoreoptions?branch=master))
-   Any writer-specific metadata backup or restore metadata ([**GetBackupMetadata**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getbackupmetadata?branch=master)), [**GetRestoreMetadata**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getrestoremetadata?branch=master))
-   Time-stamp information ([**GetBackupStamp**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getbackupstamp?branch=master), [**GetPreviousBackupStamp**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getpreviousbackupstamp?branch=master))
-   Information about backup subcomponents explicitly included in a restore ([**GetRestoreSubcomponent**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getrestoresubcomponent?branch=master), [**GetRestoreSubcomponentCount**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getrestoresubcomponentcount?branch=master))

Unlike requesters, writers can change certain information in the Backup Components Document via the [**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master) interface:

-   How a component should be restored as indicated by the restore target ([**IVssComponent::SetRestoreTarget**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setrestoretarget?branch=master))
-   Writer-specific backup and restore metadata ([**IVssComponent::SetBackupMetadata**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setbackupmetadata?branch=master), [**IVssComponent::SetRestoreMetadata**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setrestoremetadata?branch=master))
-   Time-stamp information ([**SetBackupStamp**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setbackupstamp?branch=master))
-   Pre- and post-restore error messages ([**SetPreRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setprerestorefailuremsg?branch=master), [**SetPostRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setpostrestorefailuremsg?branch=master))

## Requester State Information

Requesters insert information about the state of a backup or restore operation into the Backup Components Document using the [**IVssBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) interface. Writer applications are able to query for this information through the [**CVssWriter**](/windows/win32/VsWriter/nl-vswriter-cvsswriter?branch=master) class.

State information stored in the Backup Components Document includes the following:

General Information about the Backup

-   The overall backup type (incremental, differential, or full)<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetBackupState**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupstate?branch=master)
</dt> <dt>

Retrieved by writers using [**CVssWriter::GetBackupType**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-getbackuptype?branch=master)
</dt> </dl>
-   Whether component operations are supported<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetBackupState**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupstate?branch=master)
</dt> <dt>

Retrieved by writers using [**CVssWriter::AreComponentsSelected**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-arecomponentsselected?branch=master)
</dt> </dl>
-   Whether the bootable system state is backed up<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetBackupState**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupstate?branch=master)
</dt> <dt>

Retrieved by writers using [**CVssWriter::IsBootableStateBackedUp**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-isbootablesystemstatebackedup?branch=master)
</dt> </dl>
-   Whether partial file operations are supported<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetBackupState**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupstate?branch=master)
</dt> <dt>

Retrieved by writers using [**CVssWriter::IsPartialFileSupportEnabled**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-ispartialfilesupportenabled?branch=master)
</dt> </dl>

General Information about the Restore

-   The overall restore type (whether restore is by copy or import)<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetRestoreState**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setrestorestate?branch=master)
</dt> <dt>

Retrieved by writers using [**CVssWriter::GetRestoreType**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-getrestoretype?branch=master)
</dt> </dl>

Information about Supporting Files

-   The location of ranges files used by a specific component in partial file operations<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetRangesFilePath**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setrangesfilepath?branch=master)
</dt> <dt>

Retrieved by writers (or requesters) using [**IVssComponent::GetPartialFile**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getpartialfile?branch=master)
</dt> </dl>

Status of Information

-   Indicate whether one of a given writer's components was successfully backed up<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetBackupSucceeded**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupsucceeded?branch=master)
</dt> <dt>

Retrieved by writers and requesters using [**IVssComponent::GetBackupSucceeded**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getbackupsucceeded?branch=master)
</dt> </dl>
-   Indicate whether one of a given writer's components was successfully restored<dl> <dt>

Set by requesters using [**IVssBackupComponents::SetFileRestoreStatus**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setfilerestorestatus?branch=master)
</dt> <dt>

Retrieved by writers and requester using [**IVssComponent::GetFileRestoreStatus**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getfilerestorestatus?branch=master)
</dt> </dl>

Writer-Settable Information

-   Additional backup specification for one of a given writer's components<dl> <dt>

Set by writers using [**IVssComponent::SetBackupMetadata**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setbackupmetadata?branch=master)
</dt> <dt>

Retrieved by writers and requesters using [**IVssComponent::GetBackupMetadata**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getbackupmetadata?branch=master)
</dt> </dl>
-   Additional restore specification for one of a given writer's components<dl> <dt>

Set by writers using [**IVssComponent::SetRestoreMetadata**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setrestoremetadata?branch=master)
</dt> <dt>

Retrieved by writers and requesters using [**IVssComponent::GetRestoreMetadata**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getrestoremetadata?branch=master)
</dt> </dl>
-   A backup stamp that indicates, in a writer's own specific format, the time of the current backup of one of its component's backups<dl> <dt>

Set by writers using [**IVssComponent::SetBackupStamp**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setbackupstamp?branch=master)
</dt> <dt>

Retrieved by writers and requesters using [**IVssComponent::GetBackupStamp**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getbackupstamp?branch=master)
</dt> </dl>
-   A backup stamp that indicates, in a writer's own specific format, the time of the last backup of one of its components' backups using a backup stamp initially set by [**IVssComponent::SetBackupStamp**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setbackupstamp?branch=master)<dl> <dt>

Stored and set by requesters for a specific component using [**IVssBackupComponents::SetPreviousBackupStamp**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setpreviousbackupstamp?branch=master)
</dt> <dt>

Retrieved by writers and requesters using [**IVssComponent::GetPreviousBackupStamp**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getpreviousbackupstamp?branch=master)
</dt> </dl>
-   Error messages for failure before and after restore operations<dl> <dt>

Set by writers using [**IVssComponent::SetPreRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setprerestorefailuremsg?branch=master) or [**IVssComponent::SetPostRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setpostrestorefailuremsg?branch=master)
</dt> <dt>

Retrieved by writers and requesters using [**IVssComponent::GetPreRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getprerestorefailuremsg?branch=master) or [**IVssComponent::GetPostRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getpostrestorefailuremsg?branch=master)
</dt> </dl>

 

 



