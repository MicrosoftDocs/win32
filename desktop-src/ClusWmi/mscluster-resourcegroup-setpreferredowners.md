---
title: SetPreferredOwners method of the MSCluster\_ResourceGroup class
description: Sets the preferred owner list for this resource group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 33325c63-979a-409d-beed-8ffeb47d1ac6
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetPreferredOwners method
- SetPreferredOwners method, MSCluster_ResourceGroup class
- MSCluster_ResourceGroup class, SetPreferredOwners method
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup.SetPreferredOwners
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetPreferredOwners method of the MSCluster\_ResourceGroup class

Sets the preferred owner list for this resource [group](https://msdn.microsoft.com/library/aa369645).

## Syntax


```mof
void SetPreferredOwners(
  [in] string NodeNames[]
);
```



## Parameters

<dl> <dt>

*NodeNames* \[in\]
</dt> <dd>

Node names, in order of preference, that can be owners of this resource group.

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

[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)
</dt> </dl>

 

 





