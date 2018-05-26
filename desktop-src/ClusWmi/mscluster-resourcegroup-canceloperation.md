---
title: CancelOperation method of the MSCluster\_ResourceGroup class
description: Cancels any pending operations on the resource group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: FA40FDE4-C779-4B81-87B6-F41273607CAD
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CancelOperation method
- CancelOperation method, MSCluster_ResourceGroup class
- MSCluster_ResourceGroup class, CancelOperation method
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup.CancelOperation
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CancelOperation method of the MSCluster\_ResourceGroup class

Cancels any pending operations on the resource group.

## Syntax


```mof
void CancelOperation(
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*Flags* \[in\]
</dt> <dd>

Any flags for the cancel operation.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\MSCluster<br/>                                                                |
| Header<br/>                   | <dl> <dt>Deviceaccess.h</dt> </dl> |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl>    |



## See also

<dl> <dt>

[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)
</dt> </dl>

 

 





