---
title: GetPlacementScore method of the MSCluster\_ClusterService class
description: Gets the placement score for a virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e8de35c9-3cbc-4d02-9b6a-1c05473b1c0f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetPlacementScore method", "GetPlacementScore method, MSCluster_ClusterService class", "MSCluster_ClusterService class, GetPlacementScore method"]
topic_type:
- apiref
api_name:
- MSCluster_ClusterService.GetPlacementScore
api_location:
- ClusWMI.dll
api_type:
- COM
---

# GetPlacementScore method of the MSCluster\_ClusterService class

Gets the placement score for a virtual machine.

## Syntax


```mof
uint32 GetPlacementScore(
  [in]  uint32 VmMemory,
  [in]  uint32 VmVirtualCoreCount,
  [in]  uint32 VmCpuReservation,
  [in]  uint32 VmFlags,
  [in]  real64 ReservedNodes,
  [out] uint32 MaxNumOfVMsInCluster,
  [out] uint32 MaxNumOfVMsInNode,
  [out] uint32 PlacementScoreFlags
);
```



## Parameters

<dl> <dt>

*VmMemory* \[in\]
</dt> <dd>

The memory size of a virtual machine.

</dd> <dt>

*VmVirtualCoreCount* \[in\]
</dt> <dd>

The number of virtual cores for the virtual machine.

</dd> <dt>

*VmCpuReservation* \[in\]
</dt> <dd>

The CPU reservation of a virtual machine.

</dd> <dt>

*VmFlags* \[in\]
</dt> <dd>

Reserved for future use.

</dd> <dt>

*ReservedNodes* \[in\]
</dt> <dd>

The amount of reserved nodes.

</dd> <dt>

*MaxNumOfVMsInCluster* \[out\]
</dt> <dd>

The max number of virtual machines of this spec that can be created in the cluster.

</dd> <dt>

*MaxNumOfVMsInNode* \[out\]
</dt> <dd>

On success, returns the max number of virtual machines of this spec that can be created the node that has the highest capacity.

</dd> <dt>

*PlacementScoreFlags* \[out\]
</dt> <dd>

Flags associated with the placement score.

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

 

 





