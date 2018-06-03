---
title: Version Compatibility
description: To allow for rolling upgrades and backward compatibility, failover clusters allow a certain degree of \ 0034;mixed mode \ 0034; clustering; that is, situations in which different cluster nodes are running different versions of the Cluster service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 919345fa-cbaa-4d01-bd3c-9ca69cab5094
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- version compatibility Failover Cluster
- version compatibility Failover Cluster
- version compatibility,(See also version compatibility Failover Cluster )
- version numbers Failover Cluster
- nodes Failover Cluster ,versions
- clusters Failover Cluster ,versions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Version Compatibility

To allow for rolling upgrades and backward compatibility, [*failover clusters*](https://www.bing.com/search?q=*failover clusters*) allow a certain degree of "mixed mode" clustering; that is, situations in which different cluster nodes are running different versions of the [Cluster service](cluster-service.md). This section describes how the [*cluster*](https://www.bing.com/search?q=*cluster*) determines whether a [node](nodes.md) can join a mixed-mode cluster.

## Version Numbers

A Cluster service version number is composed of two identifiers: a major version and a minor version.

-   The major version is an integer that identifies a particular release of the Cluster service. Note the following key points about the major version:

    -   The major version does not correspond to operating system version numbers.
    -   Nodes running different versions of the Cluster service are compatible only if the difference between their major versions is 1 or less.

-   The minor version is the build number of the Cluster service.

To create a version number, the Cluster service combines the major and minor versions as follows:

*Version* = (*major version* &lt;&lt; 16 ) \| *minor version*

For example, if a release of the Cluster service has a major version of 2 and a minor version of 224. The version is therefore 131296 (0x000200E0). ClusAPI.h defines the **CLUSTER\_MAKE\_VERSION**, **GET\_MINOR\_VERSION**, and **GET\_MAJOR\_VERSION** macros for translating the different version types.

> [!Note]  
> Unless specifically qualified as "major" or "minor," any references to "version" or "version number" in this documentation refer to the combination of major and minor versions.

 

## Node Version

Each node stores two [Cluster service](cluster-service.md) version numbers:

-   The currently installed version, stored in the [**NodeHighestVersion**](nodes-nodehighestversion.md) property.
-   The earliest version with which the currently installed version is compatible, stored in the [**NodeLowestVersion**](nodes-nodelowestversion.md) property.

These properties are read-only and are set when the Cluster service is installed on a node. They can be retrieved using [**ClusterNodeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternodecontrol) with the [CLUSCTL\_NODE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-node-get-ro-common-properties.md) control code.

Note that, as a service, the Cluster service is installed as part of the operating system installation process. In other words, the Cluster service version will change only when a different version of Windows is installed.

## Cluster Version

The cluster maintains two [Cluster service](cluster-service.md) version numbers, [**ClusterHighestVersion**](clusversion-clusterhighestversion.md) and [**ClusterLowestVersion**](clusversion-clusterlowestversion.md). These numbers are based on the version restrictions of all active nodes, as follows:

``` syntax
ClusterHighestVersion = Min( all active nodes' NodeHighestVersion properties ) +/- mitigating factors
ClusterLowestVersion = Max( all active nodes' NodeLowestVersion properties ) +/- mitigating factors
```

Where "mitigating factors" involve differences in minor version. Cluster version numbers are dynamic and are recalculated every time a node joins or leaves the cluster. To obtain their current values, call [**GetClusterInformation**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_information) and pass in a [**CLUSTERVERSIONINFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusterversioninfo) structure. The following structure members will contain version data:

``` syntax
ClusterVersionInfo.dwClusterHighestVersion = ClusterHighestVersion
ClusterVersionInfo.dwClusterLowestVersion = ClusterLowestVersion
```

When the cluster version changes, each resource DLL in the cluster is notified with the [CLUSCTL\_RESOURCE\_CLUSTER\_VERSION\_CHANGED](clusctl-resource-cluster-version-changed.md) control code.

## Joining

A node can join cluster only if one of the following is true:

-   NodeHighestVersion = ClusterHighestVersion
-   NodeLowestVersion = ClusterHighestVersion
-   NodeHighestVersion = ClusterLowestVersion.

## Programming Considerations

In very rare cases, you may have an application or other resource that is restricted to specific nodes or versions of Windows. Version compatibility then becomes a concern in maintaining the availability of your resource. Note the following:

-   Version number generation and assignment, as well as join protocols, are automatic. There are no points of intervention from the API.
-   You can only detect version changes "after the fact." In other words, when you call [**GetClusterInformation**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_information) or receive the [CLUSCTL\_RESOURCE\_CLUSTER\_VERSION\_CHANGED](clusctl-resource-cluster-version-changed.md) control code in your [resource DLL](resource-dlls.md), the version change has already taken place.

For node- or version- dependent applications or resources, you may want to provide documentation or create [private properties](private-properties.md) that communicate the restrictions to administrators.

 

 




