---
title: ClusVersion.MixedVersion property
description: Indicates whether more than one version of the Cluster service is present in the cluster, a state described as mixed mode.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 20edafc7-5ff7-4a9a-b492-6e9230883643
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MixedVersion property Failover Cluster
- MixedVersion property Failover Cluster , ClusVersion object
- ClusVersion object Failover Cluster , MixedVersion property
topic_type:
- apiref
api_name:
- ClusVersion.MixedVersion
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusVersion.MixedVersion property

\[The **MixedVersion** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Indicates whether more than one version of the [Cluster service](cluster-service.md) is present in the [*cluster*](c-gly.md#-wolf-cluster-gly), a state described as [*mixed mode*](m-gly.md#-wolf-mixed-mode-gly).

This property is read-only.

## Syntax


```VB
ClusVersion.MixedVersion
```



## Property value

A **Variant** set to **TRUE** if the cluster version is mixed.

## Remarks

For more information on mixed mode clusters and compatibility between nodes running different versions of the Cluster service, see [Version Compatibility](version-compatibility.md).

All [**ClusVersion**](clusversion-object.md) properties are static values corresponding the state of the cluster when the **ClusVersion** object was first created. To obtain the latest version information from the cluster, create a new **ClusVersion** object.

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

[**ClusVersion.ClusterLowestVersion**](clusversion-clusterlowestversion.md)
</dt> </dl>

 

 





