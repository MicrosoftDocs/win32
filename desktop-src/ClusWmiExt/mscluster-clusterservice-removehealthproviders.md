---
title: RemoveHealthProviders method of the MSCluster\_ClusterService class
description: Removes health providers from the health service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 355864a4-db3b-4f8a-be93-19482c87a80a
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveHealthProviders method
- RemoveHealthProviders method, MSCluster_ClusterService class
- MSCluster_ClusterService class, RemoveHealthProviders method
topic_type:
- apiref
api_name:
- MSCluster_ClusterService.RemoveHealthProviders
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveHealthProviders method of the MSCluster\_ClusterService class

Removes health providers from the health service.

## Syntax


```mof
uint32 RemoveHealthProviders(
  [in] string Providers[]
);
```



## Parameters

<dl> <dt>

*Providers* \[in\]
</dt> <dd>

List of health Provider Ids that indicate the providers to remove.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\MSCluster<br/>                                                                |
| MOF<br/>                      | <dl> <dt>ClusWmiExt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl>    |



## See also

<dl> <dt>

[**MSCluster\_ClusterService**](mscluster-clusterservice.md)
</dt> </dl>

 

 





