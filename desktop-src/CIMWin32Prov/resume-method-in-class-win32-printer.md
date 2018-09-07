---
Description: Resumes a paused print queue.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6d6d21e9-f469-4e2c-9a89-3e9febe229fc
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Resume method of the Win32_Printer class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Printer.Resume
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Resume method of the Win32\_Printer class

The **Resume** [WMI class](https://msdn.microsoft.com/library/aa393244) method resumes a paused print queue.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Resume();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the values listed in the following list, or any other value to indicate an error. For additional error codes, see [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559) or [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978). For general **HRESULT** values, see [System Error Codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).

<dl> <dt>

**0**
</dt> <dd>

Success

</dd> <dt>

**5**
</dt> <dd>

Access Denied

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                        |
| MOF<br/>                      | <dl> <dt>Win32\_Printer.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl>       |



## See also

<dl> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> <dt>

[**Win32\_Printer**](win32-printer.md)
</dt> <dt>

[**Pause Method**](pause-method-in-class-win32-printer.md)
</dt> </dl>

 

 




