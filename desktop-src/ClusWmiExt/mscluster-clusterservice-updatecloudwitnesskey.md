---
title: UpdateCloudWitnessKey method of the MSCluster\_ClusterService class
description: Updates the account key associated with the cloud witness.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '82089cf4-f461-4946-9b6c-e22572b130cd'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["UpdateCloudWitnessKey method", "UpdateCloudWitnessKey method, MSCluster_ClusterService class", "MSCluster_ClusterService class, UpdateCloudWitnessKey method"]
topic_type:
- apiref
api_name:
- MSCluster_ClusterService.UpdateCloudWitnessKey
api_location:
- ClusWMI.dll
api_type:
- COM
---

# UpdateCloudWitnessKey method of the MSCluster\_ClusterService class

Updates the account key associated with the cloud witness.

## Syntax


```mof
uint32 UpdateCloudWitnessKey(
  [in] string AccountKey
);
```



## Parameters

<dl> <dt>

*AccountKey* \[in\]
</dt> <dd>

The cloud witness Account key.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\MSCluster<br/>                                                                |
| MOF<br/>                      | <dl> <dt>ClusWmiExt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl>    |



## See also

<dl> <dt>

[**MSCluster\_ClusterService**](mscluster-clusterservice.md)
</dt> </dl>

 

 





