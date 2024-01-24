---
description: Initiates an operating system reboot operation on the associated child virtual machine.
ms.assetid: 9f3ebbaf-ee0f-4c01-8f73-1f37c08a0feb
title: InitiateReboot method of the Msvm_ShutdownComponent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ShutdownComponent.InitiateReboot
api_type: 
- COM
api_location: 
- vmms.exe
---

# InitiateReboot method of the Msvm\_ShutdownComponent class

Initiates an operating system reboot operation on the associated child virtual machine.

If zero (0) is returned, then the reboot was initiated successfully. Any other return code indicates an error condition.

## Syntax


```mof
uint32 InitiateReboot(
  [in] boolean Force,
  [in] string  Reason
);
```



## Parameters

<dl> <dt>

*Force* \[in\]
</dt> <dd>

A flag which, if TRUE, forces applications to be closed despite having unsaved data.

</dd> <dt>

*Reason* \[in\]
</dt> <dd>

The reason for the reboot operation. This is a user-defined string.

</dd> </dl>

## Return value

This method returns one of the following values:

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

**System is in used** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> <dt>

**File not found** (32779)
</dt> <dt>

**The system is not ready** (32780)
</dt> <dt>

**The machine is locked and cannot be shut down without the force option** (32781)
</dt> <dt>

**A system shutdown is in progress** (32782)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_ShutdownComponent**](msvm-shutdowncomponent.md)
</dt> </dl>

 

 




