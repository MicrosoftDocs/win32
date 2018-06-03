---
title: Backup and Restore Functions
description: The backup and restore functions are used by applications to take snapshots of the current cluster configuration and restore those configurations at a later time.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0f492e51-f364-40f1-b2c8-478f707f079d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- backup and restore functions Failover Cluster
- cluster utility functions Failover Cluster ,backup and restore functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Backup and Restore Functions

The backup and restore functions are used by applications to take snapshots of the current [*cluster*](https://www.bing.com/search?q=*cluster*) configuration and restore those configurations at a later time. This can provide manual or automatic recovery after upgrades, installs, or tests.

## In this section

<dl> <dt>

[**BackupClusterDatabase**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-backupclusterdatabase)
</dt> <dd>

Creates a backup of the [cluster database](cluster-database.md) and all registry [checkpoints](checkpointing.md).

</dd> <dt>

[*ClusterClearBackupStateForSharedVolume*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pcluster_clear_backup_state_for_shared_volume)
</dt> <dd>

Clears the backup state for the cluster shared volume

</dd> <dt>

[*ClusterGetVolumeNameForVolumeMountPoint*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pcluster_get_volume_name_for_volume_mount_point)
</dt> <dd>

[*ClusterGetVolumeNameForVolumeMountPoint*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pcluster_get_volume_name_for_volume_mount_point) may be altered or unavailable. Instead, use [*GetVolumeNameForVolumeMountPoint*](https://msdn.microsoft.com/library/windows/desktop/aa364994).

</dd> <dt>

[*ClusterGetVolumePathName*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pcluster_get_volume_path_name)
</dt> <dd>

[*ClusterGetVolumePathName*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pcluster_get_volume_path_name) may be altered or unavailable. Instead, use [*GetVolumePathName*](https://msdn.microsoft.com/library/windows/desktop/aa364996).

</dd> <dt>

[*ClusterIsPathOnSharedVolume*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pcluster_is_path_on_shared_volume)
</dt> <dd>

Determines whether a path is on a cluster shared volume

</dd> <dt>

[*ClusterPrepareSharedVolumeForBackup*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pcluster_prepare_shared_volume_for_backup)
</dt> <dd>

[*ClusterPrepareSharedVolumeForBackup*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pcluster_prepare_shared_volume_for_backup) may be altered or unavailable.

</dd> <dt>

[**RestoreClusterDatabase**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-restoreclusterdatabase)
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

 

 




