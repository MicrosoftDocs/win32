---
description: The Shadow Copy Creation Process
ms.assetid: ca484eec-31c6-4790-9232-3ed67263f6fb
title: The Shadow Copy Creation Process
ms.topic: article
ms.date: 05/31/2018
---

# The Shadow Copy Creation Process

The following is a detailed description of the hardware provider's role in the creation of a shadow copy set. For a diagram of this process, see [Shadow Copy Creation for Providers](shadow-copy-creation-for-providers.md).

1.  As the requester adds each volume to the shadow copy set, VSS determines the associated LUNs. For example, a spanned volume could be composed of multiple LUNs. VSS creates an initial [**VDS\_LUN\_INFORMATION**](/windows/win32/api/vdslun/ns-vdslun-vds_lun_information) using physical device information for each LUN.
2.  VSS calls [**AreLunsSupported**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-arelunssupported) to determine if the provider supports a shadow copy for that LUN. The hardware provider uses the [**VDS\_LUN\_INFORMATION**](/windows/win32/api/vdslun/ns-vdslun-vds_lun_information) to determine whether the LUNs are supported. This determination must be all or nothing—the same hardware provider must support all LUNs contributing to a specific volume. In the spanned volume example, the provider cannot indicate that it supports only one of the LUNs that comprise the volume.
3.  For each volume in the shadow copy set, VSS calls [**IVssHardwareSnapshotProvider::BeginPrepareSnapshot**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-beginpreparesnapshot) with the same array of [**VDS\_LUN\_INFORMATION**](/windows/win32/api/vdslun/ns-vdslun-vds_lun_information) structures. Within a single call, all LUNs in the array are unique, but the same LUN may appear in a subsequent call whenever the same LUN contributes to multiple volumes. The provider must handle that case correctly.
4.  Immediately after [**IVssProviderCreateSnapshotSet::EndPrepareSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-endpreparesnapshots), VSS will set the read-only, hidden, no drive letter, and shadow copy flags on all affected LUNs. The flags are implemented using hidden sectors on MBR disks or operating-system-specific bits in the partition header entry on GPT disks. The flags will cause all volumes on the affected disks to be surfaced on the receiving machines as read-only and hidden. Note that the shadow-copied LUNs have not been committed at this stage, so that in the event of a system crash, the flags will be cleared and the original LUN will not be affected. That is, all volumes on the original LUN will be treated as normal—and keep their original drive-letter assignments, mounted folders, and read/write status.
    > [!Note]  
    > Providers should not attempt to modify any of the LUN flags.

     

5.  At [**CommitSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-commitsnapshots), the shadow copy LUNs are committed. **CommitSnapshots** should be returned within a few seconds or the whole shadow copy creation process will probably fail.
6.  After [**CommitSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-commitsnapshots), VSS clears the flags on all original LUNs involved in the shadow copy. Since the shadow copy LUNs have been committed at this point, the shadow copy LUNs retain these flags.
7.  After [**IVssProviderCreateSnapshotSet::PostCommitSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-postcommitsnapshots), VSS clears the LUN flags (that it set after [**IVssProviderCreateSnapshotSet::EndPrepareSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-endpreparesnapshots)) and notifies the writers to thaw. VSS then calls the provider's [**IVssProviderCreateSnapshotSet::PreFinalCommitSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-prefinalcommitsnapshots) and [**IVssProviderCreateSnapshotSet::PostFinalCommitSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-postfinalcommitsnapshots) methods.
8.  VSS retrieves an array of [**VDS\_LUN\_INFORMATION**](/windows/win32/api/vdslun/ns-vdslun-vds_lun_information) structures, one for each newly created shadow copy LUN, by calling [**IVssHardwareSnapshotProvider::GetTargetLuns**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-gettargetluns). The provider must provide enough information to allow VSS and the provider to identify the shadow copies at any later time and on any system connected to the subsystem. At this time, the shadow copy LUNs should be inaccessible to this machine—the provider must use some mechanism other than by simply reading the information from the LUN.
9.  For transportable shadow copies, VSS appends the following to the Backup Components Document describing the shadow copy set:
    1.  The original LUN [**VDS\_LUN\_INFORMATION**](/windows/win32/api/vdslun/ns-vdslun-vds_lun_information) array.
    2.  The new shadow copy LUN [**VDS\_LUN\_INFORMATION**](/windows/win32/api/vdslun/ns-vdslun-vds_lun_information) array.
    3.  The disk extents for each volume in the shadow copy set.
10. For auto-import shadow copies, the import process begins. In [**IVssHardwareSnapshotProvider::LocateLuns**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-locateluns), the provider will be given the [**VDS\_LUN\_INFORMATION**](/windows/win32/api/vdslun/ns-vdslun-vds_lun_information) generated in [**GetTargetLuns**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-gettargetluns) at creation time. During **LocateLuns**, the provider should make those shadow copy LUNs visible to the system. The provider should not cause a bus rescan. VSS will cause the rescan and enumeration to allow the LUNs to be discovered by PNP and the volumes to come online.
11. VSS calls [**IVssHardwareSnapshotProvider::FillInLunInfo**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-fillinluninfo) for the newly arrived disks in the system. VSS uses the shadow copy LUN [**VDS\_LUN\_INFORMATION**](/windows/win32/api/vdslun/ns-vdslun-vds_lun_information) array from **FillInLunInfo**, comparing it with the **VDS\_LUN\_INFORMATION** generated during creation in [**GetTargetLuns**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-gettargetluns) and the disk extents for each volume in the shadow copy set to identify the newly arrived shadow copy LUNs.
12. At this point, all volumes contained on the shadow copy LUNs are mounted hidden and read-only, and VSS has a mapping from original volume to shadow copy volume.

Because a single LUN can contain portions of multiple volumes, the set of shadow copy LUNs may include "extra" volumes. Those volumes are not part of the shadow copy set and should not be used as they are not guaranteed to be consistent.

After import, the shadow copy can be accessed via the [**IVssBackupComponents::Query**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-query) method. A shadow copy can also be exposed as a drive letter, mounted folder, or share using [**IVssBackupComponents::ExposeSnapshot**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-exposesnapshot). A shadow copy set may also be converted to a regular LUN by using the [**IVssBackupComponents::BreakSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-breaksnapshotset) method. From there management applications can use appropriate disk management APIs to further manage the LUN (such as changing the read/write attributes).

### Transportable Shadow Copies on a SAN

Beginning with Windows Server 2003, Datacenter Edition and Windows Server 2003, Enterprise Edition, VSS enables transportable shadow copy sets on a SAN. From the point of view of a provider capable of transporting LUNs between hosts, there is little or no difference between a non-transportable and a transportable shadow copy set.

**Windows Server 2003, Standard Edition, Windows Server 2003, Web Edition and Windows XP:** Transportable shadow copy sets are not supported. All editions of Windows Server 2003 with Service Pack 1 (SP1) support transportable shadow copy sets.

Transportable shadow copy sets must be created with the **VSS\_VOLSNAP\_ATTR\_TRANSPORTABLE** attribute added to the shadow copy context described by the [**\_VSS\_VOLUME\_SNAPSHOT\_ATTRIBUTES**](/windows/desktop/api/Vss/ne-vss-vss_volume_snapshot_attributes) enumeration. All volumes in the set must be transportable. By returning success from [**IVssHardwareSnapshotProvider::AreLunsSupported**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-arelunssupported), the provider is indicating that not only does it support the LUN, but also that it can transport the LUN. The creation of a transportable shadow copy set concludes when VSS records the LUN information in the Backup Components Document. A shadow copy set may only be imported once after initial creation.

On the receiving machine, the requester imports the shadow copy set. The [**IVssBackupComponents::ImportSnapshots**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-importsnapshots) method uses the Backup Components Document describing the shadow copy set as input. Importing proceeds by:

1.  VSS constructs an array of shadow copy [**VDS\_LUN\_INFORMATION**](/windows/win32/api/vdslun/ns-vdslun-vds_lun_information) structures from the Backup Components Document.
2.  When VSS calls [**IVssHardwareSnapshotProvider::LocateLuns**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-locateluns), the array of [**VDS\_LUN\_INFORMATION**](/windows/win32/api/vdslun/ns-vdslun-vds_lun_information) structures generated in [**IVssHardwareSnapshotProvider::GetTargetLuns**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-gettargetluns) will be passed to the provider. While processing this method, the provider should make those shadow copy LUNs visible to the system. The provider should not cause a bus rescan. VSS will trigger the rescan and enumeration to allow the LUNs to be discovered by PNP and the volumes to come online.
3.  VSS calls [**IVssHardwareSnapshotProvider::FillInLunInfo**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-fillinluninfo) for the newly arrived disks in the system. VSS uses the shadow copy LUN array of [**VDS\_LUN\_INFORMATION**](/windows/win32/api/vdslun/ns-vdslun-vds_lun_information) structures from **FillInLunInfo**, comparing it with the **VDS\_LUN\_INFORMATION** generated during shadow copy set creation in [**GetTargetLuns**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-gettargetluns) and the disk extents for each volume in the shadow copy set to identify the newly arrived shadow copy LUNs.
4.  At this point, all volumes contained on the transported LUNs are mounted hidden and read-only and VSS has a mapping from the original volume to the shadow copy volume.

For both the single machine and transportable case, the sequence is similar starting with the point that [**GetTargetLuns**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-gettargetluns) is called. For auto-import, the steps happen directly after creation.

 

 
