---
description: As with all important operations under VSS, incremental and differential backups require close cooperation between requesters and writers.
ms.assetid: 3cf5dd1f-dc58-42bc-925f-fee7d34053c5
title: Writer Role in Backing Up Complex Stores
ms.topic: article
ms.date: 05/31/2018
---

# Writer Role in Backing Up Complex Stores

As with all important operations under VSS, [*incremental*](vssgloss-i.md) and [*differential*](vssgloss-d.md) backups require close cooperation between requesters and writers.

## Backup Types

The infrastructure provides special support for five types of backup. They are described as follows:

-   Full (**VSS\_BT\_FULL**). Files will be backed up regardless of their last backup date. The backup history of each file will be updated, and this type of backup can be used as the basis of an incremental or differential backup. If there are log files, they may be truncated as a result of this backup.

    Restoring a full backup requires only a single backup image.

-   Differential (**VSS\_BT\_DIFFERENTIAL**). The VSS API is used to ensure that only files that have been changed or added since the last full backup are to be copied to a storage medium; all intermediate backup information is ignored. This may include entire files, or specific ranges within files. A differential backup is associated with a full backup, and generally cannot be restored until the full backup has been restored. If there are log files, they will usually not be truncated as a result of this backup.

    Restoring a differential backup requires the original backup image and the most recent differential backup image made since the last full backup.

-   Incremental (**VSS\_BT\_INCREMENTAL**). The VSS API is used to ensure that only files that have been changed or added since the last full or incremental backup are to be copied to a storage medium. This may include entire files, or specific ranges within files. Some writers do not allow incremental backups to be mixed with differential backups. If there are log files, they may be truncated as a result of this backup.

    Restoring an incremental backup requires the original backup image and all incremental backup images made since the initial backup.

-   Log Backup (**VSS\_BT\_LOG**). Only a writer's log files (files added to a component with the [**IVssCreateWriterMetadata::AddDataBaseLogFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles) method, and retrieved by a call to [**IVssWMComponent::GetDatabaseLogFile**](/windows/desktop/api/VsBackup/nf-vsbackup-ivsswmcomponent-getdatabaselogfile)) will be backed up. This backup type is specific to VSS. Log backups tend to be taken quite frequently. Typically, the log file will be truncated as a result of this backup.
-   Copy Backup (**VSS\_BT\_COPY**). Like the VSS\_BT\_FULL backup type, files will be backed up regardless of their last backup date. However, the backup history of each file will not be updated, and this type of backup cannot be used as the basis of an incremental or differential backup. Log files should never be truncated as a result of a copy backup.

<dl> <dt>

<span id="Partial_File_Support"></span><span id="partial_file_support"></span><span id="PARTIAL_FILE_SUPPORT"></span>Partial File Support
</dt> <dd>

Some writers support file restoration through the overwriting of parts of the files they manage. A requester may be designed to take advantage of this, and if so it indicates this by setting the information in [**IVssBackupComponents::SetBackupState**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupstate).

</dd> </dl>

The writers indicate what type of backups are supported by calling [**IVssCreateWriterMetadata::SetBackupSchema**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-setbackupschema) while processing the [*Identify*](vssgloss-i.md) event. The *dsSchemaMask* parameter to the **IVssCreateWriterMetadata::SetBackupSchema** method is a bit mask indicating what types of backup are supported. All writers must support full backups.

<dl> <dt>

<span id="VSS_BS_DIFFERENTIAL"></span><span id="vss_bs_differential"></span>**VSS\_BS\_DIFFERENTIAL**
</dt> <dd>

Indicates support for differential backups.

</dd> <dt>

<span id="VSS_BS_INCREMENTAL"></span><span id="vss_bs_incremental"></span>**VSS\_BS\_INCREMENTAL**
</dt> <dd>

Indicates support for incremental backups.

</dd> <dt>

<span id="VSS_BS_LOG"></span><span id="vss_bs_log"></span>**VSS\_BS\_LOG**
</dt> <dd>

Indicates support for log backups.

</dd> <dt>

<span id="VSS_BS_COPY"></span><span id="vss_bs_copy"></span>**VSS\_BS\_COPY**
</dt> <dd>

Indicates support for copy backups.

</dd> <dt>

<span id="VSS_BS_EXCLUSIVE_INCREMENTAL_DIFFERENTIAL"></span><span id="vss_bs_exclusive_incremental_differential"></span>**VSS\_BS\_EXCLUSIVE\_INCREMENTAL\_DIFFERENTIAL**
</dt> <dd>

Indicates that a writer does not support mixing incremental backups with differential backups.

</dd> </dl>

The writer can determine what type of backup is being performed by calling [**CVssWriter::GetBackupType**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-getbackuptype). The earliest point when this can be performed is while processing the PrepareForBackup event. **CVssWriter::GetBackupType** will return a member of the [**VSS\_BACKUP\_TYPE**](/windows/desktop/api/Vss/ne-vss-vss_backup_type) enumeration. If the backup type is not supported by the writer, then the writer should treat the backup as a full backup.

## Backup Stamps

Incremental and differential backups are always tied to a previous backup. There are two ways to tie backups. For simple data stores, the requester can keep track of the correlation between backups. However, for more complex data stores, the writer will need to maintain its own timestamp with the backup; this timestamp may keep track of log position, checkpoint information, and so on. A writer indicates that it needs its own timestamps by setting the **VSS\_BS\_TIMESTAMPED** bit when it calls [**IVssCreateWriterMetadata::SetBackupSchema**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-setbackupschema).

A writer can store a timestamp with each component that is being backed up. The writer stores the timestamp by calling [**IVssComponent::SetBackupStamp**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setbackupstamp), and passing in a string representation of the stamp for the *wszBackupStamp* parameter. Generally, a writer will call this method while processing the [*PostSnapshot*](vssgloss-p.md) event. However, for backups that do not involve a shadow copy, the PostSnapshot event will not be sent. In this case, **IVssComponent::SetBackupStamp** must be called while processing the [*PrepareForBackup*](vssgloss-p.md) event.

When an incremental or differential backup is being performed, the requester will indicate to the writer the backup stamp of the previous backup that is serving as a base for this backup. The writer can access this previous backup stamp while processing either the PrepareForBackup or PostSnapshot event, by calling [**IVssComponent::GetPreviousBackupStamp**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getpreviousbackupstamp). The writer can use the returned stamp to determine what needs to be backed up.

## Backup Strategies

### File Backup Files Strategies

Often, certain files reported in the writer metadata need only be backed up when performing certain types of backup. Some files may only be required when performing a full backup. Other files may only be required when performing an incremental or differential backup. VSS provides a method for the writers to indicate this information to the requester. When adding files to components using [**IVssCreateWriterMetadata::AddDatabaseFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabasefiles), [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles), or [**IVssCreateWriterMetadata::AddFilesToFileGroup**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addfilestofilegroup), the *dwBackupTypeMask* parameter indicates for which backup types these files must be backed up. The mask can contain one or more of the following values:

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

### Backup By Last Modify Time

One way for a writer to indicate what files have changed is by using the differenced file mechanism. A writer can specify that certain files in a component should only be backed up if they have been modified since a certain time. The writer calls [**IVssComponent::AddDifferencedFilesByLastModifyTime**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-adddifferencedfilesbylastmodifytime) with a file specification and a last modify time. **IVssComponent::AddDifferencedFilesByLastModifyTime** is typically called while processing the PostSnapshot event, although it can be called while processing the PrepareForBackup event. The requester must then back up all files matching the file specification that have changed since the specified time. If the writer is using the backup stamp mechanism, this last modify time will be determined based on the previous backup stamp in the backup document. The writer can also pass in zero for the last modify time, which indicates that the requester is responsible for determining the time of the last backup and the files changed since that time.

### Partial File Backup

Another way for a writer to indicate changes to the requester is by using the partial-file mechanism. A writer can specify byte ranges within component files that need to be backed up; the writer may specify these file ranges while processing either the PostSnapshot or PrepareForBackup event. The writer calls [**IVssComponent::AddPartialFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-addpartialfile) to add partial file specifications to the backup. A partial file specification consists of a path and file name together with information about what ranges in the file need to be backed up.

### File Specification Rules

[**IVssComponent::AddDifferencedFilesByLastModifyTime**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-adddifferencedfilesbylastmodifytime) or [**IVssComponent::AddPartialFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-addpartialfile) can both be used to modify file specifications given during the Identify event, or to add completely new files to the specification. If the writer is modifying information set during the Identify event using **IVssComponent::AddDifferencedFilesByLastModifyTime**, then the file specification must exactly match one of the file specifications in the current component. The file specification must not partially overlap files in the current component, and it must not match files in any other components. Files specified using **IVssComponent::AddPartialFile** can, however, partially overlap another file specification. Information set by **IVssComponent::AddDifferencedFilesByLastModifyTime** or **IVssComponent::AddPartialFile** overrides the information set earlier using the [**IVssCreateWriterMetadata**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscreatewritermetadata) interface in response to the Identify event.

General file specifications can have an alternate-location value (set by the *wszAlternateLocation* parameter of [**IVssCreateWriterMetadata::AddFilesToFileGroup**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addfilestofilegroup)) that indicates an alternate location to obtain the file from at backup time. If the file specification set through the differenced-file or partial-file mechanisms matches an existing file specification that has an alternate location, the backup application will obtain the data from this alternate location.

If the file specification set in [**IVssComponent::AddDifferencedFilesByLastModifyTime**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-adddifferencedfilesbylastmodifytime) or in [**IVssComponent::AddPartialFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-addpartialfile) does not match and files in the component that are being backed up, then all matching files are now added to the backup. Care must be taken that the writer only adds files that exist on a volume that is already being shadow copied while doing this; otherwise, the requester may fail to back up these files. If these functions are called while processing the PostSnapshot event, this can be determined by using the [**CVssWriter::IsPathAffected**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-ispathaffected) method. If called while handling the PrepareForBackup event, the writer must make this determination using another method.

### Backup Without a Shadow Copy

Certain types of files may not need to be backed up off of a shadow copy volume. For example, this will often be true of database log files. Since log files grow monotonically, and a writer can specify exactly what portions of the file to back up using partial files, it will often be possible to back up the log off the original volume. As an optimization, a writer can mark which files require shadow copies for different backup types using the flags set in the *dwBackupTypeMask* parameter of [**IVssCreateWriterMetadata::AddDatabaseFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabasefiles), [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles), or [**IVssCreateWriterMetadata::AddFilesToFileGroup**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addfilestofilegroup). Supported flags include the following:

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

## Backup Cleanup

If the writer needs to perform log truncation or other post-backup cleanup, the proper place to do this is while processing the [*BackupComplete*](vssgloss-b.md) event. The [*BackupShutdown*](vssgloss-b.md) event will be sent some time after BackupComplete, so some cleanup may also be done in the BackupShutdown event handler.

The BackupShutdown event is always sent after termination of a backup. If the requester terminates abnormally while performing a backup, BackupShutdown will be sent immediately, without first sending BackupComplete. If the writer needs to clean up any state, that may be done here; however, log truncation should not happen in this event because the backup did not necessarily complete.

## Restore Strategies

The basic tasks of writers at restore are to verify that the restore can happen in handling the PreRestore event, and that the restore has happened in handling the PostRestore event. More complex stores will also perform a recovery process in the PostRestore handler. If the restore is part of an incremental or differential restore, the writer will generally want to delay this recovery process until all incremental or differential restores have been completed. [**IVssComponent::GetAdditionalRestores**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getadditionalrestores) will indicate whether this is the final restore of this component, or whether there are more restores to come. If **IVssComponent::GetAdditionalRestores** returns **true**, the writer should not perform its recovery procedure on that component.

## New Targets

If supported by the writer, the requester can restore data files to a location other than the original backup-time location. A writer indicates support for this restore mode by setting the **VSS\_BS\_WRITER\_SUPPORTS\_NEW\_TARGET** bit in the *dsSchemaMask* parameter when calling [**IVssCreateWriterMetadata::SetBackupSchema**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-setbackupschema). A writer obtains the new locations for component files at restore time by calling [**IVssComponent::GetNewTargetCount**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getnewtargetcount) and [**IVssComponent::GetNewTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getnewtarget).

## Directed Targets

For complicated restore scenarios, a writer may want to map ranges of a backed-up file onto different ranges of the same or a different file. This can be done by using the directed-target mechanism. To do this, a writer must first indicate this is happening by calling [**IVssComponent::SetRestoreTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setrestoretarget), passing in **VSS\_RT\_DIRECTED** for the *target* parameter. Then, for each mapping, the writer calls [**IVssComponent::AddDirectedTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-adddirectedtarget). This method takes a full path to a source file on the backup and a full path to a destination file that will be restored to. It also takes a ranges list for each of these files. The writer calls these functions while handling the PreRestore event, and the requester is then responsible for restoring the specified ranges in the source file to the mapped ranges in the destination file. The format of the ranges string is the same as in [**IVssComponent::AddPartialFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-addpartialfile)

## Private Writer Metadata

It is often useful for a writer to maintain private metadata with a backup to properly perform an incremental or differential restore. A writer may call [**IVssComponent::SetBackupMetadata**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setbackupmetadata) while handling either PrepareForBackup or PostSnapshot to store metadata. This metadata can be accessed by the writer during either PreRestore or PostRestore by calling [**IVssComponent::GetBackupMetadata**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getbackupmetadata). Metadata can also be stored with partial file specification by using the *wszMetadata* parameter of [**IVssComponent::AddPartialFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-addpartialfile); this metadata is accessed through the *pbstrMetadata*parameter of [**IVssComponent::GetPartialFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getpartialfile). The writer can also pass metadata to itself between [**CVssWriter::OnPreRestore**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onprerestore) and [**CVssWriter::OnPostRestore**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onpostrestore). In **CVssWriter::OnPreRestore**, the metadata is set by calling [**IVssComponent::SetRestoreMetadata**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setrestoremetadata). In **CVssWriter::OnPostRestore**, the metadata is retrieved by calling [**IVssComponent::GetRestoreMetadata**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getrestoremetadata).

-   [Writer Role in VSS Incremental and Differential Backups](writer-role-in-vss-incremental-and-differential-backups.md)
-   [Requester Role in VSS Incremental and Differential Backups](requestor-role-in-vss-incremental-and-differential-backups.md)

 

 



