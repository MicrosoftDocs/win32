---
title: SetFaultDomain method of the MSCluster\_FaultDomain class
description: Changes settings on a fault domain object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 541b2d94-a634-4216-9f52-3638ec40f8c0
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetFaultDomain method
- SetFaultDomain method, MSCluster_FaultDomain class
- MSCluster_FaultDomain class, SetFaultDomain method
topic_type:
- apiref
api_name:
- MSCluster_FaultDomain.SetFaultDomain
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetFaultDomain method of the MSCluster\_FaultDomain class

Changes settings on a fault domain object.

## Syntax


```mof
uint32 SetFaultDomain(
  [in] string NewName,
  [in] string FaultDomain,
  [in] string Description,
  [in] string Location,
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*NewName* \[in\]
</dt> <dd>

The new name of the fault domain. Pass in **Null** to keep the current value.

</dd> <dt>

*FaultDomain* \[in\]
</dt> <dd>

The new parent of the fault domain. Pass in **Null** to keep the current value.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

The new description of the fault domain. Pass in **Null** to keep the current value.

</dd> <dt>

*Location* \[in\]
</dt> <dd>

The new location of the fault domain. Pass in **Null** to keep the current value.

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

 

 





