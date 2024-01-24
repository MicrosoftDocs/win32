---
description: The SetDateTime&\#8194;WMI class method sets the current system time on the computer.
ms.assetid: b9b86a52-c3d7-489d-8632-b297970dbeac
ms.tgt_platform: multiple
title: SetDateTime method of the Win32_OperatingSystem class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_OperatingSystem.SetDateTime
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# SetDateTime method of the Win32\_OperatingSystem class

The **SetDateTime** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method sets the current system time on the computer.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 SetDateTime(
  [in] datetime LocalDatetime
);
```



## Parameters

<dl> <dt>

*LocalDatetime* \[in\]
</dt> <dd>

Value of the current time.

</dd> </dl>

## Return value

Returns zero (0) to indicate success. Any other number indicates an error. For error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**Success** (0)
</dt> <dt>

**Other** (1 4294967295)
</dt> </dl>

## Remarks

The calling process must have the SE\_SYSTEMTIME\_NAME privilege.

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

[**Win32\_OperatingSystem**](win32-operatingsystem.md)
</dt> <dt>

[WMI Tasks: Desktop Management](/windows/desktop/WmiSdk/wmi-tasks--desktop-management)
</dt> </dl>

 

