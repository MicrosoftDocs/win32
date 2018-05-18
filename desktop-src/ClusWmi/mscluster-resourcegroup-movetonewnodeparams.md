---
title: MoveToNewNodeParams method of the MSCluster\_ResourceGroup class
description: Move the resource group to different node with the parameters specified as a raw buffer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'D05F635A-E957-45AB-A4F0-986987B3DD5B'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MoveToNewNodeParams method", "MoveToNewNodeParams method, MSCluster_ResourceGroup class", "MSCluster_ResourceGroup class, MoveToNewNodeParams method"]
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup.MoveToNewNodeParams
api_location:
- ClusWMI.dll
api_type:
- COM
---

# MoveToNewNodeParams method of the MSCluster\_ResourceGroup class

Move the resource group to different node with the parameters specified as a raw buffer.

## Syntax


```mof
void MoveToNewNodeParams(
  [in] string NodeName,
  [in] uint8  Parameters[],
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*NodeName* \[in\]
</dt> <dd>

Name of the node to move to or **NULL** to move to any node.

</dd> <dt>

*Parameters* \[in\]
</dt> <dd>

Parameters for the resource group move.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Flags for the resource group move.

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

 

 





