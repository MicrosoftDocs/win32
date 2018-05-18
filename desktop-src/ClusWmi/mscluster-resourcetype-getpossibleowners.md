---
title: GetPossibleOwners method of the MSCluster\_ResourceType class
description: Gets the possible owners of this resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'DF534A52-EAA3-4C18-BFB3-8D0F300475DD'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetPossibleOwners method", "GetPossibleOwners method, MSCluster_ResourceType class", "MSCluster_ResourceType class, GetPossibleOwners method"]
topic_type:
- apiref
api_name:
- MSCluster_ResourceType.GetPossibleOwners
api_location:
- ClusWMI.dll
api_type:
- COM
---

# GetPossibleOwners method of the MSCluster\_ResourceType class

Gets the possible owners of this resource type.

## Syntax


```mof
void GetPossibleOwners(
  [out] string NodeNames[]
);
```



## Parameters

<dl> <dt>

*NodeNames* \[out\]
</dt> <dd>

The nodes that can host this resource type.

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

[**MSCluster\_ResourceType**](mscluster-resourcetype.md)
</dt> </dl>

 

 





