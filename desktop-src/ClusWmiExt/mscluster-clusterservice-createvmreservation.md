---
title: CreateVmReservation method of the MSCluster\_ClusterService class
description: Reserves a virtual machine in the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5f6b93d6-6443-4791-a93d-c857a2175a8c
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateVmReservation method
- CreateVmReservation method, MSCluster_ClusterService class
- MSCluster_ClusterService class, CreateVmReservation method
topic_type:
- apiref
api_name:
- MSCluster_ClusterService.CreateVmReservation
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateVmReservation method of the MSCluster\_ClusterService class

Reserves a virtual machine in the cluster.

## Syntax


```mof
uint32 CreateVmReservation(
  [in]  uint32 VmMemory,
  [in]  uint32 VmVirtualCoreCount,
  [in]  uint32 VmCpuReservation,
  [in]  uint32 VmFlags,
  [in]  uint32 TimeSpan,
  [in]  string ReservationId,
  [out] uint32 NodeId
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

*TimeSpan* \[in\]
</dt> <dd>

The time span before the reservation ages out.

</dd> <dt>

*ReservationId* \[in\]
</dt> <dd>

The virtual machine reservation ID.

</dd> <dt>

*NodeId* \[out\]
</dt> <dd>

On success, returns the node ID on which the virtual machine is reserved.

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

 

 





