---
title: RemoveVmReservation method of the MSCluster\_ClusterService class
description: Removes the reservation of a virtual machine in the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a8df27d3-729d-4206-9d03-196f21b03241'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveVmReservation method", "RemoveVmReservation method, MSCluster_ClusterService class", "MSCluster_ClusterService class, RemoveVmReservation method"]
topic_type:
- apiref
api_name:
- MSCluster_ClusterService.RemoveVmReservation
api_location:
- ClusWMI.dll
api_type:
- COM
---

# RemoveVmReservation method of the MSCluster\_ClusterService class

Removes the reservation of a virtual machine in the cluster.

## Syntax


```mof
uint32 RemoveVmReservation(
  [in] string ReservationId,
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*ReservationId* \[in\]
</dt> <dd>

The virtual machine reservation ID.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Reserved flags that control usage.

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

 

 





