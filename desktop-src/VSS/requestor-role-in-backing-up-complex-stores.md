---
description: As with all important operations under VSS, incremental and differential backups require close cooperation between requesters and writers.
ms.assetid: 00391a49-8c81-4518-88a2-741ad5ee4ac3
title: Requester Role in Backing Up Complex Stores
ms.topic: article
ms.date: 05/31/2018
---

# Requester Role in Backing Up Complex Stores

As with all important operations under VSS, [*incremental*](vssgloss-i.md) and [*differential*](vssgloss-d.md) backups require close cooperation between requesters and writers.

## Backup Type

The infrastructure provides special support for five types of backup. They are described as follows:

-   Full (**VSS\_BT\_FULL**). Files will be backed up regardless of their last backup date. The backup history of each file will be updated, and this type of backup can be used as the basis of an incremental or differential backup. If there are log files, they may be truncated as a result of this backup.

    Restoring a full backup requires only a single backup image.

-   Differential (**VSS\_BT\_DIFFERENTIAL**). The VSS API is used to ensure that only files that have been changed or added since the last full backup are to be copied to a storage medium; all intermediate backup information is ignored. This may include entire files, or specific ranges within files. A differential backup is associated with a full backup, and generally cannot be restored until the full backup has been restored. If there are log files, they will usually not be truncated as a result of this backup.

    Restoring a differential backup requires the original backup image and the most recent differential backup image made since the last full backup.

-   Incremental (**VSS\_BT\_INCREMENTAL**). The VSS API is used to ensure that only files that have been changed or added since the last full or incremental backup are to be copied to a storage medium. This may include entire files, or specific ranges within files. Some writers do not allow incremental backups to be mixed with differential backups. If there are log files, they may be truncated as a result of this backup.

    Restoring an incremental backup requires the original backup image and all incremental backup images made since the initial backup.

-   Log Backup (**VSS\_BT\_LOG**). Only a writer's log files (files added to a component with the [**IVssCreateWriterMetadata::AddDataBaseLogFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles) method, and retrieved by a call to [**IVssWMComponent::GetDatabaseLogFile**](/windows/desktop/api/VsBackup/nf-vsbackup-ivsswmcomponent-getdatabaselogfile)) will be backed up. This backup type is specific to VSS. Log backups tend to be taken quite frequently. Typically, the log file will be truncated as a result of this backup.
-   Copy Backup (**VSS\_BT\_COPY**). Like the VSS\_BT\_FULL backup type, files will be backed up regardless of their last backup date. However, the backup history of each file will not be updated, and this sort of backup cannot be used as the basis of an incremental or differential backup. Log files should never be truncated as a result of a copy backup.

<dl> <dt>

<span id="Partial_File_Support"></span><span id="partial_file_support"></span><span id="PARTIAL_FILE_SUPPORT"></span>Partial File Support
</dt> <dd>

Some writers support file restoration through the overwriting of parts of the files they manage. A requester may be designed to take advantage of this, and if so it indicates this by setting the information in [**IVssBackupComponents::SetBackupState**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupstate).

</dd> </dl>

The requester specifies what type of backup is being performed through the *backupType* parameter of [**IVssBackupComponents::SetBackupState**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupstate). Different writers will support different types of backup. After [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata) has been called, the requester can determine what types of backup a given writer supports by calling [**IVssExamineWriterMetadata::GetBackupSchema**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getbackupschema). The returned value is a bit mask indicating support for different backup types. **VSS\_BS\_DIFFERENTIAL** indicates support for differential backups, **VSS\_BS\_INCREMENTAL** for incremental backups, **VSS\_BS\_LOG** for log backups, and **VSS\_BS\_COPY** for copy backups; all writers must support full backups. If a writer does not support mixing incremental backups with differential backups, the **VSS\_BS\_EXCLUSIVE\_INCREMENTAL\_DIFFERENTIAL** flag will be added as well. If the requester is performing an incremental or differential backup and a given writer does not support that backup type, a full backup should be performed on that writer.

## Backup Stamps

Incremental and differential backups are always tied to a previous backup. There are two ways to tie backups. For simple data stores, the requester can keep track of the correlation between backups. However, for more complex data stores, the writer will need to maintain its own timestamp with the backup; this timestamp may keep track of log position, checkpoint information, and so on. The requester can determine whether a given writer needs to store its own timestamp by checking for the **VSS\_BS\_TIMESTAMPED** bit in the value returned by [**IVssExamineWriterMetadata::GetBackupSchema**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getbackupschema).

Writers that store a timestamp in a backup will add the timestamp either while processing [**IVssBackupComponents::PrepareForBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup) or while processing [**IVssBackupComponents::DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset). The requester can obtain this timestamp by calling [**IVssComponent::GetBackupStamp**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getbackupstamp). When performing an incremental or differential backup, the requester needs to tie the current backup to some previous backup. This is done by obtaining the timestamp from the previous backup of a specific component and passing it into the [**IVssBackupComponents::SetPreviousBackupStamp**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setpreviousbackupstamp) function; this needs to be done for each component that was backed up in the previous backup.

## Backing Up Files

### Backing Up Files Reported by Writer

Every file specification that a writer adds to its metadata during the GatherWriterMetadata phase contains a backup type mask that specifies when the file should be backed up. The requester determines what this mask is by calling [**IVssWMFiledesc::GetBackupTypeMask**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getbackuptypemask). The values in this mask are used to determine for which backup types the file specification needs to be backed up. The mask can contain one or more of the following bit values:

<dl> <dt>

<span id="VSS_FSBT_FULL_BACKUP_REQUIRED"></span><span id="vss_fsbt_full_backup_required"></span>**VSS\_FSBT\_FULL\_BACKUP\_REQUIRED**
</dt> <dd>

Required for full backups.

</dd> <dt>

<span id="VSS_FSBT_DIFFERENTIAL_BACKUP_REQUIRED"></span><span id="vss_fsbt_differential_backup_required"></span>**VSS\_FSBT\_DIFFERENTIAL\_BACKUP\_REQUIRED**
</dt> <dd>

Required for differential backups.

</dd> <dt>

<span id="VSS_FSBT_INCREMENTAL_BACKUP_REQUIRED"></span><span id="vss_fsbt_incremental_backup_required"></span>**VSS\_FSBT\_INCREMENTAL\_BACKUP\_REQUIRED**
</dt> <dd>

Required for incremental backups.

</dd> <dt>

<span id="VSS_FSBT_LOG_BACKUP_REQUIRED"></span><span id="vss_fsbt_log_backup_required"></span>**VSS\_FSBT\_LOG\_BACKUP\_REQUIRED**
</dt> <dd>

Required for log backups.

</dd> <dt>

<span id="VSS_FSBT_ALL_BACKUP_REQUIRED"></span><span id="vss_fsbt_all_backup_required"></span>**VSS\_FSBT\_ALL\_BACKUP\_REQUIRED**
</dt> <dd>

Required for all backup types; this is the default.

</dd> </dl>

This specification overrides the component's selectivity specification. For example, consider a component whose files are all marked with **VSS\_FSBT\_LOG\_BACKUP\_REQUIRED** but not with **VSS\_FSBT\_FULL\_BACKUP\_REQUIRED**. Suppose this component is not selectable for backup (*bSelectable* was false when [**IVssCreateWriterMetadata::AddComponent**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addcomponent) was called). In the case of a log backup, this means that all the files in this component must always be backed up. However, in the case of a full backup, none of the files need to be backed up, despite the fact that the component's selectivity implies it should be backed up.

### Backup by Last Modify Time

The file specification information specified in the [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata) phase does not give the requester information about what has changed since the last backup. One way for a writer to indicate changes to the requester is by using the differenced file mechanism. A writer can specify that certain files in a component should be backed up only if they have been modified since a certain time; the writer may specify these files either in [**IVssBackupComponents::PrepareForBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup) or in [**IVssBackupComponents::DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset). A requester can determine these files by calling [**IVssComponent::GetDifferencedFilesCount**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getdifferencedfilescount) and [**IVssComponent::GetDifferencedFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getdifferencedfile). If the file specification matches one set in **IVssBackupComponents::GatherWriterMetadata** (that is currently valid based on the backup type mask) the differenced file information overrides the previous information; that is, the files matching that file specification are now backed up only if they have been modified since the specified time. The last-modify time is communicated using a [**FILETIME**](/windows/win32/api/minwinbase/ns-minwinbase-filetime) structure. If the value of this structure is zero, this implies that the last-modify time should be determined based on the requester's record of the time of last backup.

### Partial File Backup

Another way for a writer to indicate changes to the requester is by using the partial file mechanism. A writer can specify byte ranges within component files that need to be backed up; the writer can specify these file ranges either in [**IVssBackupComponents::PrepareForBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup) or in [**IVssBackupComponents::DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset). A requester can determine these files by calling [**IVssComponent::GetPartialFileCount**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getpartialfilecount) and [**IVssComponent::GetPartialFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getpartialfile). **IVssComponent::GetPartialFile** will return a path and a file name pointing to the file, and a ranges string indicating what needs to be backed up in the file. As with differenced files, if the path and file name matches a file specification set by the writer in [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata), the partial-file information overrides the previous setting. The ranges string can have two formats: it can either specify the ranges directly, or it can specify a file containing ranges information. If specifying ranges directly, the syntax is a comma-separated list of the form offset1:length1, offset2:length2, where each offset and length is a 64-bit unsigned integer. If specifying a ranges file, the ranges string should be set to File= *filename*, where *filename* is the full path to the ranges file. The ranges file itself is a binary file that is formatted as a list of 64-bit unsigned integers. The first integer indicates how many ranges are represented in the file. Each subsequent pair of integers represents the offset and length of a range. The requester must take care to back up and restore this ranges file as well.

### File Specification Rules

File specifications added through the differenced-file and the partial-file mechanisms will either modify file specifications set in [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata) or add completely new files. If modifying files specifications set in **IVssBackupComponents::GatherWriterMetadata** using the partial-file mechanism, then a requester can expect the file specification to exactly match one of the file specifications set in the component in **IVssBackupComponents::GatherWriterMetadata**. The file specification will not partially overlap another file specification, and it will not match any file specifications in any other of that writer's components. File specifications added using the partial-file mechanism can, however, partially overlap another file specification. When this is true, the differenced-file or partial-file specification overrides the specification set in **IVssBackupComponents::GatherWriterMetadata**. General file specifications can have an alternate-location value (returned by [**IVssWMFiledesc::GetAlternateLocation**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getalternatelocation)) that indicates an alternate place to obtain the file from at backup time. If the file specifications set through the differenced-file or partial file mechanisms match an existing files specification that has an alternate location, the data should be picked up from this alternate location. If the file specifications set through the differenced-file or partial-file mechanisms do not match any existing specifications for the component, then these file ranges should now be added to the backup. The requester can expect that only files on volumes that have already been included in the shadow copy set will be added using one of these mechanisms.

### Backup without a Shadow Copy

Certain types of files may not need to be backed up off of a shadow copy volume. For example, this will often be true of database log files. Since log files grow monotonically, and a writer can specify exactly what portions of the file to back up using partial files, it will often be possible to backup the log off the original volume. As an optimization, a writer can mark which files require shadow copies for different backup types using the backup-type mask. The value returned from [**IVssWMFiledesc::GetBackupTypeMask**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getbackuptypemask) can contain one or more of the following bit values:

<dl> <dt>

<span id="VSS_FSBT_FULL_SNAPSHOT_REQUIRED"></span><span id="vss_fsbt_full_snapshot_required"></span>**VSS\_FSBT\_FULL\_SNAPSHOT\_REQUIRED**
</dt> <dd>

Shadow copy required for full backups.

</dd> <dt>

<span id="VSS_FSBT_DIFFERENTIAL_SNAPSHOT_REQUIRED"></span><span id="vss_fsbt_differential_snapshot_required"></span>**VSS\_FSBT\_DIFFERENTIAL\_SNAPSHOT\_REQUIRED**
</dt> <dd>

Shadow copy required for differential backups.

</dd> <dt>

<span id="VSS_FSBT_INCREMENTAL_SNAPSHOT_REQUIRED"></span><span id="vss_fsbt_incremental_snapshot_required"></span>**VSS\_FSBT\_INCREMENTAL\_SNAPSHOT\_REQUIRED**
</dt> <dd>

Shadow copy required for incremental backups.

</dd> <dt>

<span id="VSS_FSBT_LOG_SNAPSHOT_REQUIRED"></span><span id="vss_fsbt_log_snapshot_required"></span>**VSS\_FSBT\_LOG\_SNAPSHOT\_REQUIRED**
</dt> <dd>

Shadow copy required for log backups.

</dd> <dt>

<span id="VSS_FSBT_ALL_SNAPSHOT_REQUIRED"></span><span id="vss_fsbt_all_snapshot_required"></span>**VSS\_FSBT\_ALL\_SNAPSHOT\_REQUIRED**
</dt> <dd>

Shadow copy required for all backup types; this is the default.

</dd> </dl>

If a specific volume contains only components that do not require a shadow copy for this backup, the requester can skip the step of creating a shadow copy for this volume. All the data on this volume can be copied to the backup media directly from the original volume.

## Restoring Files

### Sequential Restores

After the requester is done performing a restore operation, it sends the PostRestore event to all writers. Generally, writers handle this event by performing recovery or other post-restore operations. Restoration of incremental backups, however, usually happen as a sequence of restore operations, one per incremental backup. The requester needs to inform the writer that such a restoration is in progress in order to prevent recovery or other undesirable operations from happening until the restore is completely done. This is done by calling [**IVssBackupComponents::SetAdditionalRestores**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setadditionalrestores). This method is called per component, and indicates to the writer that more restores are coming for that component. For the final restore in the sequence, the additional-restores flag should be set to false (its default value), which indicates that this is the last restore in the sequence for that component.

### New Targets

If supported by the writer, the requester can restore data files to a location other than the original backup-time location. The requester can check for this support by calling [**IVssExamineWriterMetadata::GetBackupSchema**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getbackupschema). The **VSS\_BS\_WRITER\_SUPPORTS\_NEW\_TARGET** bit will be set if the writer supports this behavior. The requester informs the writer of the new location by calling [**IVssBackupComponents::AddNewTarget**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addnewtarget) for each relocated file specification. The requester can also decide to restore a specific ranges file to a different location. The requester informs the writer of this change by calling [**IVssBackupComponents::SetRangesFilePath**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setrangesfilepath).

### Directed Targets

For complicated restore scenarios, a writer may want to map ranges of a backed-up file onto different ranges of the same or a different file. This can be done by using the directed target mechanism. The requester can determine after the [**IVssBackupComponents::PreRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prerestore) phase that this mechanism is being used for a component by calling [**IVssComponent::GetRestoreTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getrestoretarget) and checking for a return of **VSS\_RT\_DIRECTED**. The requester can than obtain all of these redirected restores by calling [**IVssComponent::GetDirectedTargetCount**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getdirectedtargetcount) and [**IVssComponent::GetDirectedTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getdirectedtarget). **IVssComponent::GetDirectedTarget** will return a full path to a source file on the backup and a full path to a destination file that will be restored to. It also returns a ranges list for each of these files. The requester is then responsible for restoring the specified ranges in the source file to the mapped ranges in the destination file. The format of the ranges string is the same as in [**IVssComponent::GetPartialFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getpartialfile).

-   [Writer Role in VSS Incremental and Differential Backups](writer-role-in-vss-incremental-and-differential-backups.md)
-   [Requester Role in VSS Incremental and Differential Backups](requestor-role-in-vss-incremental-and-differential-backups.md)

 

 
