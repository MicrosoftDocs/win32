---
Description: 'To support an incremental or differential backup operation, a requester must do the following:'
ms.assetid: 'a77700e3-8217-460e-bec9-1041d03eec41'
title: Requester Role in VSS Incremental and Differential Backups
---

# Requester Role in VSS Incremental and Differential Backups

To support an [*incremental*](vssgloss-i.md#base-vssgloss-incremental-backup-operations) or [*differential*](vssgloss-d.md#base-vssgloss-differential-backup-operations) backup operation, a requester must do the following:

1.  Determine what degree of writer support is available (using [**IVssBackupComponents::GetWriterMetadata**](ivssbackupcomponents-getwritermetadata.md) to get access to information in Writer Metadata Documents)—in particular, determine which backup schema are supported ([**VSS\_BACKUP\_SCHEMA**](vss-backup-schema.md)).
2.  Set an appropriate backup state.
3.  Obtain file and file set level specifications for an incremental or differential backup.
4.  Perform the backup.

## Requester Determination of Incremental and Differential Support and Configuration

A requester needs to obtain information about writer support prior to selecting components for inclusion in an incremental or differential backup or setting its own state.

<dl> <dt>

<span id="Determining_Writer_Support"></span><span id="determining_writer_support"></span><span id="DETERMINING_WRITER_SUPPORT"></span>Determining Writer Support
</dt> <dd>

A requester determines if a given writer supports VSS incremental or differential backups by retrieving the writer's backup schema mask using the [**IVssExamineWriterMetadata::GetBackupSchema**](ivssexaminewritermetadata-getbackupschema.md) method.

The backup schema mask of a writer supporting VSS incremental or differential techniques will contain either **VSS\_BS\_INCREMENTAL** or **VSS\_BS\_DIFFERENTIAL**, or both. Writers may also indicate restrictions on their participation with the **VSS\_BS\_EXCLUSIVE\_INCREMENTAL\_DIFFERENTIAL** flag. (See [**VSS\_BACKUP\_SCHEMA**](vss-backup-schema.md) for more information on backup schemas).

</dd> <dt>

<span id="Setting_Requester_Backup_State"></span><span id="setting_requester_backup_state"></span><span id="SETTING_REQUESTER_BACKUP_STATE"></span>Setting Requester Backup State
</dt> <dd>

A requester indicates that a backup is an incremental or differential backup by setting a backup type to either **VSS\_BT\_INCREMENTAL** or **VSS\_BT\_DIFFERENTIAL** using the [**IVssBackupComponents::SetBackupState**](ivssbackupcomponents-setbackupstate.md) method prior to generating a [**PrepareForBackup**](ivssbackupcomponents-prepareforbackup.md) event.

The [**IVssBackupComponents::SetBackupState**](ivssbackupcomponents-setbackupstate.md) method is also used to indicate whether the requester provides [*partial file support*](vssgloss-p.md#base-vssgloss-partial-file-support), which is frequently used to implement certain incremental backup and restore operations.

</dd> </dl>

## Getting Writer Specifications for Incremental and Differential Backups

The file-set-level file backup specification information ([**VSS\_FILE\_SPEC\_BACKUP\_TYPE**](vss-file-spec-backup-type.md)) contained in each writer's Writer Metadata Document is available for examination after the successful return of [**IVssBackupComponents::GatherWriterMetadata**](ivssbackupcomponents-gatherwritermetadata.md).

However, a writer can add [*differenced files*](vssgloss-d.md#base-vssgloss-differenced-files) or ask for [*partial file support*](vssgloss-p.md#base-vssgloss-partial-file-support) until its successful handling of the [*PostSnapshot*](vssgloss-p.md#-win32-vssgloss-prepareforbackup-event) event.

Differenced file and partial file support specification can override the file specification backup type, so requesters may want to defer a full analysis of all writer specifications about incremental and differential backups until after the successful return of [**IVssBackupComponents::PrepareForBackup**](ivssbackupcomponents-prepareforbackup.md).

<dl> <dt>

<span id="Getting_File_Backup_Specification_Information"></span><span id="getting_file_backup_specification_information"></span><span id="GETTING_FILE_BACKUP_SPECIFICATION_INFORMATION"></span>Getting File Backup Specification Information
</dt> <dd>

The file-set-level file backup specification information ([**VSS\_FILE\_SPEC\_BACKUP\_TYPE**](vss-file-spec-backup-type.md)) is contained in each writer's Writer Metadata Document, and can be examined immediately after the successful return of [**IVssBackupComponents::GatherWriterMetadata**](ivssbackupcomponents-gatherwritermetadata.md).

Requesters must obtain file backup specification masks ([**VSS\_FILE\_SPEC\_BACKUP\_TYPE**](vss-file-spec-backup-type.md)) for every file set of each of a writer's components to be included in the incremental or differential backup, regardless of whether the component was [*explicitly*](vssgloss-e.md#base-vssgloss-explicit-component-inclusion) or [*implicitly*](vssgloss-i.md#base-vssgloss-implicit-component-inclusion) included.

A requester can determine which writers' Writer Metadata Document must be queried by using [**IVssBackupComponents::GetWriterComponentsCount**](ivssbackupcomponents-getwritercomponentscount.md) and [**IVssBackupComponents::GetWriterComponents**](ivssbackupcomponents-getwritercomponents.md). The instance of the [**IVssWriterComponentsExt**](ivsswritercomponentsext.md) interface returned by **IVssBackupComponents::GetWriterComponents** provides writer information through the [**IVssWriterComponentsExt::GetWriterInfo**](ivsswritercomponents-getwriterinfo.md) method.

The requester obtains component information through instances of the [**IVssWMComponent**](ivsswmcomponent.md) interface corresponding to an included component managed by a given writer by using [**IVssExamineWriterMetadata::GetComponent**](ivssexaminewritermetadata-getcomponent.md).

The information about file sets managed by the component corresponding to the [**IVssWMComponent**](ivsswmcomponent.md) interface is obtained by calls to [**IVssWMComponent::GetFile**](ivsswmcomponent-getfile.md), [**IVssWMComponent::GetDatabaseFile**](ivsswmcomponent-getdatabasefile.md), or [**IVssWMComponent::GetDatabaseLogFile**](ivsswmcomponent-getdatabaselogfile.md) (as appropriate).

These calls can return instances of the [**IVssWMFiledesc**](ivsswmfiledesc.md) interface for each of a component's file sets.

A file set's file specification backup type is obtained by calling [**IVssWMFiledesc::GetBackupTypeMask**](ivsswmfiledesc-getbackuptypemask.md).

</dd> <dt>

<span id="Getting_Partial_File_and_Differenced_File_Information"></span><span id="getting_partial_file_and_differenced_file_information"></span><span id="GETTING_PARTIAL_FILE_AND_DIFFERENCED_FILE_INFORMATION"></span>Getting Partial File and Differenced File Information
</dt> <dd>

A requester obtains partial file and differenced file information through the [**IVssComponent**](ivsscomponent.md) interface.

A requester can iterate over all writers included in a backup using [**IVssBackupComponents::GetWriterComponentsCount**](ivssbackupcomponents-getwritercomponentscount.md) and [**IVssBackupComponents::GetWriterComponents**](ivssbackupcomponents-getwritercomponents.md).

The instance of an [**IVssWriterComponentsExt**](ivsswritercomponentsext.md) interface returned by [**IVssBackupComponents::GetWriterComponents**](ivssbackupcomponents-getwritercomponents.md) provides access to all instances of the [**IVssComponent**](ivsscomponent.md) interface corresponding to a given writer's [*explicitly included*](vssgloss-e.md#base-vssgloss-explicit-component-inclusion) components through the [**IVssWriterComponentsExt::GetComponent**](ivsswritercomponents-getcomponent.md) and [**IVssWriterComponentsExt::GetComponentCount**](ivsswritercomponents-getcomponentcount.md) methods.

A requester will need to go through all instances of [**IVssComponent**](ivsscomponent.md) for all writers whose schema support the incremental or differential backup—that is, writers whose backup schema mask, as returned by [**IVssExamineWriterMetadata::GetBackupSchema**](ivssexaminewritermetadata-getbackupschema.md), includes **VSS\_BS\_INCREMENTAL** when the backup type is **VSS\_BT\_INCREMENTAL**, or **VSS\_BS\_DIFFERENTIAL** when the backup type is **VSS\_BS\_DIFFERENTIAL**.

Partial file information is obtained by calling [**IVssComponent::GetPartialFileCount**](ivsscomponent-getpartialfilecount.md) and [**IVssComponent::GetPartialFile**](ivsscomponent-getpartialfile.md) (see [Working with Partial Files](working-with-partial-files.md)).

For writers that support backup operations on the basis of a file's last modification data (writers whose backup schema mask, as returned by [**IVssExamineWriterMetadata::GetBackupSchema**](ivssexaminewritermetadata-getbackupschema.md), includes **VSS\_BS\_LAST\_MODIFY**), differenced file information is obtained by calling [**IVssComponent::GetDifferencedFilesCount**](ivsscomponent-getdifferencedfilescount.md) and [**IVssComponent::GetDifferencedFile**](ivsscomponent-getdifferencedfile.md).

Note that differenced files may be new files—that is, files that are not members of any file set currently in a given writer's Writer Metadata Document.

Requesters should not find files included both for partial file operations and as differenced files. If a requester does encounter such a circumstance, it should return and log a writer error.

A requester may still choose to proceed with backing up the problematic writer's files, but in that case should do so according to the specification found in the differenced file information.

</dd> </dl>

## Implementing Incremental or Differential Backups

Prior to implementing a backup, requesters should have information about which writers support an [*incremental*](vssgloss-i.md#base-vssgloss-incremental-backup-operations) or [*differential*](vssgloss-d.md#base-vssgloss-differential-backup-operations) backup, all requested partial file operations, all differenced files, and the file specification backup type of all other files.

<dl> <dt>

<span id="Nonsupporting_Writers"></span><span id="nonsupporting_writers"></span><span id="NONSUPPORTING_WRITERS"></span>Nonsupporting Writers
</dt> <dd>

Writers whose schema do not support the incremental or differential backup (writers whose backup schema mask, as returned by [**IVssExamineWriterMetadata::GetBackupSchema**](ivssexaminewritermetadata-getbackupschema.md), includes **VSS\_BS\_INCREMENTAL** when the backup type is **VSS\_BT\_INCREMENTAL** or does not include **VSS\_BS\_DIFFERENTIAL** when the backup type is **VSS\_BS\_DIFFERENTIAL**) cannot provide any direct support to an incremental or differential backup operation.

This does not necessarily mean that the writers' data will not be involved in an incremental or differential backup operation. However, the choice of what to do is at the discretion of the requester. The requester can do any of the following:

-   Back up no files belonging to the nonsupporting writers (clearly indicate this to the user)
-   Back up all the files of nonsupporting writers
-   Perform an incremental backup using file system data and the requester's own history logs.

The last alternative should be used with great care, and only if the requester understands if the writers involved can support incremental or differential backup and restoration of data independent of the VSS mechanism.

</dd> <dt>

<span id="Supporting_Writers"></span><span id="supporting_writers"></span><span id="SUPPORTING_WRITERS"></span>Supporting Writers
</dt> <dd>

A requester needs to process (in order) all of a writer's [*differenced files*](vssgloss-d.md#base-vssgloss-differenced-files), then handle any [*partial file*](vssgloss-p.md#base-vssgloss-partial-file-support) requests, and then back up remaining files according to their file specification backup type ([**VSS\_FILE\_SPEC\_BACKUP\_TYPE**](vss-file-spec-backup-type.md)).

1.  **Backing up Differenced Files:**

    For writers that support backup operations on the basis of last modification data (writers whose backup schema mask, as returned by [**IVssExamineWriterMetadata::GetBackupSchema**](ivssexaminewritermetadata-getbackupschema.md), includes **VSS\_BS\_LAST\_MODIFY**), a requester uses the path, file specification, and recursion flag information returned by [**IVssComponent::GetDifferencedFile**](ivsscomponent-getdifferencedfile.md) to generate a list of files as candidates for incremental backup or restore.

    [**IVssComponent::GetDifferencedFile**](ivsscomponent-getdifferencedfile.md) can also return a time of last modification (expressed as a [**FILETIME**](base.filetime_str) structure).

    If the last modification time supplied by the writer is nonzero, then the requester uses it as the basis (rather than file system information or the requester's own stored data) for determining if the file should be included in the [*incremental*](vssgloss-i.md#base-vssgloss-incremental-backup-operations) or [*differential*](vssgloss-d.md#base-vssgloss-differential-backup-operations) backup.

    For instance, if a file's last modification time as returned by the writer was:

    -   After the last full backup, the file should be included in both incremental and differential backups.
    -   After the last full backup but prior to the last incremental backup, the file should be included in incremental backup operations, but not differential backups.

    If the last modification time supplied by the writer is zero, then the requester must use file system information and its own stored data to determine the modification time of the differenced file.

2.  **Using Partial File Operations:**

    If a writer has requested that a file be backed up using a partial file operation, the requester uses the file offset information to save the indicated file segments to backup media. (See [Working with Partial Files](working-with-partial-files.md) for more information on partial file operations).

    As noted above, a writer should not designate a file both as a differenced file and as a participant in a partial file operation. If a requester does encounter such a circumstance, it should return and log a writer error.

    A requester may still choose to proceed with backing up the problematic writer's files, but in that case should do so according to the specification found in the differenced file information.

3.  **Working with File Specification Backup Type:**

    Having processed all differenced files and partial file operations, the requester now processes all remaining files in its backup set on the basis of their file specification backup type ([**VSS\_FILE\_SPEC\_BACKUP\_TYPE**](vss-file-spec-backup-type.md)).

    There are three "backup required" values of the [**VSS\_FILE\_SPEC\_BACKUP\_TYPE**](vss-file-spec-backup-type.md) enumeration that affect differential and incremental backups:

    -   VSS\_FSBT\_ALL\_BACKUP\_REQUIRED
    -   VSS\_FSBT\_INCREMENTAL\_BACKUP\_REQUIRED
    -   VSS\_FSBT\_DIFFERENTIAL\_BACKUP\_REQUIRED

    There are three "shadow copy required" values:

    -   VSS\_FSBT\_ALL\_SNAPSHOT\_REQUIRED
    -   VSS\_FSBT\_INCREMENTAL\_SNAPSHOT\_REQUIRED
    -   VSS\_FSBT\_DIFFERENTIAL\_SNAPSHOT\_REQUIRED

    File sets tagged with a file specification backup type of "shadow copy required" indicate that a requester needs to copy data from a shadow copy when performing INCREMENTAL, DIFFERENTIAL, or ALL (which includes both incremental and differential operations) backup operations.

    The "backup required" flag, applied to INCREMENTAL, DIFFERENTIAL, or ALL backup operations, indicates that the writer expects a copy of the current version of the file set to be available following the restore of any backup operation. Typically, this means that if a file set is tagged with "backup required," a requester will copy all its members to backup media during an incremental or differential backup, regardless of when their backup or modification last occurred.

    By default, file sets are added to components with a file specification backup type of VSS\_FSBT\_ALL\_BACKUP\_REQUIRED \| VSS\_FSBT\_ALL\_SNAPSHOT\_REQUIRED. Therefore, unless a writer explicitly sets the file specification backup type otherwise, requesters will need to copy those files not handled by partial file operations or designated differenced files in most file sets will typically be copied in their entirety to backup media.

</dd> <dt>

<span id="Backup_Stamps"></span><span id="backup_stamps"></span><span id="BACKUP_STAMPS"></span>Backup Stamps
</dt> <dd>

Writers that support backup stamps (VSS\_BS\_TIMESTAMP) may choose to generate backup stamp information to be used to support future incremental and differential backup and restore operations.

The format and information contained in strings containing backup stamp information are private to the writer that generates them; the requester does not know how to process this information.

Supporting writers store the backup stamp in the Backup Components Document as a string by using the [**IVssComponent::SetBackupStamp**](ivsscomponent-setbackupstamp.md) method.

The requester's role in handling backup stamp information is (if it exists) to make it available to the writer by calling [**IVssBackupComponents::SetPreviousBackupStamp**](ivssbackupcomponents-setpreviousbackupstamp.md) in a future backup or restore operation.

</dd> </dl>

 

 



