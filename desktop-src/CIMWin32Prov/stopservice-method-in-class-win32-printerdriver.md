---
Description: Places the service represented by the Win32\_PrinterDriver object in the stopped state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0e730fe6-ff9f-4866-a255-be6d372f2d7d
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: StopService method of the Win32_PrinterDriver class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_PrinterDriver.StopService
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# StopService method of the Win32\_PrinterDriver class

The **StopService** [WMI class](https://msdn.microsoft.com/library/aa393244) method places the service represented by the [**Win32\_PrinterDriver**](win32-printerdriver.md) object in the stopped state.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 StopService();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the values listed in the following list or any other value to indicate an error. For values different from those listed in the following list, see [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

<dl> <dt>

**0**
</dt> <dd>

Service successfully stopped.

</dd> <dt>

**1**
</dt> <dd>

Request not supported.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                        |
| Header<br/>                   | <dl> <dt>Sdoias.h</dt> </dl>           |
| MOF<br/>                      | <dl> <dt>Win32\_Printer.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl>       |



## See also

<dl> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> <dt>

[**Win32\_PrinterDriver**](win32-printerdriver.md)
</dt> </dl>

 

 




