---
title: CreateCloudWitness method of the MSCluster\_ClusterService class
description: Creates a cloud witness quorum resource in the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 49389661-fb93-4031-b088-35264b68ffc7
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateCloudWitness method
- CreateCloudWitness method, MSCluster_ClusterService class
- MSCluster_ClusterService class, CreateCloudWitness method
topic_type:
- apiref
api_name:
- MSCluster_ClusterService.CreateCloudWitness
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateCloudWitness method of the MSCluster\_ClusterService class

Creates a cloud witness quorum resource in the cluster.

## Syntax


```mof
uint32 CreateCloudWitness(
  [in] string AccountName,
  [in] string AccountKey,
  [in] string EndpointInfo,
  [in] string CloudWitnessName
);
```



## Parameters

<dl> <dt>

*AccountName* \[in\]
</dt> <dd>

The cloud witness account name.

</dd> <dt>

*AccountKey* \[in\]
</dt> <dd>

The cloud witness Account key.

</dd> <dt>

*EndpointInfo* \[in\]
</dt> <dd>

The optional endpoint info for the cloud witness account.

</dd> <dt>

*CloudWitnessName* \[in\]
</dt> <dd>

The optional cloud witness resource name.

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

 

 





