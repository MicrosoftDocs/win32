---
title: CreateFaultDomain method of the MSCluster\_FaultDomain class
description: Creates a fault domain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '56b47899-edf7-49c7-ab53-dcf9485fb570'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateFaultDomain method", "CreateFaultDomain method, MSCluster_FaultDomain class", "MSCluster_FaultDomain class, CreateFaultDomain method"]
topic_type:
- apiref
api_name:
- MSCluster_FaultDomain.CreateFaultDomain
api_location:
- ClusWMI.dll
api_type:
- COM
---

# CreateFaultDomain method of the MSCluster\_FaultDomain class

Creates a fault domain.

## Syntax


```mof
uint32 CreateFaultDomain(
  [in]  string                Name,
  [in]  string                FaultDomain,
  [in]  uint32                FaultDomainType,
  [in]  string                Description,
  [in]  string                Location,
  [in]  uint32                Flags,
  [out] MSCluster_FaultDomain CreatedFaultDomain
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the fault domain to create.

</dd> <dt>

*FaultDomain* \[in\]
</dt> <dd>

The parent name of the fault domain.

</dd> <dt>

*FaultDomainType* \[in\]
</dt> <dd>

The type of fault domain.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

The description of the fault domain.

</dd> <dt>

*Location* \[in\]
</dt> <dd>

The location of the fault domain.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Flags

</dd> <dt>

*CreatedFaultDomain* \[out\]
</dt> <dd>

On success, returns a [**MSCluster\_FaultDomain**](mscluster-faultdomain.md) that describes the newly created fault domain.

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

 

 





