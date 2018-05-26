---
title: ClusVersion.ClusterHighestVersion property
description: Returns a value containing the highest version of the Cluster service with which the current cluster is compatible.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 016d6c19-1f24-4c04-8665-092ebb9464b7
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusterHighestVersion property Failover Cluster
- ClusterHighestVersion property Failover Cluster , ClusVersion object
- ClusVersion object Failover Cluster , ClusterHighestVersion property
topic_type:
- apiref
api_name:
- ClusVersion.ClusterHighestVersion
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusVersion.ClusterHighestVersion property

\[The **ClusterHighestVersion** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a value containing the highest version of the [*Cluster service*](c-gly.md#-wolf-cluster-service-gly) with which the current [*cluster*](c-gly.md#-wolf-cluster-gly) is compatible.

This property is read-only.

## Syntax


```VB
ClusVersion.ClusterHighestVersion
```



## Property value

**Long** that receives the version value. The upper 16 bits of the value indicate the release number of the Cluster service. The lower 16 bits specify the build number of the Cluster service.

## Remarks

All [**ClusVersion**](clusversion-object.md) properties are static values corresponding to the state of the cluster when the **ClusVersion** object was first created. To obtain the latest version information from the cluster, create a new **ClusVersion** object.

The cluster dynamically maintains the **ClusterHighestVersion** and [**ClusVersion.ClusterLowestVersion**](clusversion-clusterlowestversion.md) values based on the versions of the Cluster service running on the active [nodes](nodes.md). A node can join the cluster only if its version of the Cluster service is compatible with **ClusterHighestVersion** and **ClusVersion.ClusterLowestVersion**. For more information, see [Version Compatibility](version-compatibility.md).

## Examples

See [**ClusVersion**](clusversion-object.md) for an example.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusVersion is defined as F2E60716-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[**ClusVersion**](clusversion-object.md)
</dt> <dt>

[**ClusVersion.ClusterLowestVersion**](clusversion-clusterlowestversion.md)
</dt> <dt>

[**ClusVersion.MixedVersion**](clusversion-mixedversion.md)
</dt> </dl>

 

 





