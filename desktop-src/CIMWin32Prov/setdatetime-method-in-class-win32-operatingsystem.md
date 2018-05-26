---
Description: The SetDateTime&\#8194;WMI class method sets the current system time on the computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b9b86a52-c3d7-489d-8632-b297970dbeac
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: SetDateTime method of the Win32\_OperatingSystem class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetDateTime method of the Win32\_OperatingSystem class

The **SetDateTime** [WMI class](https://msdn.microsoft.com/library/aa393244) method sets the current system time on the computer.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

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

Returns zero (0) to indicate success. Any other number indicates an error. For error codes, see [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559) or [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978). For general **HRESULT** values, see [System Error Codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).

<dl> <dt>

**Success** (0)
</dt> <dt>

**Other** (1 4294967295)
</dt> </dl>

## Remarks

The calling process must have the SE\_SYSTEMTIME\_NAME privilege.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[**Win32\_OperatingSystem**](win32-operatingsystem.md)
</dt> <dt>

[WMI Tasks: Desktop Management](https://msdn.microsoft.com/library/aa394591)
</dt> </dl>

 

 




