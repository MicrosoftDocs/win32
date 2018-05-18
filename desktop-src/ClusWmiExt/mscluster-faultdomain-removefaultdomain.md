---
title: RemoveFaultDomain method of the MSCluster\_FaultDomain class
description: Removes the fault domain from the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '195611ec-23c1-4fe1-821e-3d422c1b9ab9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveFaultDomain method", "RemoveFaultDomain method, MSCluster_FaultDomain class", "MSCluster_FaultDomain class, RemoveFaultDomain method"]
topic_type:
- apiref
api_name:
- MSCluster_FaultDomain.RemoveFaultDomain
api_location:
- ClusWMI.dll
api_type:
- COM
---

# RemoveFaultDomain method of the MSCluster\_FaultDomain class

Removes the fault domain from the cluster.

## Syntax


```mof
uint32 RemoveFaultDomain(
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*Flags* \[in\]
</dt> <dd>

Flags

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

[**MSCluster\_FaultDomain**](mscluster-faultdomain.md)
</dt> </dl>

 

 





