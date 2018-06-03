---
title: GetGroups method of the MSCluster\_GroupSet class
description: Gets the groups that are providers for the group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b03facdd-819f-43dc-821a-5c9cdd330d54
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetGroups method
- GetGroups method, MSCluster_GroupSet class
- MSCluster_GroupSet class, GetGroups method
topic_type:
- apiref
api_name:
- MSCluster_GroupSet.GetGroups
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetGroups method of the MSCluster\_GroupSet class

Gets the groups that are providers for the group.

## Syntax


```mof
uint32 GetGroups(
  [in]  string DependentGroup,
  [in]  string ProviderGroup,
  [out] string Groups[]
);
```



## Parameters

<dl> <dt>

*DependentGroup* \[in\]
</dt> <dd>

The name of the group to find the providers of.

</dd> <dt>

*ProviderGroup* \[in\]
</dt> <dd>

The name of the group to find the dependents of.

</dd> <dt>

*Groups* \[out\]
</dt> <dd>

On success, returns the providers for the group.

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

[**MSCluster\_GroupSet**](mscluster-groupset.md)
</dt> </dl>

 

 





