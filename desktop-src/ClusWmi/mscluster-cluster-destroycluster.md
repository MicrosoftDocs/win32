---
title: DestroyCluster method of the MSCluster\_Cluster class
description: Removes the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fb3c1870-7746-4cd5-84f3-c6b4f7171ca0'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DestroyCluster method", "DestroyCluster method, MSCluster_Cluster class", "MSCluster_Cluster class, DestroyCluster method"]
topic_type:
- apiref
api_name:
- MSCluster_Cluster.DestroyCluster
api_location:
- ClusWMI.dll
api_type:
- COM
---

# DestroyCluster method of the MSCluster\_Cluster class

Removes the cluster.

## Syntax


```mof
void DestroyCluster(
  [in] boolean CleanupAD
);
```



## Parameters

<dl> <dt>

*CleanupAD* \[in\]
</dt> <dd>

Clean up the remaining computer objects and virtual computer objects in the current directory.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| Header<br/>                   | <dl> <dt>Clusapi.h</dt> </dl>   |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> </dl>

 

 





