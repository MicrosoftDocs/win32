---
title: ClusVersion.ClusterLowestVersion property
description: Returns a value containing the lowest version of the Cluster service with which the current cluster is compatible.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 32393f01-467f-4d73-bbe7-18c428806e7c
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusterLowestVersion property Failover Cluster
- ClusterLowestVersion property Failover Cluster , ClusVersion object
- ClusVersion object Failover Cluster , ClusterLowestVersion property
topic_type:
- apiref
api_name:
- ClusVersion.ClusterLowestVersion
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusVersion.ClusterLowestVersion property

\[The **ClusterLowestVersion** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a value containing the lowest version of the [*Cluster service*](https://www.bing.com/search?q=*Cluster service*) with which the current [*cluster*](https://www.bing.com/search?q=*cluster*) is compatible.

This property is read-only.

## Syntax


```VB
ClusVersion.ClusterLowestVersion
```



## Property value

**Long** that receives the version value. The upper 16 bits of the value indicate the release number of the Cluster service. The lower 16 bits specify the build number of the Cluster service.

## Remarks

All [**ClusVersion**](clusversion-object.md) properties are static values corresponding the state of the cluster when the **ClusVersion** object was first created. To obtain the latest version information from the cluster, create a new **ClusVersion** object.

The cluster dynamically maintains the [**ClusVersion.ClusterHighestVersion**](clusversion-clusterhighestversion.md) and **ClusterLowestVersion** values based on the versions of the Cluster service running on the active cluster [nodes](nodes.md). A node can join the cluster only if its version of the Cluster service is compatible with **ClusVersion.ClusterHighestVersion** and **ClusterLowestVersion**. For more information, see [Version Compatibility](version-compatibility.md).

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

[**ClusVersion.ClusterHighestVersion**](clusversion-clusterhighestversion.md)
</dt> <dt>

[**ClusVersion.MixedVersion**](clusversion-mixedversion.md)
</dt> </dl>

 

 





