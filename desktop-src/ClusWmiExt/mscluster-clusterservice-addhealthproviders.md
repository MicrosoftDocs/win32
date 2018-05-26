---
title: AddHealthProviders method of the MSCluster\_ClusterService class
description: Adds health providers to the health service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6006eb12-4a43-4a17-8367-d396aa01c82e
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddHealthProviders method
- AddHealthProviders method, MSCluster_ClusterService class
- MSCluster_ClusterService class, AddHealthProviders method
topic_type:
- apiref
api_name:
- MSCluster_ClusterService.AddHealthProviders
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddHealthProviders method of the MSCluster\_ClusterService class

Adds health providers to the health service.

## Syntax


```mof
uint32 AddHealthProviders(
  [in] string Providers[]
);
```



## Parameters

<dl> <dt>

*Providers* \[in\]
</dt> <dd>

List of health ProviderIds that indicate the heal providers to add.

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

 

 





