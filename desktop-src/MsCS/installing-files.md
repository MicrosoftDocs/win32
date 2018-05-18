---
title: Installing Files
description: Use the following procedure to install and distribute the files associated with a resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '91d19dc0-2c2b-4b55-adf5-8661ef3597db'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["cluster-aware applications Failover Cluster ,creating setup applications, files Failover Cluster ,installing"]
---

# Installing Files

Use the following procedure to install and distribute the files associated with a [resource type](resource-types.md).

**To install resource type files**

1.  Call the [**GetNodeClusterState**](getnodeclusterstate.md) function to determine if setup is running in a clustered environment.
2.  If the [Cluster service](cluster-service.md) is installed but not running, give the user the option of starting the Cluster service before proceeding with the installation.
3.  If the Cluster service is not installed, you can choose to install a non-cluster version of your resource or not, depending on your requirements.
4.  For each type of resource supported by your [resource DLL](resource-dlls.md), install the necessary program files on one of the nodes. This includes binaries, COM and ActiveX components, and other files required for the [node](nodes.md) to run a local instance of the resource. Data files should be stored on a cluster disk.
5.  Copy your resource DLL and your extension DLL to the node. Use path and filenames that can be consistent across all nodes. For more information, see [Deploying Resource Types](deploying-resource-types.md).
6.  Once the application and the DLLs are installed on one node, enumerate the other nodes and then use the administration shares and remote registry manipulation to install the application and distribute the files over the network. For information on enumeration see [Enumerating Objects](enumerating-objects.md).
7.  Additionally, copy your extension DLL to any remote system that will use [Cluster Administrator](cluster-administrator.md) to administer the cluster.

Your setup application can now register your resource type. See [Registering Resource Types](registering-resource-types.md).

> [!Note]  
> You should not store program files on cluster disks. Although these drives may seem to be the ideal location for program files because all nodes in the [*cluster*](c-gly.md#-wolf-cluster-gly) can access them, storing files there causes problems when you upgrade either the Cluster service or the application software, especially if the cluster is in a production environment. Such upgrades require the cluster to be shut down completely. If you choose instead to install program files on all nodes in the cluster, you can use a rolling upgrade approach—upgrading each node individually—without affecting the operation of the cluster.

 

 

 




