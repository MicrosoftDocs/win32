---
description: Requests the Remote Desktop Services virtual device to start a pipe connection with the virtual machine.
ms.assetid: e53238ee-8264-416b-8855-193c28089cfa
title: EnableEndPoints method of the Msvm_RdvComponent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_RdvComponent.EnableEndPoints
api_type: 
- COM
api_location: 
- vmms.exe
---

# EnableEndPoints method of the Msvm\_RdvComponent class

Requests the Remote Desktop Services virtual device to start a pipe connection with the virtual machine.

## Syntax


```mof
uint32 EnableEndPoints();
```



## Parameters

This method has no parameters.

## Return value

This method returns one of the following values.

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



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_RdvComponent**](msvm-rdvcomponent.md)
</dt> </dl>

 

 




