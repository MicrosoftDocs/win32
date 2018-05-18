---
Description: 'In general, how a shadow copy is created depends on the type of shadow copy to be created, its context, and the role accorded to writers in the shadow copy operation.'
ms.assetid: 'eab3b39b-dfa7-43ea-adba-cd0b495c373f'
title: Shadow Copy Creation Details
---

# Shadow Copy Creation Details

In general, how a shadow copy is created depends on the type of shadow copy to be created, its context, and the role accorded to writers in the shadow copy operation. (See [Shadow Copy Context Configurations](shadow-copy-context-configurations.md) for more information.)

The shadow copy context is set by calling the [**IVssBackupComponents::SetContext**](ivssbackupcomponents-setcontext.md) method. Before calling the [**IVssBackupComponents::DoSnapshotSet**](ivssbackupcomponents-dosnapshotset.md) method to create a shadow copy, requesters must call the [**IVssBackupComponents**](ivssbackupcomponents.md) methods in the order specified in the following sections.

## Prerequisites for All Shadow Copies

Regardless of the level of writer participation, the creation of any shadow copy will always require the requestor be initialized with calls to [**IVssBackupComponents::InitializeForBackup**](ivssbackupcomponents-initializeforbackup.md) and [**IVssBackupComponents::StartSnapshotSet**](ivssbackupcomponents-startsnapshotset.md).

If this call is not made, the [**IVssBackupComponents::DoSnapshotSet**](ivssbackupcomponents-dosnapshotset.md) method will return an error.

## Shadow Copies with Writer Participation

If the shadow copy context specifies writer participation (that is, [**IVssBackupComponents::SetContext**](ivssbackupcomponents-setcontext.md) is called with **VSS\_CTX\_BACKUP**, or **VSS\_CTX\_APP\_ROLLBACK**):

-   Requesters must always call [**IVssBackupComponents::GatherWriterMetadata**](ivssbackupcomponents-gatherwritermetadata.md) when the shadow copy context supports writer participation. If the shadow copy context supports writer participation and **IVssBackupComponents::GatherWriterMetadata** is not called prior to [**IVssBackupComponents::DoSnapshotSet**](ivssbackupcomponents-dosnapshotset.md), an error will be returned.
-   If a requester wants to select specific writer components, it must call [**IVssBackupComponents::AddComponent**](ivssbackupcomponents-addcomponent.md) before calling [**StartSnapshotSet**](ivssbackupcomponents-startsnapshotset.md) to create the shadow copy set.
-   [**StartSnapshotSet**](ivssbackupcomponents-startsnapshotset.md) must be called to create the shadow copy set.
-   Requesters may add one or more volumes to the shadow copy set by calling [**AddToSnapshotSet**](ivssbackupcomponents-addtosnapshotset.md). Some writer components may not specify any affected volumes. In this case, it is acceptable for a snapshot set to be empty (that is, to contain no volumes).
-   To guarantee the consistency of writer metadata, a requester should always call [**IVssBackupComponents::PrepareForBackup**](ivssbackupcomponents-prepareforbackup.md) even if no components are selected. This causes VSS to generate a **PrepareForBackup** event, in which VSS calls the [**CVssWriter::OnPrepareBackup**](cvsswriter-onpreparebackup.md) method for each participating writer.
-   VSS will generate [*PrepareForSnapshot*](vssgloss-p.md#base-vssgloss-preparesnapshot-event) and [*Freeze*](vssgloss-f.md#base-vssgloss-freeze) events before creating the shadow copy in response to [**IVssBackupComponents::DoSnapshotSet**](ivssbackupcomponents-dosnapshotset.md). Writers will handle the events with [**CVssWriter::OnPrepareSnapshot**](cvsswriter-onpreparesnapshot.md) and [**CVssWriter::OnFreeze**](cvsswriter-onfreeze.md).
-   VSS will generate [*Thaw*](vssgloss-t.md#base-vssgloss-thaw-event) events and [*PostSnapshot*](vssgloss-p.md#base-vssgloss-postsnapshot-event) events after creating a shadow copy in response to [**IVssBackupComponents::DoSnapshotSet**](ivssbackupcomponents-dosnapshotset.md). Writers will handle the events with [**CVssWriter::OnThaw**](cvsswriter-onthaw.md) and [**CVssWriter::OnPostSnapshot**](cvsswriter-onpostsnapshot.md).

## Shadow Copies without Writer Participation

Creating shadow copies without writer participation is discouraged for standard backup applications (see [Backups without Writer Participation](backups-without-writer-participation.md)).

There are uses, such as fast backups of a disk to provide a safety net against accidental file corruption, which can be conducted without explicit writer participation. Such a shadow copy would have a context of either **VSS\_CTX\_FILE\_SHARE\_BACKUP** or **VSS\_CTX\_NAS\_ROLLBACK**.

For this type of shadow copy, note the following:

-   Requesters must still call the required methods listed in [Prerequisites for All Shadow Copies](#prerequisites-for-all-shadow-copies).
-   Requesters may call [**IVssBackupComponents::GatherWriterMetadata**](ivssbackupcomponents-gatherwritermetadata.md), but this is not required.
-   If requesters call [**IVssBackupComponents::AddComponent**](ivssbackupcomponents-addcomponent.md), [**IVssBackupComponents::PrepareForBackup**](ivssbackupcomponents-prepareforbackup.md), or [**IVssBackupComponents::BackupComplete**](ivssbackupcomponents-backupcomplete.md), an error will be returned.
-   Providers will not generate [*PrepareForSnapshot*](vssgloss-p.md#base-vssgloss-preparesnapshot-event), [*Freeze*](vssgloss-f.md#base-vssgloss-freeze), [*Thaw*](vssgloss-t.md#base-vssgloss-thaw-event), or [*PostSnapshot*](vssgloss-p.md#base-vssgloss-postsnapshot-event) events for this type of shadow copy.

 

 



