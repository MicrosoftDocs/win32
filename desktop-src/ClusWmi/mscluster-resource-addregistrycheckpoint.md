---
title: AddRegistryCheckpoint method of the MSCluster\_Resource class
description: Adds a registry key to the list of keys being checkpointed for the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '757aec20-ea8d-4d1b-911b-f7f1c92abe0d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddRegistryCheckpoint method", "AddRegistryCheckpoint method, MSCluster_Resource class", "MSCluster_Resource class, AddRegistryCheckpoint method"]
topic_type:
- apiref
api_name:
- MSCluster_Resource.AddRegistryCheckpoint
api_location:
- ClusWMI.dll
api_type:
- COM
---

# AddRegistryCheckpoint method of the MSCluster\_Resource class

Adds a registry key to the list of keys being checkpointed for the [resource](https://msdn.microsoft.com/library/aa372152).

## Syntax


```mof
void AddRegistryCheckpoint(
  [in] string CheckpointName
);
```



## Parameters

<dl> <dt>

*CheckpointName* \[in\]
</dt> <dd>

The registry key name at the root of the subtree that should be checkpointed for the resource. This is a key name that is relative to **HKEY\_LOCAL\_MACHINE**, such as **Software**\\**Microsoft**\\*My Application*. Do not use a leading backslash (\) in the relative path or the call will fail.

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

 

 





