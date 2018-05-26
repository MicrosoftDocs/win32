---
title: MoveToNewNodeEx method of the MSCluster\_ResourceGroup class
description: Move the resource group to a different node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: A196B129-D787-4900-968C-EBFFDA3CF45C
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MoveToNewNodeEx method
- MoveToNewNodeEx method, MSCluster_ResourceGroup class
- MSCluster_ResourceGroup class, MoveToNewNodeEx method
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup.MoveToNewNodeEx
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MoveToNewNodeEx method of the MSCluster\_ResourceGroup class

Move the resource group to a different node.

## Syntax


```mof
void MoveToNewNodeEx(
  [in] string             NodeName,
  [in] MSCluster_Property Parameters,
  [in] uint32             Flags
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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)
</dt> <dt>

[**MSCluster\_Property**](mscluster-property.md)
</dt> </dl>

 

 





