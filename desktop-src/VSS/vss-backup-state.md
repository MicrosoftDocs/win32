---
description: During a backup operation, the requester uses IVssBackupComponents::SetBackupState to define the type of operation in progress.
ms.assetid: 43dcdac7-ed8e-4150-83eb-585e0e92f13c
title: VSS Backup State
ms.topic: article
ms.date: 05/31/2018
---

# VSS Backup State

During a backup operation, the requester uses [**IVssBackupComponents::SetBackupState**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupstate) to define the type of operation in progress.

This information is not included in an easily retrievable form in the Backup Components Document, so requester developers should store this information independently on any backup media.

The backup state contains the following:

<dl> <dt>

<span id="Backup_Type"></span><span id="backup_type"></span><span id="BACKUP_TYPE"></span>Backup Type
</dt> <dd>

The backup type specifies criteria for identifying files to be backed up. The evaluation of these criteria must be made using the VSS API.

When deciding on the type of backup to pursue and which writers to work with, requesters should examine the kinds (or schemas—see [Writer Backup Schema Support](writer-backup-schema-support.md)) of backup operations that each of the system's writers supports. Backups under VSS can be the following types:

-   Full (VSS\_BT\_FULL)—files will be backed up regardless of their last backup date. The backup history of each file will be updated, and this type of backup can be used as the basis of an incremental or differential backup. Restoring a full backup requires only a single backup image.
-   Copy Backup (VSS\_BT\_COPY)—like the VSS\_BT\_FULL backup type, files will be backed up regardless of their last backup date. However, the backup history of each file will not be updated, and this sort of backup cannot be used as the basis of an incremental or differential backup.
-   Incremental (VSS\_BT\_INCREMENTAL)—the VSS API is used to ensure that only files that have been changed or added since the last full or incremental backup are to be copied to a storage medium. Restoring an incremental backup requires the original backup image and all incremental backup images made since the initial backup.
-   Differential (VSS\_BT\_DIFFERENTIAL)—the VSS API is used to ensure that only files that have been changed or added since the last full backup are to be copied to a storage media; all intermediate backup information is ignored. Restoring a differential backup requires the original backup image and the most recent differential backup image made since the last full backup.
-   Log File (VSS\_BT\_LOG)—only a writer's log files (files added to a component with the [**IVssCreateWriterMetadata::AddDataBaseLogFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles) method, and retrieved by a call to [**IVssWMComponent::GetDatabaseLogFile**](/windows/desktop/api/VsBackup/nf-vsbackup-ivsswmcomponent-getdatabaselogfile)) will be backed up. This backup type is specific to VSS.

It is possible for requesters to implement these backups using information and methods outside of VSS. Only when a requester implements a backup using the VSS API should it be said to have one of the listed backup types. For instance, a requester participates in a VSS\_BT\_LOG type of backup only if it used the information returned by [**IVssWMComponent::GetDatabaseLogFile**](/windows/desktop/api/VsBackup/nf-vsbackup-ivsswmcomponent-getdatabaselogfile) to identify log files. Similarly, the VSS\_BT\_INCREMENTAL and VSS\_BT\_DIFFERENTIAL types apply only to incremental or differential operations, as described in [Incremental and Differential Backups](incremental-and-differential-backups.md).

</dd> <dt>

<span id="Specification_about_Selectability"></span><span id="specification_about_selectability"></span><span id="SPECIFICATION_ABOUT_SELECTABILITY"></span>Specification about Selectability
</dt> <dd>

A VSS backup may choose to respect VSS notions of component selectability—this is referred to as running in [*component mode*](vssgloss-c.md)—or to ignore them.

An example of not running in component mode would be performing a system image backup, where the backup application would need writer cooperation to ensure data stability but where selection of components would be irrelevant.

</dd> <dt>

<span id="Saving_Bootable_State"></span><span id="saving_bootable_state"></span><span id="SAVING_BOOTABLE_STATE"></span>Saving Bootable State
</dt> <dd>

VSS supports saving the running system state in a fully bootable configuration. However, this is not always necessary, and writer preparation to save a bootable state can sometimes degrade real-time performance of a running system.

Therefore, requesters indicate whether a backup will include a bootable system state as an argument to [**IVssBackupComponents::SetBackupState**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupstate). Writers determine whether they have to support saving the bootable system state by calling [**CVssWriter::IsBootableStateBackedUp**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-isbootablesystemstatebackedup).

Even if bootable system state is not selected, shadow copies of the system files will be made and the files may be backed up.

However, great care should be exercised in restoring system files if the backup did not save the bootable system state (see [Backing Up and Restoring System State in Windows Server 2003 R2 and Windows Server 2003 SP1](backing-up-and-restoring-system-state-under-vss.md)).

It is not possible to recover this information from a retrieved Backup Components Document, so requester authors should store whether the system was backed up with a bootable system state or not.

</dd> <dt>

<span id="Partial_File_Support"></span><span id="partial_file_support"></span><span id="PARTIAL_FILE_SUPPORT"></span>Partial File Support
</dt> <dd>

Some writers support file restoration through the overwriting of parts of the files they manage. A requester may be designed to take advantage of this, and if so it indicates this by setting the information in [**IVssBackupComponents::SetBackupState**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupstate).

</dd> </dl>

 

 



