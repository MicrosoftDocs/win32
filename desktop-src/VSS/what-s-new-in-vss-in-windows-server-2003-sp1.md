---
description: 'The following list indicates additions and changes to the Volume Shadow Copy Service interface in Windows Server 2003 with Service Pack 1 (SP1):'
ms.assetid: 9e0dba98-5d23-444d-bd2f-cb72de8fb2d2
title: What's New in VSS in Windows Server 2003 SP1
ms.topic: article
ms.date: 05/31/2018
---

# What's New in VSS in Windows Server 2003 SP1

The following list indicates additions and changes to the Volume Shadow Copy Service interface in Windows Server 2003 with Service Pack 1 (SP1):

## Auto-recovery

[*Auto-recovery*](vssgloss-a.md) allows writers a time to update components in a shadow copy before the shadow copy is permanently changed to read-only. For example, a database may need to rollback any incomplete transactions for all shadow copies (the database writer would set the **VSS\_CF\_BACKUP\_RECOVERY** flag for the database components). Auto-recovery initiated by the requester allows both fine-grained restore (for example restoring one table in a database or one folder on a mail server), or the rollback to support data mining to perform analysis that would be too slow for a production server (the requester would add **VSS\_VOLSNAP\_ATTR\_ROLLBACK\_RECOVERY** to the shadow copy context.) Auto-recovery is not compatible with transportable shadow copies, but the same functionality is supported by using [Fast Recovery Using Transportable Shadow Copied Volumes](fast-recovery-using-transportable-shadow-copied-volumes.md).

The following programming elements have changes to support auto-recovery:

Class methods

-   [**CVssWriter::GetSnapshotDeviceName**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-getsnapshotdevicename)
-   [**CVssWriter::OnPostSnapshot**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onpostsnapshot)

Enumerations

-   [**VSS\_COMPONENT\_FLAGS**](/windows/desktop/api/VsWriter/ne-vswriter-vss_component_flags)
-   [**\_VSS\_VOLUME\_SNAPSHOT\_ATTRIBUTES**](/windows/desktop/api/Vss/ne-vss-vss_volume_snapshot_attributes)

Interface methods

-   [**IVssProviderCreateSnapshotSet::PreFinalCommitSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-prefinalcommitsnapshots)
-   [**IVssProviderCreateSnapshotSet::PostFinalCommitSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-postfinalcommitsnapshots)

## Full Support for Transportable Shadow Copies

Transportable shadow copies are supported in all editions of Windows Server 2003 with SP1. For more information, see [Importing Transportable Shadow Copied Volumes](importing-transportable-shadow-copied-volumes.md).

## Fast Recovery Using Transportable Shadow Copied Volumes

[Fast Recovery Using Transportable Shadow Copied Volumes](fast-recovery-using-transportable-shadow-copied-volumes.md)

## Shadow copy storage area management

[**IVssSnapshotMgmt2**](/windows/desktop/api/VsMgmt/nn-vsmgmt-ivsssnapshotmgmt2)

 

 



