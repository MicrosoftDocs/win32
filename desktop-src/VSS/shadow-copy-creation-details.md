---
Description: In general, how a shadow copy is created depends on the type of shadow copy to be created, its context, and the role accorded to writers in the shadow copy operation.
ms.assetid: eab3b39b-dfa7-43ea-adba-cd0b495c373f
title: Shadow Copy Creation Details
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Shadow Copy Creation Details

In general, how a shadow copy is created depends on the type of shadow copy to be created, its context, and the role accorded to writers in the shadow copy operation. (See [Shadow Copy Context Configurations](shadow-copy-context-configurations.md) for more information.)

The shadow copy context is set by calling the [**IVssBackupComponents::SetContext**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setcontext?branch=master) method. Before calling the [**IVssBackupComponents::DoSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset?branch=master) method to create a shadow copy, requesters must call the [**IVssBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) methods in the order specified in the following sections.

## Prerequisites for All Shadow Copies

Regardless of the level of writer participation, the creation of any shadow copy will always require the requestor be initialized with calls to [**IVssBackupComponents::InitializeForBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-initializeforbackup?branch=master) and [**IVssBackupComponents::StartSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-startsnapshotset?branch=master).

If this call is not made, the [**IVssBackupComponents::DoSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset?branch=master) method will return an error.

## Shadow Copies with Writer Participation

If the shadow copy context specifies writer participation (that is, [**IVssBackupComponents::SetContext**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setcontext?branch=master) is called with **VSS\_CTX\_BACKUP**, or **VSS\_CTX\_APP\_ROLLBACK**):

-   Requesters must always call [**IVssBackupComponents::GatherWriterMetadata**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata?branch=master) when the shadow copy context supports writer participation. If the shadow copy context supports writer participation and **IVssBackupComponents::GatherWriterMetadata** is not called prior to [**IVssBackupComponents::DoSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset?branch=master), an error will be returned.
-   If a requester wants to select specific writer components, it must call [**IVssBackupComponents::AddComponent**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent?branch=master) before calling [**StartSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-startsnapshotset?branch=master) to create the shadow copy set.
-   [**StartSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-startsnapshotset?branch=master) must be called to create the shadow copy set.
-   Requesters may add one or more volumes to the shadow copy set by calling [**AddToSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addtosnapshotset?branch=master). Some writer components may not specify any affected volumes. In this case, it is acceptable for a snapshot set to be empty (that is, to contain no volumes).
-   To guarantee the consistency of writer metadata, a requester should always call [**IVssBackupComponents::PrepareForBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup?branch=master) even if no components are selected. This causes VSS to generate a **PrepareForBackup** event, in which VSS calls the [**CVssWriter::OnPrepareBackup**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onpreparebackup?branch=master) method for each participating writer.
-   VSS will generate [*PrepareForSnapshot*](vssgloss-p.md#base-vssgloss-preparesnapshot-event) and [*Freeze*](vssgloss-f.md#base-vssgloss-freeze) events before creating the shadow copy in response to [**IVssBackupComponents::DoSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset?branch=master). Writers will handle the events with [**CVssWriter::OnPrepareSnapshot**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onpreparesnapshot?branch=master) and [**CVssWriter::OnFreeze**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onfreeze?branch=master).
-   VSS will generate [*Thaw*](vssgloss-t.md#base-vssgloss-thaw-event) events and [*PostSnapshot*](vssgloss-p.md#base-vssgloss-postsnapshot-event) events after creating a shadow copy in response to [**IVssBackupComponents::DoSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset?branch=master). Writers will handle the events with [**CVssWriter::OnThaw**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onthaw?branch=master) and [**CVssWriter::OnPostSnapshot**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onpostsnapshot?branch=master).

## Shadow Copies without Writer Participation

Creating shadow copies without writer participation is discouraged for standard backup applications (see [Backups without Writer Participation](backups-without-writer-participation.md)).

There are uses, such as fast backups of a disk to provide a safety net against accidental file corruption, which can be conducted without explicit writer participation. Such a shadow copy would have a context of either **VSS\_CTX\_FILE\_SHARE\_BACKUP** or **VSS\_CTX\_NAS\_ROLLBACK**.

For this type of shadow copy, note the following:

-   Requesters must still call the required methods listed in [Prerequisites for All Shadow Copies](#prerequisites-for-all-shadow-copies).
-   Requesters may call [**IVssBackupComponents::GatherWriterMetadata**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata?branch=master), but this is not required.
-   If requesters call [**IVssBackupComponents::AddComponent**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent?branch=master), [**IVssBackupComponents::PrepareForBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup?branch=master), or [**IVssBackupComponents::BackupComplete**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-backupcomplete?branch=master), an error will be returned.
-   Providers will not generate [*PrepareForSnapshot*](vssgloss-p.md#base-vssgloss-preparesnapshot-event), [*Freeze*](vssgloss-f.md#base-vssgloss-freeze), [*Thaw*](vssgloss-t.md#base-vssgloss-thaw-event), or [*PostSnapshot*](vssgloss-p.md#base-vssgloss-postsnapshot-event) events for this type of shadow copy.

 

 



