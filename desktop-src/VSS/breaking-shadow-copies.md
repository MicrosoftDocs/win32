---
description: A requester can break a shadow copy set by using the IVssBackupComponents::BreakSnapshotSet or IVssBackupComponentsEx2::BreakSnapshotSetEx method.
ms.assetid: fb796b2f-b6fb-48ee-8d42-36f88cb165aa
title: Breaking Shadow Copies
ms.topic: article
ms.date: 05/31/2018
---

# Breaking Shadow Copies

A requester can break a shadow copy set by using the [**IVssBackupComponents::BreakSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-breaksnapshotset) or [**IVssBackupComponentsEx2::BreakSnapshotSetEx**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponentsex2-breaksnapshotsetex) method.

A broken shadow copy is a volume that contains a shadow copy that is no longer managed by VSS. Breaking a shadow copy has meaning only if the shadow copy's [*provider*](vssgloss-p.md) is a [*hardware provider*](vssgloss-h.md). This is because only hardware providers can implement a shadow copy as an actual volume with a life cycle independent of VSS. If VSS does not manage such a volume, it still is available.

Software providers maintain shadow copies only while involved in VSS operations. For that reason, breaking a shadow copy has no meaning for software providers.

If the shadow copy was managed by a hardware provider, the requester must import the shadow copy before calling [**BreakSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-breaksnapshotset) or [**BreakSnapshotSetEx**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponentsex2-breaksnapshotsetex). In case of non-transportable (created by a hardware provider) shadow copies, they are imported implicitly as part of the [**IVssBackupComponents::DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset) call.

After the requester has called [**BreakSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-breaksnapshotset) or [**BreakSnapshotSetEx**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponentsex2-breaksnapshotsetex), the shadow copy set is still accessible via its device objects or other access paths, but it is no longer a shadow copy set. It can be managed as one or more LUNs by using the Virtual Disk Service (VDS) COM interfaces. Using VDS, a requester can convert the LUNs to read/write, mount them with drive letters, or mask/unmask them to other computers. See the [VDS API documentation](../vds/virtual-disk-service-portal.md) for more information.

 

 
