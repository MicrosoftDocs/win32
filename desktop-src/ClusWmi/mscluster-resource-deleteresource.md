---
title: DeleteResource method of the MSCluster\_Resource class
description: Deletes a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '79566882-460a-4ba6-b049-5fdf80ff8331'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DeleteResource method", "DeleteResource method, MSCluster_Resource class", "MSCluster_Resource class, DeleteResource method"]
topic_type:
- apiref
api_name:
- MSCluster_Resource.DeleteResource
api_location:
- ClusWMI.dll
api_type:
- COM
---

# DeleteResource method of the MSCluster\_Resource class

Deletes a [resource](https://msdn.microsoft.com/library/aa372152).

## Syntax


```mof
void DeleteResource(
  [in] uint32 Options
);
```



## Parameters

<dl> <dt>

*Options* \[in\]
</dt> <dd>

Any options which to perform while deleting the resource.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (1)


</dt> <dd></dd> <dt>

<span id="PerformCleanup"></span><span id="performcleanup"></span><span id="PERFORMCLEANUP"></span>

**PerformCleanup** (2)


</dt> <dd></dd> </dl> </dd> </dl>

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

 

 





