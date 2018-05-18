---
title: Maintaining Physical Disk Resources
description: When a Physical Disk Resource has been created and assigned to a cluster, routine disk maintenance creates an ownership conflict between the Cluster Administrator and the system utilities used to perform the disk maintenance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4ccc1145-fbb3-48ba-9709-065c024e657c'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
---

# Maintaining Physical Disk Resources

When a Physical Disk Resource has been created and assigned to a cluster, routine disk maintenance creates an ownership conflict between the Cluster Administrator and the system utilities used to perform the disk maintenance. Maintenance mode for disk resources to address the ownership issue without causing a resource fail over.

Administrators use tools such as ChkDsk and VSS as part of weekly maintenance operation to ensure that disks are functional and there are no operational issues. These tools require exclusive access to the volume during their run. While these tools are in use, applications cannot read or write to the disk. The administrator expects the disk maintenance to succeed without ChkDsk failure and without a failover of the disk that the ChkDsk is run against.

Under normal circumstances, the cluster disk resources will fail over when ChkDsk (fix error mode), VSS restore or any other tool that locks or dismounts the volume is run against a clustered disk. These tools fails part way through since cluster disk resource fails its health check that causes the cluster service to fail over the disk to the other node. This causes the node where these tools are run to lose access to the disk.

Maintenance mode is a mechanism provided through failover cluster cmdlets and the Failover Cluster API that places the specified resource in a mode that will disable health checking. After maintenance mode is enabled for a resource, Resource Monitor will ignore health check calls on the resource even though the resource is left in online mode. This will allow tools like ChkDsk to function against a resource that is in maintenance mode. Administrators should note that while ChkDsk is running the disk resource is not available to the application even though the resource is in online mode. Additionally, if the resource is genuinely not available then any application or resource dependent on the resource that is put in maintenance mode will fail. Hence, it is critical that the user remove the maintenance mode as soon as the administrative task is done. Leaving a resource in maintenance mode may lead to unexpected application failures. This mode is persisted on the node until the administrator explicitly removes it. However, this mode is non-persistent across groups, and any failover or reboot of the node will clear this mode.

**Windows Server 2008:  **

Failover cluster cmdlets are not available; the Cluster.exe command is used instead. For more information, see [Extended maintenance mode functionality for cluster physical disk resources in Windows Server 2003](https://support.microsoft.com/kb/903650).

The cluster administrator can set, remove, or query a disk resource's maintenance mode through failover cluster cmdlets, or a calling application can place the resource in maintenance mode by using the [**ClusterResourceControl**](clusterresourcecontrol.md) API function with either the [**CLUSCTL\_RESOURCE\_SET\_MAINTENANCE\_MODE**](clusctl-resource-set-maintenance-mode.md) or [**CLUSCTL\_RESOURCE\_QUERY\_MAINTENANCE\_MODE**](clusctl-resource-query-maintenance-mode.md) cluster resource control codes.

**Windows Server 2008:  **

Failover cluster cmdlets are not available; the Cluster.exe command is used instead. For more information, see [Extended maintenance mode functionality for cluster physical disk resources in Windows Server 2003](https://support.microsoft.com/kb/903650).

Resources must be online and not be part of the resource quorum in order to set, remove, or query maintenance mode. Events which set or remove maintenance mode of a server are logged into the system event log.

 

 




