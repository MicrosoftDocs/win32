---
title: MoveToNewNode method of the MSCluster\_ResourceGroup class
description: Moves the group to a different node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c597c189-d140-494c-89ba-4fe66d23992d
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MoveToNewNode method
- MoveToNewNode method, MSCluster_ResourceGroup class
- MSCluster_ResourceGroup class, MoveToNewNode method
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup.MoveToNewNode
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MoveToNewNode method of the MSCluster\_ResourceGroup class

Moves the [group](https://msdn.microsoft.com/library/aa369645) to a different [node](https://msdn.microsoft.com/library/aa371745).

## Syntax


```mof
void MoveToNewNode(
  [in] string NodeName,
  [in] uint32 TimeOut
);
```



## Parameters

<dl> <dt>

*NodeName* \[in\]
</dt> <dd>

The target node.

</dd> <dt>

*TimeOut* \[in\]
</dt> <dd>

The length of time, in seconds that the method should wait for the resource to move to the new node.

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

 

 





