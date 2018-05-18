---
title: GetPreferredOwners method of the MSCluster\_ResourceGroup class
description: Get the list of preferred owners for this resource group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'FAC5DD83-2D6B-4997-B7D3-629B1EAFF983'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetPreferredOwners method", "GetPreferredOwners method, MSCluster_ResourceGroup class", "MSCluster_ResourceGroup class, GetPreferredOwners method"]
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup.GetPreferredOwners
api_location:
- ClusWMI.dll
api_type:
- COM
---

# GetPreferredOwners method of the MSCluster\_ResourceGroup class

Get the list of preferred owners for this resource group.

## Syntax


```mof
void GetPreferredOwners(
  [out] string NodeNames[]
);
```



## Parameters

<dl> <dt>

*NodeNames* \[out\]
</dt> <dd>

Node names in order of preference that can be owners of this resource group.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)
</dt> </dl>

 

 





