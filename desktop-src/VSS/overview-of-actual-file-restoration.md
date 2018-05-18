---
Description: 'After performing the actions described in Overview of Restore Initialization and Overview of Preparing for Restore, the requester has sufficient information to begin restoring files.'
ms.assetid: '15df39fa-1eb1-4e96-9e26-14470f391de4'
title: Overview of Actual File Restoration
---

# Overview of Actual File Restoration

After performing the actions described in [Overview of Restore Initialization](overview-of-restore-initialization.md) and [Overview of Preparing for Restore](overview-of-preparing-for-restore.md), the requester has sufficient information to begin restoring files. File restoration does not involve writer interactions or the generation of events. For more information, see [Overview of Processing a Restore Under VSS](overview-of-processing-a-restore-under-vss.md).

The following table shows the sequence of actions and events that are required to restore files.



| Requester action                                                                                                                                                                                                                                                                                                          | Event | Writer action |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|---------------|
| Generate a restore set listing for files on backup media.                                                                                                                                                                                                                                                                 | None  | None          |
| Handle [*directed targets*](vssgloss-d.md#base-vssgloss-directed-targeting) or [*partial file*](vssgloss-p.md#base-vssgloss-partial-file-support) restoration (see [**IVssComponent::GetDirectedTarget**](ivsscomponent-getdirectedtarget.md), [**IVssComponent::GetPartialFile**](ivsscomponent-getpartialfile.md)). | None  | None          |
| If necessary, ignore all specified restore locations and restore to a new location specified in an earlier call to [**IVssBackupComponents::AddNewTarget**](ivssbackupcomponents-addnewtarget.md).                                                                                                                       | None  | None          |
| If the restore is incremental and further restores are needed, indicate (see [**IVssBackupComponents::SetAdditionalRestores**](ivssbackupcomponents-setadditionalrestores.md) and [Incremental and Differential Backups](incremental-and-differential-backups.md)).                                                     | None  | None          |
| To learn whether a writer has modified the contents of the Backup Components Document, call [**IVssBackupComponents::GetWriterComponents**](ivssbackupcomponents-getwritercomponents.md). For example, the writer might have changed the restore target.                                                                 | None  | None          |



 

## Requester Actions during Restoring Files

For most files on the backup media, the requester needs to determine their original locations and any new locations or alternate location mappings that apply to them. (See [Generating a Restore Set](generating-a-restore-set.md) for a discussion of best practices in determining which files to restore and where to restore them.)

In addition, some files may have [*directed targets*](vssgloss-d.md#base-vssgloss-directed-targeting) or support [*partial file*](vssgloss-p.md#base-vssgloss-partial-file-support) restoration. The number of such files can be found by calling [**IVssComponent::GetDirectedTargetCount**](ivsscomponent-getdirectedtargetcount.md) and [**IVssComponent::GetPartialFileCount**](ivsscomponent-getpartialfilecount.md), and information on detailed restoration instructions can be found by calling [**IVssComponent::AddDirectedTarget**](ivsscomponent-adddirectedtarget.md) and [**IVssComponent::GetPartialFile**](ivsscomponent-getpartialfile.md). (Partial and directed files can be part of components added implicitly or explicitly to the original backup, see [Working with Selectability For Restore and Subcomponents](working-with-selectability-for-restore-and-subcomponents.md) for more information.)

Success or failure of a restore is indicated on a component-by-component basis using [**IVssBackupComponents::SetFileRestoreStatus**](ivssbackupcomponents-setfilerestorestatus.md). The need for further restore operations (in the case of incremental or differential restores) is also indicated on a component-by-component basis using [**IVssBackupComponents::SetAdditionalRestores**](ivssbackupcomponents-setadditionalrestores.md).

In general, VSS does not specify a mechanism for retrieving data from a storage media, a choice of storage medium, or how to determine which files should be restored where.

However, for certain writers, restoring files may involve the use of a documented custom interface and procedure. Windows system writers, which currently require such support, are documented in [Special VSS Usage Cases](special-vss-usage-cases.md).

In general, it is recommended that the files of each component of each [*writer instance*](vssgloss-w.md#base-vssgloss-writer-instance) be processed as a unit. This requires the following:

-   Associating each file to be restored with the component that managed it. This requires the use of Writer Metadata Documents.
-   Obtaining correct restoration target information. This requires information from the Backup Components Document.

 

 



