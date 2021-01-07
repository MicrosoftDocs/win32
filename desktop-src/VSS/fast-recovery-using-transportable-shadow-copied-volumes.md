---
description: Transportable shadow copies can be used to facilitate a fast recovery.
ms.assetid: 2eaffcf7-01b2-44ce-8bc4-fd9fa42c8a8c
title: Fast Recovery Using Transportable Shadow Copied Volumes
ms.topic: article
ms.date: 05/31/2018
---

# Fast Recovery Using Transportable Shadow Copied Volumes

[*Transportable shadow copies*](vssgloss-t.md) can be used to facilitate a *fast recovery*.

Fast recovery can be used to quickly revert to an earlier shadow copy. The steps involved are:

1.  Create the transportable shadow copy of the appropriate LUNs. The shadow copy can be either [*persistent*](vssgloss-p.md) or nonpersistent.
2.  Remove the original LUNs
    1.  If the computer is inside a cluster, mark the affected disk resources as offline, or enable the [maintenance mode](/previous-versions/windows/desktop/mscs/maintaining-physical-disk-resources) for these disk resources.
    2.  Mask the affected LUNs from this computer (and all other nodes if the computer is in a cluster).
3.  Import the shadow copy using the [**IVssBackupComponents::ImportSnapshots**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-importsnapshots) method.
4.  Break the shadow copy using the [**IVssBackupComponents::BreakSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-breaksnapshotset) method.
5.  Mark the new shadow copy volumes as read/write.
6.  If the computer is in a cluster, expose the new shadow copy LUNs as the original LUNs.
    1.  Unmask the shadow copy LUNs to the other nodes in the cluster.
    2.  Mark the resources that were previously marked as offline as online, or disable the maintenance mode for those disk resources.

> [!Note]  
> Transportable shadow copies in a cluster are not supported before Windows Server 2003 with Service Pack 1 (SP1). This is only supported with compliant LUNs, which have at least one SCSI Vital Product Data (VPD) page 0x83 STORAGE\_IDENTIFIER of type 1,2, or 8, and association 0, and the LUNs must maintain a basic disk with MBR partitioning.

 

 

 
