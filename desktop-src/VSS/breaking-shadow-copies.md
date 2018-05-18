---
Description: 'A requester can break a shadow copy set by using the IVssBackupComponents::BreakSnapshotSet or IVssBackupComponentsEx2::BreakSnapshotSetEx method.'
ms.assetid: 'fb796b2f-b6fb-48ee-8d42-36f88cb165aa'
title: Breaking Shadow Copies
---

# Breaking Shadow Copies

A requester can break a shadow copy set by using the [**IVssBackupComponents::BreakSnapshotSet**](ivssbackupcomponents-breaksnapshotset.md) or [**IVssBackupComponentsEx2::BreakSnapshotSetEx**](ivssbackupcomponentsex2-breaksnapshotsetex.md) method.

A broken shadow copy is a volume that contains a shadow copy that is no longer managed by VSS. Breaking a shadow copy has meaning only if the shadow copy's [*provider*](vssgloss-p.md#base-vssgloss-provider) is a [*hardware provider*](vssgloss-h.md#base-vssgloss-hardware-based-provider). This is because only hardware providers can implement a shadow copy as an actual volume with a life cycle independent of VSS. If VSS does not manage such a volume, it still is available.

Software providers maintain shadow copies only while involved in VSS operations. For that reason, breaking a shadow copy has no meaning for software providers.

If the shadow copy was managed by a hardware provider, the requester must import the shadow copy before calling [**BreakSnapshotSet**](ivssbackupcomponents-breaksnapshotset.md) or [**BreakSnapshotSetEx**](ivssbackupcomponentsex2-breaksnapshotsetex.md). In case of non-transportable (created by a hardware provider) shadow copies, they are imported implicitly as part of the [**IVssBackupComponents::DoSnapshotSet**](ivssbackupcomponents-dosnapshotset.md) call.

After the requester has called [**BreakSnapshotSet**](ivssbackupcomponents-breaksnapshotset.md) or [**BreakSnapshotSetEx**](ivssbackupcomponentsex2-breaksnapshotsetex.md), the shadow copy set is still accessible via its device objects or other access paths, but it is no longer a shadow copy set. It can be managed as one or more LUNs by using the Virtual Disk Service (VDS) COM interfaces. Using VDS, a requester can convert the LUNs to read/write, mount them with drive letters, or mask/unmask them to other computers. See the [VDS API documentation](base.vds_programming_guide_portal) for more information.

 

 



