---
title: Pause method of the MSCluster\_Node class
description: Pauses the cluster activity on a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 35ead07d-f84f-4e0a-a7eb-f0b2bcdf6978
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Pause method
- Pause method, MSCluster_Node class
- MSCluster_Node class, Pause method
topic_type:
- apiref
api_name:
- MSCluster_Node.Pause
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Pause method of the MSCluster\_Node class

Pauses the cluster activity on a node.

## Syntax


```mof
void Pause(
  [in] uint32 DrainType,
  [in] string TargetNode
);
```



## Parameters

<dl> <dt>

*DrainType* \[in\]
</dt> <dd>

The type of drain which to perform.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="Drain"></span><span id="drain"></span><span id="DRAIN"></span>

**Drain** (1)


</dt> <dd></dd> <dt>

<span id="Force_Drain"></span><span id="force_drain"></span><span id="FORCE_DRAIN"></span>

**Force Drain** (2)


</dt> <dd></dd> </dl> </dd> <dt>

*TargetNode* \[in\]
</dt> <dd>

The node which the current workload is moved to.

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

[**MSCluster\_Node**](mscluster-node.md)
</dt> <dt>

[**Pause**](mscluster-node-pause.md)
</dt> </dl>

 

 





