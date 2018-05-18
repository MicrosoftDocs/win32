---
title: AddVirtualMachine method of the MSCluster\_Cluster class
description: Adds an existing virtual machine to the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '424CDD44-DCF1-4D13-B45C-CC8BD3DED6B4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddVirtualMachine method", "AddVirtualMachine method, MSCluster_Cluster interface", "MSCluster_Cluster interface, AddVirtualMachine method"]
topic_type:
- apiref
api_name:
- MSCluster_Cluster.AddVirtualMachine
api_location:
- ClusWMI.dll
api_type:
- COM
---

# AddVirtualMachine method of the MSCluster\_Cluster class

Adds an existing virtual machine to the cluster.

## Syntax


```mof
void AddVirtualMachine(
  [in] String VirtualMachine
);
```



## Parameters

<dl> <dt>

*VirtualMachine* \[in\]
</dt> <dd>

The virtual machine to add.

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

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> </dl>

 

 





