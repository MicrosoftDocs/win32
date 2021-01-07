---
description: A shadow copy provider must conform to guidelines to ensure requester compatibility.
ms.assetid: 49baeb89-1dc9-45c2-a532-071085a8e52f
title: Required Behaviors for Shadow Copy Providers
ms.topic: article
ms.date: 05/31/2018
---

# Required Behaviors for Shadow Copy Providers

A shadow copy provider must conform to guidelines to ensure requester compatibility. At runtime, a backup application or any other requester that uses shadow copies must function correctly without any knowledge of specific provider implementation details.

## Automagic Resource Management

It must be possible for the requester to simply add a volume to a shadow copy set. The requester can specify shadow copy attributes such as **VSS\_VOLSNAP\_ATTR\_TRANSPORTABLE**, **VSS\_VOLSNAP\_ATTR\_DIFFERENTIAL**, and/or **VSS\_VOLSNAP\_ATTR\_PLEX** in the [**\_VSS\_SNAPSHOT\_CONTEXT**](/windows/desktop/api/Vss/ne-vss-vss_snapshot_context). The provider must honor those attributes. If it cannot honor those attributes, then it should indicate that the shadow copy set is unsupported by setting the \**pbIsSupported* in [**IVssHardwareSnapshotProvider::AreLunsSupported**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-arelunssupported) to **FALSE**.

The provider must never agree to support a shadow copy that it cannot create. If the requester does not specify a plex or differential attribute, the provider must include automagic logic for allocating subsystem space for the shadow copy and create the shadow copy using the most appropriate method. The hardware provider must not include a provider-specific API for managing required shadow copy properties.

## Created Shadow Copy Volumes Are Read-Only and Hidden

VSS sets flags on each affected LUN such that the resulting shadow copy volumes will be hidden and read-only when detected by a computer running Windows Server 2003. Drive letters and mounted folders are not automatically assigned. VSS maintains these flags throughout the life cycle of a shadow copy.

## Hardware Shadow Copy LUNs Must Be Read/Write

VSS supports hardware shadow copies only where the underlying LUN is mapped as read/write. This must be done before the shadow copy is created; it cannot be done after the fact. Hardware providers should not modify these flags. For more information about how VSS uses these flags, see [The Shadow Copy Creation Process](the-shadow-copy-creation-process.md).

## Auto-Import Hardware Shadow Copies Are Not Supported on Windows Cluster Service

Windows Cluster service cannot accommodate LUNs with duplicate signatures and partition layout. The shadow copy LUNs must be transported to a host outside the cluster. For more information, see [Fast Recovery Using Transportable Shadow Copied Volumes](fast-recovery-using-transportable-shadow-copied-volumes.md).

## Shadow Copies That Contain Dynamic Disks Must Be Transported to a Different Host

**Prior to Windows Server 2008:** The native support for dynamic disks cannot accommodate LUNs with duplicate signatures and configuration database contents. The shadow copy LUNs must be transported to a different host. VSS enforces this by not allowing auto-import shadow copies of dynamic disks. A requester should not import a transportable shadow copy back to the same host.

**Beginning with Windows Server 2008:** This limitation is removed.

## Providers Are Out-of-Process

All providers must be implemented as out-of-process COM components.

## Time-Critical Operations

Long operations, such as syncing plexes, should be initiated in [**IVssHardwareSnapshotProvider::BeginPrepareSnapshot**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-beginpreparesnapshot). This function should start the asynchronous preparation work and return quickly. [**IVssProviderCreateSnapshotSet::EndPrepareSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-endpreparesnapshots) serves as a "rendezvous" function—the provider can wait synchronously in this method for the completion of the preparation work that was started by **BeginPrepareSnapshot**.

Providers must not add delays in [**IVssProviderCreateSnapshotSet::PreCommitSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-precommitsnapshots), [**IVssProviderCreateSnapshotSet::CommitSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-commitsnapshots), or [**IVssProviderCreateSnapshotSet::PostCommitSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-postcommitsnapshots) as applications are frozen during these calls. **CommitSnapshots** should return within seconds, because this is called during the Flush and Hold window, and VSS Kernel Support will cancel the Flush and Hold if the release is not received within 10 seconds, which would cause VSS to fail the shadow copy creation process. If the provider takes more than a few seconds to complete this call, there is a high probability that the shadow copy creation will fail.

## Careful I/O During CommitSnapshots

Hardware providers should not need to do any I/O to the volumes involved in the shadow copy during [**CommitSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-commitsnapshots). If any I/O is required, providers must not initiate any I/O to an original volume while handling the **CommitSnapshots** method.

During [**CommitSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-commitsnapshots), VSS Kernel Support drivers block I/O to the original volumes that are being shadow copied. If the provider uses synchronous I/O to a volume which is in the shadow copy set, then that I/O will be blocked and the shadow copy commit process will be deadlocked. The provider should not call any Win32 APIs during **CommitSnapshots** as they will have a high probability of causing I/O and a deadlock. The VSS Kernel Support timeout will break this deadlock after 10 seconds, but this will cause the shadow copy creation to fail.

If I/O must be attempted, it must be performed asynchronously. The I/O will not complete until after all providers have returned from their [**CommitSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-commitsnapshots) methods. In general, it is better to perform such operations in the [**PostCommitSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-postcommitsnapshots) call.

## Read/Write Shadow Copy LUNs

In this version, VSS supports only read/write shadow copy LUNs even if the volumes are exposed as read-only. The reason is that the system needs to change on-disk data structures such as:

-   Disk signature, which changes during the shadow copy process
-   Partition-related data structures, including those indicating the partition is read-only, hidden, a shadow copy, and should not be assigned a drive letter.

## Unique Page 83 Information

Both the original LUN and the newly created shadow copy LUN must have at least one unique storage identifier in the page 83 data. At least one STORAGE\_IDENTIFIER with a type of 1, 2, 3, or 8, and an association of 0 must be unique on the original LUN and the newly created shadow copy LUN.

 

 



