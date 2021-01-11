---
description: Pauses the print queue.
ms.assetid: 0f425318-a7c0-4bba-bb44-e7635fa3ca03
ms.tgt_platform: multiple
title: Pause method of the Win32_Printer class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Printer.Pause
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Pause method of the Win32\_Printer class

The **Pause** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method pauses the print queue. No jobs can print until the queue is resumed.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Pause();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the values listed in the following list, or any other value to indicate an error. For additional error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

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



| Requirement | Value |
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

[**Resume method**](resume-method-in-class-win32-printer.md)
</dt> </dl>

 

