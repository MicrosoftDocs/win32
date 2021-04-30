---
description: Initiates an operating system shutdown operation on the associated child virtual machine. If zero (0) is returned, then the shutdown was initiated successfully. Any other return code indicates an error condition.
ms.assetid: 946BBC62-5479-4AE0-8870-D0A07827B902
title: InitiateShutdown method of the Msvm_ShutdownComponent class (Winreg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ShutdownComponent.InitiateShutdown
api_type: 
- COM
api_location: 
- vmms.exe
---

# InitiateShutdown method of the Msvm\_ShutdownComponent class

Initiates an operating system shutdown operation on the associated child virtual machine. If zero (0) is returned, then the shutdown was initiated successfully. Any other return code indicates an error condition.

## Syntax


```mof
uint32 InitiateShutdown(
  [in] boolean Force,
  [in] string  Reason
);
```



## Parameters

<dl> <dt>

*Force* \[in\]
</dt> <dd>

Type: **boolean**

A flag which, if **True**, forces applications to be closed despite having unsaved data.

</dd> <dt>

*Reason* \[in\]
</dt> <dd>

Type: **string**

The reason for the shutdown operation. This is a user-defined string.

</dd> </dl>

## Return value

Type: **uint32**

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

## Remarks

Access to the [**Msvm\_ShutdownComponent**](msvm-shutdowncomponent.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| Header<br/>                   | <dl> <dt>Winreg.h</dt> </dl>                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_ShutdownComponent**](msvm-shutdowncomponent.md)
</dt> </dl>

 

