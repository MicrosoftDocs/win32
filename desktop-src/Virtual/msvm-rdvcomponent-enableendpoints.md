---
title: EnableEndPoints method of the Msvm\_RdvComponent class
description: Requests the Remote Desktop Services Virtual Device to Start a Pipe connection with the virtual machine.
ms.assetid: '16590d10-6307-437d-a3bb-6cf8c86c75d9'
keywords: ["EnableEndPoints method Hyper-V", "EnableEndPoints method Hyper-V , Msvm_RdvComponent class", "Msvm_RdvComponent class Hyper-V , EnableEndPoints method"]
topic_type:
- apiref
api_name:
- Msvm_RdvComponent.EnableEndPoints
api_location:
- Root\virtualization
api_type:
- COM
---

# EnableEndPoints method of the Msvm\_RdvComponent class

Requests the Remote Desktop Services Virtual Device to Start a Pipe connection with the virtual machine.

## Syntax


```mof
uint32 EnableEndPoints();
```



## Parameters

This method has no parameters.

## Return value

If zero (0) is returned, then the operation was successful. Any other return code indicates an error condition.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**Out of memory** (32774)
</dt> <dt>

**File not found** (32775)
</dt> <dt>

 (32776)
</dt> <dt>

 (32777)
</dt> <dt>

 (32778)
</dt> <dt>

 (32779)
</dt> <dt>

 (32780)
</dt> <dt>

 (32781)
</dt> <dt>

 (32782)
</dt> </dl>

## Requirements



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_RdvComponent**](msvm-rdvcomponent.md)
</dt> </dl>

 

 





