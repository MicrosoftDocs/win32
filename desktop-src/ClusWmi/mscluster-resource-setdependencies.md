---
title: SetDependencies method of the MSCluster\_Resource class
description: Sets the resource dependency expression.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '49e431f0-d2fb-4c85-b52f-ffa3565299fe'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetDependencies method", "SetDependencies method, MSCluster_Resource class", "MSCluster_Resource class, SetDependencies method"]
topic_type:
- apiref
api_name:
- MSCluster_Resource.SetDependencies
api_location:
- ClusWMI.dll
api_type:
- COM
---

# SetDependencies method of the MSCluster\_Resource class

Sets the resource dependency expression.

## Syntax


```mof
void SetDependencies(
  [in] string Expression
);
```



## Parameters

<dl> <dt>

*Expression* \[in\]
</dt> <dd>

The dependency expression that this resource should depend on.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> </dl>

 

 





