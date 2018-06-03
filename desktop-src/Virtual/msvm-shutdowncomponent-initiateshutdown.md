---
title: InitiateShutdown method of the Msvm\_ShutdownComponent class
description: Initiates an operating system shutdown operation on the associated child virtual machine. If zero (0) is returned, then the shutdown was initiated successfully. Any other return code indicates an error condition.
ms.assetid: 96b08031-19e5-42ae-b3cb-5fe87ff45bb0
keywords:
- InitiateShutdown method Hyper-V
- InitiateShutdown method Hyper-V , Msvm_ShutdownComponent class
- Msvm_ShutdownComponent class Hyper-V , InitiateShutdown method
topic_type:
- apiref
api_name:
- Msvm_ShutdownComponent.InitiateShutdown
api_location:
- winreg.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

A flag which, if **TRUE**, forces applications to be closed despite having unsaved data.

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

Access to the [**Msvm\_ShutdownComponent**](msvm-shutdowncomponent.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| Header<br/>                   | <dl> <dt>Winreg.h</dt> </dl>                  |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_ShutdownComponent**](msvm-shutdowncomponent.md)
</dt> </dl>

 

 





