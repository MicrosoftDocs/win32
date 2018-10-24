---
Description: Starts the debugger that is currently registered for this process.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 63c30db8-6117-4353-9132-4f39c72a6637
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: AttachDebugger method of the Win32_Process class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Process.AttachDebugger
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# AttachDebugger method of the Win32\_Process class

The **AttachDebugger** [WMI class](https://msdn.microsoft.com/library/aa393244) method starts the debugger that is currently registered for this process.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 AttachDebugger();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the values listed in the following list or any other value to indicate an error. For additional error codes, see [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559) or [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978). For general **HRESULT** values, see [System Error Codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).

<dl> <dt>

**Successful completion**
</dt> <dd>

0

Successful completion.

</dd> <dt>

**Access denied**
</dt> <dd>

2

The user does not have access to the requested information.

</dd> <dt>

**Insufficient privilege**
</dt> <dd>

3

The user does not have sufficient privilege.

</dd> <dt>

**Unknown failure**
</dt> <dd>

8

Unknown failure.

</dd> <dt>

**Path not found**
</dt> <dd>

9

The path specified does not exist.

</dd> <dt>

**Invalid parameter**
</dt> <dd>

21

The specified parameter is not valid.

</dd> <dt>

**Other**
</dt> <dd>

22 4294967295

</dd> </dl>

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

[**Win32\_Process**](win32-process.md)
</dt> </dl>

 

 




