---
title: GetChildren method of the MSCluster\_FaultDomain class
description: Retrieves the children of the fault domain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 55a14bdf-8291-4238-a635-7e5e6a5cc4b4
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetChildren method
- GetChildren method, MSCluster_FaultDomain class
- MSCluster_FaultDomain class, GetChildren method
topic_type:
- apiref
api_name:
- MSCluster_FaultDomain.GetChildren
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetChildren method of the MSCluster\_FaultDomain class

Retrieves the children of the fault domain.

## Syntax


```mof
uint32 GetChildren(
  [out] MSCluster_FaultDomain Children[],
  [in]  uint32                Flags
);
```



## Parameters

<dl> <dt>

*Children* \[out\]
</dt> <dd>

On success, returns a collection of [**MSCluster\_FaultDomain**](mscluster-faultdomain.md) that describes the children of the fault domain.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Flags

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

[**MSCluster\_FaultDomain**](mscluster-faultdomain.md)
</dt> </dl>

 

 





