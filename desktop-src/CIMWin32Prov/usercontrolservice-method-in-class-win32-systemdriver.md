---
description: Attempts to send a user-defined control code to a service managed by a system driver.
ms.assetid: 62e66c35-f264-43d0-9e94-fb5e85f936e0
ms.tgt_platform: multiple
title: UserControlService method of the Win32_SystemDriver class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_SystemDriver.UserControlService
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# UserControlService method of the Win32\_SystemDriver class

The **UserControlService** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method attempts to send a user-defined control code to a service managed by a system driver.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 UserControlService(
  [in] uint8 ControlCode
);
```



## Parameters

<dl> <dt>

*ControlCode* \[in\]
</dt> <dd>

Specifies defined values (from 128 to 255) that provide control commands specific to a user.

</dd> </dl>

## Return value

Returns a value of 0 (zero) if the **UserControlService** request was accepted, 1 (one) if the request is not supported, and any other number to indicate an error.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> <dt>

[**Win32\_SystemDriver**](win32-systemdriver.md)
</dt> </dl>

 

