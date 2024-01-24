---
description: To fully implement a backup requires participation of the system's writers.
ms.assetid: ea504f8e-26d9-499e-b3e9-03515b480a75
title: Writer Backup Schema Support
ms.topic: article
ms.date: 05/31/2018
---

# Writer Backup Schema Support

To fully implement a backup requires participation of the system's writers. Different types of supported backups are referred to as schemas and are indicated by a bitmask (or bitwise OR) of members of the [**VSS\_BACKUP\_SCHEMA**](/windows/desktop/api/Vss/ne-vss-vss_backup_schema) enumeration. The currently supported valid schemas include the following:

-   Default Schema: Full (VSS\_BS\_UNDEFINED)—indicates that a writer supports a backup where all files will be backed up regardless of their last backup date. The backup history of each file can be updated by the requester, and writers supporting the VSS\_BS\_TIMESTAMPED enumeration value, it will store an updated time stamp with the requester. This backup scheme can be used as the basis of an incremental or differential backup.

    Restoring a full backup requires only a single backup image.

-   Copy Backup (VSS\_BS\_COPY)—like the VSS\_BS\_FULL backup schema, indicates that a writer supports a backup where all files will be backed up regardless of their last backup date. However, the backup history of each file will not be updated by either requester or writer, and this sort of backup cannot be used as the basis of an incremental or differential backup.
-   Log File (VSS\_BS\_LOG)—only a writer's log files are to be backed up. This requires a writer to have added at least one file to at least one component using the [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles) method. This backup type is specific to VSS.
-   Custom Restore Locations (VSS\_BS\_WRITER\_SUPPORTS\_NEW\_TARGET)—indicates writer support for a requester changing, at restore time, where its files are restored. This means that a writer has been coded to check for such relocation (using [**IVssComponent::GetNewTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getnewtarget)), and has the capacity for working with relocated files.
-   Restore with Move (VSS\_BS\_WRITER\_SUPPORTS\_RESTORE\_WITH\_MOVE)—indicates that the writer supports running multiple writer instances with the same class ID, and it supports a requester moving a component to a different writer instance at restore time. The writer instance is specified by using a persistent writer instance name that was passed as the *wszWriterInstanceName* parameter to the [**CVssWriter::Initialize**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-initialize) method. A requester can obtain the writer instance name using [**IVssExamineWriterMetadataEx::GetIdentityEx**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadataex-getidentityex) and move components during restore using [**IVssBackupComponentsEx::SetSelectedForRestoreEx**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponentsex-setselectedforrestoreex).

    **Windows Server 2003 and Windows XP:** This value is not supported until Windows Server 2003 with Service Pack 1 (SP1).

-   Incremental (VSS\_BS\_INCREMENTAL)—indicates that the writer uses the VSS API to help the requester, ensuring that only files that have been changed or added since the last full or incremental backup are to be copied to a storage medium.

    Restoring an incremental backup requires the original backup image and all incremental backup images made since the initial backup.

-   Differential (VSS\_BS\_DIFFERENTIAL)—indicates that the writer uses the VSS API to help the requester ensure that only files that have been changed or added since the last full backup are to be copied to a storage medium; all intermediate backup information is ignored.

    Restoring a differential backup requires the original backup image and the most recent differential backup image made since the last full backup.

-   Incremental/Differential: Time Stamping Support (VSS\_BS\_TIMESTAMPED)—indicates that a writer supports using the VSS time-stamp mechanism to include files in incremental or differential operations. At backup, the writer must store a [*file set's*](vssgloss-f.md) backup stamp with the [**IVssComponent::SetBackupStamp**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setbackupstamp) method, and at restore retrieve it with [**IVssComponent::GetPreviousBackupStamp**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getpreviousbackupstamp).
-   Incremental/Differential: Time of Last Modification Support (VSS\_BS\_LAST\_MODIFY)—indicates that when implementing incremental or differential backups with differenced files, a writer can provide last modification time information independently. This information can be provided to a requester via the [**IVssComponent::AddDifferencedFilesByLastModifyTime**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-adddifferencedfilesbylastmodifytime) method.
-   Incremental/Differential: Support Limitation (VSS\_BS\_EXCLUSIVE\_INCREMENTAL\_DIFFERENTIAL)—indicates writer support of both differential or increment backup schemas, but only exclusively: for example, you cannot follow an incremental backup with a differential backup.
-   Independent System State (VSS\_BS\_INDEPENDENT\_SYSTEM\_STATE)—indicates that the writer supports backing up data that is part of the system state, but that can also be backed up independently of the system state.

    **Windows Server 2003 and Windows XP:** This value is not supported until Windows Vista.

-   Roll-Forward Restore (VSS\_BS\_ROLLFORWARD\_RESTORE)—indicates that the writer supports a requester setting a roll-forward restore point using [**IVssBackupComponentsEx2::SetRollForward**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponentsex2-setrollforward).

    **Windows Server 2003 and Windows XP:** This value is not supported until Windows Vista.

-   Restore Rename (VSS\_BS\_RESTORE\_RENAME)—indicates that the writer supports a requester setting a restore name using [**IVssBackupComponentsEx2::SetRestoreName**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponentsex2-setrestorename).

    **Windows Server 2003 and Windows XP:** This value is not supported until Windows Vista.

-   Authoritative Restore (VSS\_BS\_AUTHORITATIVE\_RESTORE)—indicates that the writer supports a requester setting authoritative restore using [**IVssBackupComponentsEx2::SetAuthoritativeRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponentsex2-setauthoritativerestore).

Writers set their schemas using the [**IVssCreateWriterMetadata::SetBackupSchema**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-setbackupschema) method, and a requester obtains each writer's schema by calling [**IVssExamineWriterMetadata::GetBackupSchema**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getbackupschema).

 

 



