---
title: GetParent method of the MSCluster\_FaultDomain class
description: Gets the parent of the fault domain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'dbe3f97a-bd38-4f4d-bb43-1cd49e6bf40f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetParent method", "GetParent method, MSCluster_FaultDomain class", "MSCluster_FaultDomain class, GetParent method"]
topic_type:
- apiref
api_name:
- MSCluster_FaultDomain.GetParent
api_location:
- ClusWMI.dll
api_type:
- COM
---

# GetParent method of the MSCluster\_FaultDomain class

Gets the parent of the fault domain.

## Syntax


```mof
uint32 GetParent(
  [out] MSCluster_FaultDomain Parent,
  [in]  uint32                Flags
);
```



## Parameters

<dl> <dt>

*Parent* \[out\]
</dt> <dd>

A [**MSCluster\_FaultDomain**](mscluster-faultdomain.md) that describes the parent of the fault domain.

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

 

 





