---
description: Creates a new printer driver.
ms.assetid: 23d9ec50-235a-4bf8-ab6b-be3509c3869f
ms.tgt_platform: multiple
title: AddPrinterDriver method of the Win32_PrinterDriver class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_PrinterDriver.AddPrinterDriver
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# AddPrinterDriver method of the Win32\_PrinterDriver class

The **AddPrinterDriver** class method creates a new printer driver.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 AddPrinterDriver(
  [in] Win32_PrinterDriver DriverInfo
);
```



## Parameters

<dl> <dt>

*DriverInfo* \[in\]
</dt> <dd>

An instance of the [**Win32\_PrinterDriver**](win32-printerdriver.md) class that represents the printer driver.

</dd> </dl>

## Return value

Returns one of the values listed in the following list or any other value to indicate an error. For values different from those listed in the following list, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants).

<dl> <dt>

**0**
</dt> <dd>

Success.

</dd> <dt>

**5**
</dt> <dd>

Access denied.

</dd> <dt>

**87**
</dt> <dd>

The parameter is incorrect. May occur when the object is not correctly filled or when driver can not be found in the system. Alternately, the name attribute may be different than the model specified in the .inf file. Or, there may be a missing backslash ("\\") on a PathFile attribute.

</dd> <dt>

**1797**
</dt> <dd>

The printer driver is unknown.

</dd> </dl>

## Remarks

> [!Note]  
> When using the **AddPrinterDriver** method you must use **SeLoadDriverPrivilege** to load or unload a device driver.

 

## Examples

The[Install a Printer Driver not Found in Drivers Cab](https://Gallery.TechNet.Microsoft.Com/1aac6333-a794-48d3-b7da-46d87df56ee1) VBScript code example installs a hypothetical printer using a print driver not found in Drivers.cab.

The following VBScript sample installs the printer driver for an Apple LaserWriter 8500 printer.


```VB
strComputer = "." 
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2") 
objWMIService.Security_.Privileges.AddAsString "SeLoadDriverPrivilege", True 
 
Set objDriver = objWMIService.Get("Win32_PrinterDriver") 
 
objDriver.Name = "NewPrinter Model 2900" 
objDriver.SupportedPlatform = "Windows NT x86" 
objDriver.Version = "3" 
objDriver.DriverPath = "C:\Scripts\NewPrinter.dll" 
objDriver.Infname = "C:\Scripts\NewPrinter.inf" 
intResult = objDriver.AddPrinterDriver(objDriver) 
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

[**Win32\_PrinterDriver**](win32-printerdriver.md)
</dt> </dl>

 

