---
title: Backup and Restore Functions
description: The backup and restore functions are used by applications to take snapshots of the current cluster configuration and restore those configurations at a later time.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0f492e51-f364-40f1-b2c8-478f707f079d'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["backup and restore functions Failover Cluster", "cluster utility functions Failover Cluster ,backup and restore functions"]
---

# Backup and Restore Functions

The backup and restore functions are used by applications to take snapshots of the current [*cluster*](c-gly.md#-wolf-cluster-gly) configuration and restore those configurations at a later time. This can provide manual or automatic recovery after upgrades, installs, or tests.

## In this section

<dl> <dt>

[**BackupClusterDatabase**](backupclusterdatabase.md)
</dt> <dd>

Creates a backup of the [cluster database](cluster-database.md) and all registry [checkpoints](checkpointing.md).

</dd> <dt>

[*ClusterClearBackupStateForSharedVolume*](clusterclearbackupstateforsharedvolume.md)
</dt> <dd>

Clears the backup state for the cluster shared volume

</dd> <dt>

[*ClusterGetVolumeNameForVolumeMountPoint*](clustergetvolumenameforvolumemountpoint.md)
</dt> <dd>

[*ClusterGetVolumeNameForVolumeMountPoint*](clustergetvolumenameforvolumemountpoint.md) may be altered or unavailable. Instead, use [*GetVolumeNameForVolumeMountPoint*](https://msdn.microsoft.com/library/windows/desktop/aa364994).

</dd> <dt>

[*ClusterGetVolumePathName*](clustergetvolumepathname.md)
</dt> <dd>

[*ClusterGetVolumePathName*](clustergetvolumepathname.md) may be altered or unavailable. Instead, use [*GetVolumePathName*](https://msdn.microsoft.com/library/windows/desktop/aa364996).

</dd> <dt>

[*ClusterIsPathOnSharedVolume*](clusterispathonsharedvolume.md)
</dt> <dd>

Determines whether a path is on a cluster shared volume

</dd> <dt>

[*ClusterPrepareSharedVolumeForBackup*](clusterpreparesharedvolumeforbackup.md)
</dt> <dd>

[*ClusterPrepareSharedVolumeForBackup*](clusterpreparesharedvolumeforbackup.md) may be altered or unavailable.

</dd> <dt>

[**RestoreClusterDatabase**](restoreclusterdatabase.md)
</dt> <dd>

Restores the [cluster database](cluster-database.md) and restarts the [Cluster service](cluster-service.md) on the [node](nodes.md) from which the function is called. This node is called the restoring node.

> [!Note]  
> This function is available for use in the operating systems specified in the Requirements section. Support for this function was removed in Windows Server 2008 and this function does nothing and returns **ERROR\_CALL\_NOT\_IMPLEMENTED**.

 

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Utility Functions](cluster-utility-functions.md)
</dt> <dt>

[Backing Up and Restoring the Failover Cluster Configuration Using VSS](backing-up-and-restoring-the-failover-cluster-configuration-using-vss.md)
</dt> <dt>

[Backing Up and Restoring the Failover Cluster Configuration with Windows Server 2003](backing-up-and-restoring-the-cluster-configuration.md)
</dt> </dl>

 

 




