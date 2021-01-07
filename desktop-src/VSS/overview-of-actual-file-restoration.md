---
description: After performing the actions described in Overview of Restore Initialization and Overview of Preparing for Restore, the requester has sufficient information to begin restoring files.
ms.assetid: 15df39fa-1eb1-4e96-9e26-14470f391de4
title: Overview of Actual File Restoration
ms.topic: article
ms.date: 05/31/2018
---

# Overview of Actual File Restoration

After performing the actions described in [Overview of Restore Initialization](overview-of-restore-initialization.md) and [Overview of Preparing for Restore](overview-of-preparing-for-restore.md), the requester has sufficient information to begin restoring files. File restoration does not involve writer interactions or the generation of events. For more information, see [Overview of Processing a Restore Under VSS](overview-of-processing-a-restore-under-vss.md).

The following table shows the sequence of actions and events that are required to restore files.



| Requester action                                                                                                                                                                                                                                                                                                          | Event | Writer action |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|---------------|
| Generate a restore set listing for files on backup media.                                                                                                                                                                                                                                                                 | None  | None          |
| Handle [*directed targets*](vssgloss-d.md) or [*partial file*](vssgloss-p.md) restoration (see [**IVssComponent::GetDirectedTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getdirectedtarget), [**IVssComponent::GetPartialFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getpartialfile)). | None  | None          |
| If necessary, ignore all specified restore locations and restore to a new location specified in an earlier call to [**IVssBackupComponents::AddNewTarget**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addnewtarget).                                                                                                                       | None  | None          |
| If the restore is incremental and further restores are needed, indicate (see [**IVssBackupComponents::SetAdditionalRestores**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setadditionalrestores) and [Incremental and Differential Backups](incremental-and-differential-backups.md)).                                                     | None  | None          |
| To learn whether a writer has modified the contents of the Backup Components Document, call [**IVssBackupComponents::GetWriterComponents**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritercomponents). For example, the writer might have changed the restore target.                                                                 | None  | None          |



 

## Requester Actions during Restoring Files

For most files on the backup media, the requester needs to determine their original locations and any new locations or alternate location mappings that apply to them. (See [Generating a Restore Set](generating-a-restore-set.md) for a discussion of best practices in determining which files to restore and where to restore them.)

In addition, some files may have [*directed targets*](vssgloss-d.md) or support [*partial file*](vssgloss-p.md) restoration. The number of such files can be found by calling [**IVssComponent::GetDirectedTargetCount**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getdirectedtargetcount) and [**IVssComponent::GetPartialFileCount**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getpartialfilecount), and information on detailed restoration instructions can be found by calling [**IVssComponent::AddDirectedTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-adddirectedtarget) and [**IVssComponent::GetPartialFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getpartialfile). (Partial and directed files can be part of components added implicitly or explicitly to the original backup, see [Working with Selectability For Restore and Subcomponents](working-with-selectability-for-restore-and-subcomponents.md) for more information.)

Success or failure of a restore is indicated on a component-by-component basis using [**IVssBackupComponents::SetFileRestoreStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setfilerestorestatus). The need for further restore operations (in the case of incremental or differential restores) is also indicated on a component-by-component basis using [**IVssBackupComponents::SetAdditionalRestores**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setadditionalrestores).

In general, VSS does not specify a mechanism for retrieving data from a storage media, a choice of storage medium, or how to determine which files should be restored where.

However, for certain writers, restoring files may involve the use of a documented custom interface and procedure. Windows system writers, which currently require such support, are documented in [Special VSS Usage Cases](special-vss-usage-cases.md).

In general, it is recommended that the files of each component of each [*writer instance*](vssgloss-w.md) be processed as a unit. This requires the following:

-   Associating each file to be restored with the component that managed it. This requires the use of Writer Metadata Documents.
-   Obtaining correct restoration target information. This requires information from the Backup Components Document.

 

 



