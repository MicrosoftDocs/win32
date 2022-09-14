---
description: The SetDefaultPrinter WMI class method sets the default system printer for the user calling the method.
ms.assetid: 7e896961-363d-4b8b-9d22-bbfc9681e97b
ms.tgt_platform: multiple
title: SetDefaultPrinter method of the Win32_Printer class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Printer.SetDefaultPrinter
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# SetDefaultPrinter method of the Win32\_Printer class

The **SetDefaultPrinter** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method sets the default system printer for the user calling the method.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 SetDefaultPrinter();
```



## Parameters

This method has no parameters.

## Return value

Returns 0 (zero) if successful, and some other value if an error occurs. For additional error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

## Examples

The [Install a TCP/IP Printer Port and Printer](https://Gallery.TechNet.Microsoft.Com/41a4c996-b7f7-4d58-808d-2acac20ddbf7) VBScript sample installs a TCP/IP printer port, installs a printer, and then sets the printer to be default.

The following VBScript code sample sets the default printer on a computer.


```VB
strComputer = "." 
Set objWMIService = GetObject("winmgmts:" _ 
    & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2") 
 
Set colInstalledPrinters =  objWMIService.ExecQuery _ 
    ("Select * from Win32_Printer Where Name = 'ScriptedPrinter'") 
 
For Each objPrinter in colInstalledPrinters 
    objPrinter.SetDefaultPrinter() 
Next 
```



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

[WMI Tasks: Printers and Printing](/windows/desktop/WmiSdk/wmi-tasks--printers-and-printing)
</dt> <dt>

[**Win32\_Printer**](win32-printer.md)
</dt> </dl>

 

