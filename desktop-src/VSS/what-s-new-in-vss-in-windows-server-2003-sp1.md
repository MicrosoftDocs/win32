---
Description: The following list indicates additions and changes to the Volume Shadow Copy Service interface in Windows Server 2003 with Service Pack 1 (SP1)
ms.assetid: 9e0dba98-5d23-444d-bd2f-cb72de8fb2d2
title: Whats New in VSS in Windows Server 2003 SP1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What's New in VSS in Windows Server 2003 SP1

The following list indicates additions and changes to the Volume Shadow Copy Service interface in Windows Server 2003 with Service Pack 1 (SP1):

## Auto-recovery

[*Auto-recovery*](vssgloss-a.md#base-vssgloss-auto-recoved-shadow-copy) allows writers a time to update components in a shadow copy before the shadow copy is permanently changed to read-only. For example, a database may need to rollback any incomplete transactions for all shadow copies (the database writer would set the **VSS\_CF\_BACKUP\_RECOVERY** flag for the database components). Auto-recovery initiated by the requester allows both fine-grained restore (for example restoring one table in a database or one folder on a mail server), or the rollback to support data mining to perform analysis that would be too slow for a production server (the requester would add **VSS\_VOLSNAP\_ATTR\_ROLLBACK\_RECOVERY** to the shadow copy context.) Auto-recovery is not compatible with transportable shadow copies, but the same functionality is supported by using [Fast Recovery Using Transportable Shadow Copied Volumes](fast-recovery-using-transportable-shadow-copied-volumes.md).

The following programming elements have changes to support auto-recovery:

Class methods

-   [**CVssWriter::GetSnapshotDeviceName**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-getsnapshotdevicename?branch=master)
-   [**CVssWriter::OnPostSnapshot**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onpostsnapshot?branch=master)

Enumerations

-   [**VSS\_COMPONENT\_FLAGS**](/windows/win32/VsWriter/ne-vswriter-vss_component_flags?branch=master)
-   [**\_VSS\_VOLUME\_SNAPSHOT\_ATTRIBUTES**](/windows/win32/Vss/ne-vss-_vss_volume_snapshot_attributes?branch=master)

Interface methods

-   [**IVssProviderCreateSnapshotSet::PreFinalCommitSnapshots**](/windows/win32/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-prefinalcommitsnapshots?branch=master)
-   [**IVssProviderCreateSnapshotSet::PostFinalCommitSnapshots**](/windows/win32/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-postfinalcommitsnapshots?branch=master)

## Full Support for Transportable Shadow Copies

Transportable shadow copies are supported in all editions of Windows Server 2003 with SP1. For more information, see [Importing Transportable Shadow Copied Volumes](importing-transportable-shadow-copied-volumes.md).

## Fast Recovery Using Transportable Shadow Copied Volumes

[Fast Recovery Using Transportable Shadow Copied Volumes](fast-recovery-using-transportable-shadow-copied-volumes.md)

## Shadow copy storage area management

[**IVssSnapshotMgmt2**](/windows/win32/VsMgmt/nn-vsmgmt-ivsssnapshotmgmt2?branch=master)

 

 



