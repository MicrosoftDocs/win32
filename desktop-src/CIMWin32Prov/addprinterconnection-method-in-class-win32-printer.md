---
Description: Provides a connection to an existing printer on the network, and adds it to the list of available printers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 44149051-4abf-4428-8999-355dd0b0ce69
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: AddPrinterConnection method of the Win32_Printer class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Printer.AddPrinterConnection
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# AddPrinterConnection method of the Win32\_Printer class

The **AddPrinterConnection** [WMI class](https://msdn.microsoft.com/library/aa393244) method provides a connection to an existing printer on the network, and adds it to the list of available printers.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 AddPrinterConnection(
  [in] string Name
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Friendly name for the printer.

</dd> </dl>

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

</dd> <dt>

**1801**
</dt> <dd>

Invalid Printer Name

</dd> <dt>

**1930**
</dt> <dd>

Incompatible Printer Driver

</dd> </dl>

## Examples

The [Add-PrinterDriver](https://Gallery.TechNet.Microsoft.Com/1c8f4c0d-9439-4af0-8840-59686d9b4bc1) PowerShell sample installs all printer drivers from a specified print server.

The [ListSharedPrintersAddPrintConnection.ps1](https://Gallery.TechNet.Microsoft.Com/b7f74333-e78b-49d8-b23a-f1307d5b1ee6) PowerShell sample lists shared printers on a remote comptuer, and gives you the ability to add a printer connection from the remote computer to your computer.

The following VBScript code sample adds a local printer.


```VB
Dim strPrinterName as String = "Isidoros Printer"
Dim strComputer AsString = My.Computer.Name
Dim objWMIService, objPrinter AsObject
objWMIService = GetObject(
"winmgmts:" _

& 
"{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")

objPrinter = objWMIService.Get(
"Win32_Printer").SpawnInstance_
objPrinter.Name = strPrinterName
objPrinter.DriverName = "Generic / Text Only"
objPrinter.PortName = 
"c:\temp\file.prn"
objPrinter.DeviceID = strPrinterName
'objPrinter.Location = "Athens, Greece"
objPrinter.Network = 
False
objPrinter.Shared = 
False'objPrinter.ShareName = "MyShareName"
objPrinter.Put_()
```



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

[WMI Tasks: Printers and Printing](https://msdn.microsoft.com/library/aa394598)
</dt> <dt>

[**Win32\_Printer**](win32-printer.md)
</dt> </dl>

 

 




