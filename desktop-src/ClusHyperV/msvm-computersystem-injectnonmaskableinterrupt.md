---
title: InjectNonMaskableInterrupt method of the Msvm\_ComputerSystem class
description: Injects a non-maskable interrupt into the virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '724110dd-fb26-43d3-863c-8674f4be3fd4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["InjectNonMaskableInterrupt method", "InjectNonMaskableInterrupt method, Msvm_ComputerSystem class", "Msvm_ComputerSystem class, InjectNonMaskableInterrupt method"]
topic_type:
- apiref
api_name:
- Msvm_ComputerSystem.InjectNonMaskableInterrupt
api_location:
- VMMS.exe
api_type:
- COM
---

# InjectNonMaskableInterrupt method of the Msvm\_ComputerSystem class

Injects a non-maskable interrupt into the virtual machine.

## Syntax


```mof
uint32 InjectNonMaskableInterrupt(
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Access Denied** (32769)
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

[**Msvm\_ComputerSystem**](msvm-computersystem.md)
</dt> </dl>

 

 





