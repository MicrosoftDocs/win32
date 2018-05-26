---
title: GetPossibleOwners method of the MSCluster\_Resource class
description: Gets the list of nodes which can be an owner, host, of this resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: FDEDACB3-D78F-4A80-8B16-BD6177B05B5B
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetPossibleOwners method
- GetPossibleOwners method, MSCluster_Resource class
- MSCluster_Resource class, GetPossibleOwners method
topic_type:
- apiref
api_name:
- MSCluster_Resource.GetPossibleOwners
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetPossibleOwners method of the MSCluster\_Resource class

Gets the list of nodes which can be an owner, host, of this resource.

## Syntax


```mof
void GetPossibleOwners(
  [out] string NodeNames[]
);
```



## Parameters

<dl> <dt>

*NodeNames* \[out\]
</dt> <dd>

The nodes that can be an owner, host, of this resource.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> </dl>

 

 





