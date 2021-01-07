---
description: Hyper-V uses the Volume Shadow Copy Service (VSS) to backup and restore virtual machines.
ms.assetid: 94C67F22-658D-49DD-9588-6BB4FCF7ADA9
title: Backing up and restoring virtual machines
ms.topic: article
ms.date: 05/31/2018
---

# Backing up and restoring virtual machines

Hyper-V uses the Volume Shadow Copy Service (VSS) to backup and restore virtual machines. If the backup (volume snapshot) integration services are installed in the guest operating system, a VSS requester is installed that will allow VSS writers in the guest operating system to participate in the backup of the virtual machine. For details, see the following sections:

-   [Backing up the virtual machines](#backing-up-the-virtual-machines)
-   [Restoring the virtual machines](#restoring-the-virtual-machines)
-   [Failover clustering and Hyper-V VSS](#failover-clustering-and-hyper-v-vss)
-   [Details on the Hyper-V VSS Writer](#details-on-the-hyper-v-vss-writer)
-   [Related topics](#related-topics)

## Backing up the virtual machines

Hyper-V uses one of two mechanisms to back up each virtual machine. The default backup mechanism is called the "Saved State" method, where the virtual machine is put into a saved state during the processing of the PrepareForSnapshot event, snapshots are taken of the appropriate volumes, and the virtual machine is returned to the previous state during the processing of the PostSnapshot event.

The other backup mechanism is called the "Child VM Snapshot" method, which uses VSS inside the child virtual machine to participate in the backup. For the "Child VM Snapshot" method to be supported, all of the following conditions must be met:

-   Backup (volume snapshot) Integration Service is installed and running in the child virtual machine. The service name is "Hyper-V Volume Shadow Copy Requestor".
-   The child virtual machine must be in the running state.
-   The Snapshot File Location for the virtual machine is set to be the same volume in the host operating system as the VHD files for the virtual machine.
-   All volumes on the child virtual machine are basic disks and there are no dynamic disks.
-   All disks on the child virtual machine must use a file system that supports snapshots (for example, NTFS).

In general, the process for backing up virtual machines is the same as described in [Overview of Processing a Backup Under VSS](/windows/desktop/VSS/overview-of-processing-a-backup-under-vss). The unique behavior happens when the Hyper-V VSS writer (part of the "Hyper-V Virtual Machine Management" service) processes the PrepareForSnapshot event. If the backup was done using the "Child VM Snapshot" method, there is additional processing done but it is not visible to the child virtual machine.

The following procedure describes how to back up virtual machines.

**To back up virtual machines**

1.  For each virtual machine in the writer metadata, if the "Saved State" method is used, the virtual machine is put into a saved state. For virtual machines using the "Child VM Snapshot" method, the Hyper-V Volume Shadow Copy Requestor Service in the child virtual machine processes the backup as detailed in [Overview of Processing a Backup Under VSS](/windows/desktop/VSS/overview-of-processing-a-backup-under-vss). All VSS events on the child virtual machine occur during the host operating system processing of the PrepareForSnapshot event.
2.  After all virtual machines have either been put in the saved state or had snapshots taken, the Hyper-V VSS writer returns from the PrepareForSnapshot event. No processing is done by the Hyper-V VSS writer during the Freeze and Thaw events.
3.  When the Hyper-V VSS writer processes the PostSnapshot event, virtual machines that were backed up using the "Saved State" method and were put into a saved state by the Hyper-V VSS writer are returned to the state they were in before the backup started. For the virtual machines that were backed up using the "Child VM Snapshot" method, the host image of the VHD files that had the snapshots taken are rolled back to the snapshot taken during the processing of the PrepareForSnapshot event. This processing is done independently of the VSS writers on the child virtual machines so the snapshots taken must be auto-recoverable. (**VSS\_VOLSNAP\_ATTR\_NO\_AUTORECOVERY** is not set in the context.)

Partial backups are not supported. If any virtual machine fails to create a snapshot, no virtual machines will be backed up.

> [!Note]  
> Pass-through and iSCSI disks are not visible to the host operating system and therefore not backed up by the Hyper-V VSS writer. Backups of these volumes must be done entirely on the virtual machine.

 

## Restoring the virtual machines

Restoring the virtual machines is done entirely by the host operating system; the VSS writers on the child virtual machines are not involved.

The following procedure describes how to restore virtual machines.

**To restore virtual machines**

1.  During the processing of the PreRestore event, the Hyper-V VSS writer turns off and deletes any virtual machines that are about to be restored.
2.  After all VSS writers have processed the PreRestore event, the files are restored.
3.  During the processing of the PostRestore event, the Hyper-V VSS writer calls the [**IVssComponent::GetFileRestoreStatus**](/windows/desktop/api/vswriter/nf-vswriter-ivsscomponent-getfilerestorestatus) method. If the return is not **VSS\_RS\_ALL**, then the Hyper-V VSS writer calls the [**SetWriterFailure**](/windows/desktop/api/vswriter/nf-vswriter-cvsswriter-setwriterfailure) method and returns **False** from the [**OnPostRestore**](/windows/desktop/api/vswriter/nf-vswriter-cvsswriter-onpostrestore) method.
4.  For each virtual machine that was restored, the Hyper-V VSS writer registers the virtual machine with the Hyper-V management service. If the virtual machine is restored to a nondefault location, a symbolic link is created in the default location linking to that location.
5.  For each VHD that was restored, the location is compared with the one specified for that virtual machine. If the location is different, then the configuration is updated with the proper location.
6.  The network configuration is updated. If the virtual switches that the virtual machine was connected to when it was backed up still exit, new ports are created and connected to the virtual machine.

## Failover clustering and Hyper-V VSS

The Hyper-V VSS writer does not give any consideration to virtual machines that are part of a failover cluster. During both the "Saved State" method backups and all restores, the virtual machine would be put into the saved state or deleted entirely. This would be seen as a failure by the clustering service and cause the applications on those nodes to be failed over to other nodes. To avoid this during "Saved State" backups, the virtual machine state must be saved using the clustering service. To avoid this during a restore, the resources on the virtual machine would need to be taken offline.

## Details on the Hyper-V VSS Writer

Writer Name: Microsoft Hyper-V VSS Writer

Writer ID: 66841cd4-6ded-4f4b-8f17-fd23f8ddc3de

## Related topics

<dl> <dt>

[Overview of Processing a Backup Under VSS](/windows/desktop/VSS/overview-of-processing-a-backup-under-vss)
</dt> <dt>

[Overview of Processing a Restore Under VSS](/windows/desktop/VSS/overview-of-processing-a-restore-under-vss)
</dt> </dl>

 

 
