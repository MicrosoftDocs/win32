---
title: Backing Up and Restoring the Failover Cluster Configuration Using VSS
description: Failover clustering uses the Volume Shadow Copy Service (VSS) for backing up and restoring the failover cluster configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ea8b76b2-3931-4489-a648-e1077fd93b21
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Backing Up and Restoring the Failover Cluster Configuration Using VSS

Failover clustering uses the Volume Shadow Copy Service (VSS) for backing up and restoring the failover cluster configuration.

While a node is not part of a cluster or the cluster is down, the cluster configuration file (ClusDb) can be treated like any other registry hive. If the cluster is running, ClusDb will have to be committed on reboot as part of the registry. For information on handling registry backups and restores under VSS, see [Registry Backup and Restore Operations Under VSS](https://msdn.microsoft.com/library/windows/desktop/aa384595).

Because of the distributed nature of clusters, backing up a ClusDb is not sufficient to ensure that the full cluster state has been saved. This state is contained in the quorum resource or database.

For a backup application to successfully save the state of a clustered system, at a minimum it will need to perform the following steps:

1.  Detect whether the system is a clustered system and determine its current state.
2.  Select a clustered node for backup.
3.  Back up the clustered database and registry in a checkpointed form.

## Backing Up the Cluster State Using VSS

The first step in backing up or recovering a clustered system is to detect clustering services and determine their state using the [**GetNodeClusterState**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_node_cluster_state) function.

If clustering services are installed and running, backup applications (requesters) should choose to treat the system as a cluster. If clustering services are installed but not running, backup applications should treat the system as a stand-alone server.

If clustering services are detected, a backup application can display the cluster by name for backup. The cluster name can be determined by passing either the machine name or **NULL** to the [**OpenCluster**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster) function and retrieving a handle to the cluster to which the current node running the backup application belongs.

It is best to pass "machine name" as a parameter to the [**OpenCluster**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster) function if possible because this will ensure that the client is connected to the cluster even if the cluster service stops on the node to which the client is initially connected.

After the application has a handle to the cluster, the [**GetClusterInformation**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_information) function will provide information about the cluster, including its name.

Now, ClusDb can be backed up using VSS.

## Restoring the Cluster State Using VSS

There are two parts to restoring the cluster state:

1.  Restoring the node. This is completely taken care of in a system state restore on that particular node.

    If the rest of the cluster is running and you do not want to restore the cluster, stop at this point and restart the node; it should rejoin the cluster.

    If the cluster needs to be restored or rolled back in time, you will need to do an authoritative restore and restore the cluster.

2.  Restoring the cluster. To perform such a restore, the cluster service has to be installed but not necessarily running on the node being restored. All other nodes in the cluster must have the cluster service stopped. The [**IVssComponentEx2::SetAuthoritativeRestore**](https://msdn.microsoft.com/library/windows/desktop/aa382211) method is used to indicate that an authoritative restore is being performed.

    The Cluster VSS Writer will specify a restore method of **VSS\_RME\_RESTORE\_STOP\_START** to indicate that the specified service is to be stopped and restarted. For more information, see the description of the **VSS\_RME\_RESTORE\_STOP\_START** enumeration value in the [**VSS\_RESTOREMETHOD\_ENUM**](https://msdn.microsoft.com/library/windows/desktop/aa384964) enumeration topic. After the cluster service has been started, the other nodes on the cluster can have their cluster service restarted.

## Details on the Failover Cluster VSS Writer

Writer Name: Cluster Database

Writer ID: 41e12264-35d8-479b-8e5c-9b23d1dad37e

## Related topics

<dl> <dt>

[Changing The Cluster Configuration](changing-the-cluster-configuration.md)
</dt> <dt>

[Overview of Processing a Backup Under VSS](https://msdn.microsoft.com/library/windows/desktop/aa384589)
</dt> <dt>

[Overview of Processing a Restore Under VSS](https://msdn.microsoft.com/library/windows/desktop/aa384590)
</dt> <dt>

[Backup and Restore Functions](backup-and-restore-functions.md)
</dt> </dl>

 

 




