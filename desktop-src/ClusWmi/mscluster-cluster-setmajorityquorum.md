---
title: SetMajorityQuorum method of the MSCluster\_Cluster class
description: Sets the quorom to a majority quorum and uses the passed-in resource as the quorum witness resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4b25a95a-828c-413a-a30a-8515272a029c
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetMajorityQuorum method
- SetMajorityQuorum method, MSCluster_Cluster class
- MSCluster_Cluster class, SetMajorityQuorum method
topic_type:
- apiref
api_name:
- MSCluster_Cluster.SetMajorityQuorum
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetMajorityQuorum method of the MSCluster\_Cluster class

Sets the quorom to a majority quorum and uses the passed-in resource as the quorum witness resource.

## Syntax


```mof
void SetMajorityQuorum(
  [in] string Resource,
  [in] string QuorumPath
);
```



## Parameters

<dl> <dt>

*Resource* \[in\]
</dt> <dd>

The name of the disk quorum witness resource.

</dd> <dt>

*QuorumPath* \[in\]
</dt> <dd>

The optional path that will be used to maintain quorum files.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> </dl>

 

 





