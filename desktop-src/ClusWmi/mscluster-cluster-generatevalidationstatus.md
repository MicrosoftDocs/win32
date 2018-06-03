---
title: GenerateValidationStatus method of the MSCluster\_Cluster class
description: Creates an MSCluster\_ValidationStatus instance bound to the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3E79AFF7-7CA4-4425-AFA3-A8F8BAC85F2F
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GenerateValidationStatus method
- GenerateValidationStatus method, MSCluster_Cluster interface
- MSCluster_Cluster interface, GenerateValidationStatus method
topic_type:
- apiref
api_name:
- MSCluster_Cluster.GenerateValidationStatus
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GenerateValidationStatus method of the MSCluster\_Cluster class

Creates an [**MSCluster\_ValidationStatus**](mscluster-validationstatus.md) instance bound to the cluster.

## Syntax


```mof
void GenerateValidationStatus(
  [out] MSCluster_ValidationStatus REF Status
);
```



## Parameters

<dl> <dt>

*Status* \[out\]
</dt> <dd>

A [**MSCluster\_ValidationStatus**](mscluster-validationstatus.md) containing the validation status of the cluster.

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

 

 





