---
Description: Transportable shadow copies can be used to facilitate a fast recovery.
ms.assetid: 2eaffcf7-01b2-44ce-8bc4-fd9fa42c8a8c
title: Fast Recovery Using Transportable Shadow Copied Volumes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Fast Recovery Using Transportable Shadow Copied Volumes

[*Transportable shadow copies*](vssgloss-t.md#base-vssgloss-transportable-shadow-copy) can be used to facilitate a *fast recovery*.

Fast recovery can be used to quickly revert to an earlier shadow copy. The steps involved are:

1.  Create the transportable shadow copy of the appropriate LUNs. The shadow copy can be either [*persistent*](vssgloss-p.md#base-vssgloss-persistent-shadow-copy) or nonpersistent.
2.  Remove the original LUNs
    1.  If the computer is inside a cluster, mark the affected disk resources as offline, or enable the [maintenance mode](mscs.maintaining_physical_disk_resources) for these disk resources.
    2.  Mask the affected LUNs from this computer (and all other nodes if the computer is in a cluster).
3.  Import the shadow copy using the [**IVssBackupComponents::ImportSnapshots**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-importsnapshots?branch=master) method.
4.  Break the shadow copy using the [**IVssBackupComponents::BreakSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-breaksnapshotset?branch=master) method.
5.  Mark the new shadow copy volumes as read/write.
6.  If the computer is in a cluster, expose the new shadow copy LUNs as the original LUNs.
    1.  Unmask the shadow copy LUNs to the other nodes in the cluster.
    2.  Mark the resources that were previously marked as offline as online, or disable the maintenance mode for those disk resources.

> [!Note]  
> Transportable shadow copies in a cluster are not supported before Windows Server 2003 with Service Pack 1 (SP1). This is only supported with compliant LUNs, which have at least one SCSI Vital Product Data (VPD) page 0x83 STORAGE\_IDENTIFIER of type 1,2, or 8, and association 0, and the LUNs must maintain a basic disk with MBR partitioning.

 

 

 



