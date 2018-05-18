---
title: MoveFaultDomain method of the MSCluster\_FaultDomain class
description: Moves the fault domain hierarchy to a new parent.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '24fc785e-2c18-4824-897a-666b139e3d39'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MoveFaultDomain method", "MoveFaultDomain method, MSCluster_FaultDomain class", "MSCluster_FaultDomain class, MoveFaultDomain method"]
topic_type:
- apiref
api_name:
- MSCluster_FaultDomain.MoveFaultDomain
api_location:
- ClusWMI.dll
api_type:
- COM
---

# MoveFaultDomain method of the MSCluster\_FaultDomain class

Moves the fault domain hierarchy to a new parent.

## Syntax


```mof
uint32 MoveFaultDomain(
  [in] string FaultDomain,
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*FaultDomain* \[in\]
</dt> <dd>

The new fault domain to move to.

</dd> <dt>

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

 

 





