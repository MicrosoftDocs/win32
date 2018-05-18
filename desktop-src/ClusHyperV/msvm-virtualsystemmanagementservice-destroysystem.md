---
title: DestroySystem method of the Msvm\_VirtualSystemManagementService class
description: Deletes a virtual system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2925ed81-9ca6-488f-9952-f9799b925e21'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DestroySystem method", "DestroySystem method, Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class, DestroySystem method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.DestroySystem
api_location:
- VMMS.exe
api_type:
- COM
---

# DestroySystem method of the Msvm\_VirtualSystemManagementService class

Deletes a virtual system. The specified virtual system is deleted, including any elements scoped by it. The virtual resources of the deleted virtual system are returned to their resource pools, which, depending on the implementation may imply the deletion of those resources. If the virtual system is active when the operation is invoked, it is first deactivated and then deleted. If snapshots were created from the virtual system, they are also deleted.

## Syntax


```mof
uint32 DestroySystem(
  [in]  CIM_ComputerSystem REF AffectedSystem,
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*AffectedSystem* \[in\]
</dt> <dd>

A reference to the [**CIM\_ComputerSystem**](cim-computersystem.md) that represents the virtual system to delete.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Invalid Parameter** (4)
</dt> <dt>

**Invalid State** (5)
</dt> <dt>

**DMTF Reserved** (6–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





