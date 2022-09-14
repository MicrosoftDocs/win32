---
description: The DeletePrinterDriver function removes the specified printer-driver name from the list of names of supported drivers on a server.
ms.assetid: b159bd8b-3416-44a5-91bf-c0447ed6b465
title: DeletePrinterDriver function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeletePrinterDriver
- DeletePrinterDriverA
- DeletePrinterDriverW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# DeletePrinterDriver function

The **DeletePrinterDriver** function removes the specified printer-driver name from the list of names of supported drivers on a server.

To delete the files associated with the driver in addition to removing the specified printer-driver name from the list of names of supported drivers for a server, use the [**DeletePrinterDriverEx**](deleteprinterdriverex.md) function.

**DeletePrinterDriver** deletes a driver only if no version of the driver is in use for the specified environment. [**DeletePrinterDriverEx**](deleteprinterdriverex.md) can delete specific versions of the driver.

## Syntax


```C++
BOOL DeletePrinterDriver(
  _In_ LPTSTR pName,
  _In_ LPTSTR pEnvironment,
  _In_ LPTSTR pDriverName
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the server from which the driver is to be deleted. If this parameter is **NULL**, the printer-driver name will be removed locally.

</dd> <dt>

*pEnvironment* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the environment from which the driver is to be deleted (for example, Windows x86, Windows IA64, or Windows x64). If this parameter is **NULL**, the driver name is deleted from the current environment of the calling application and client machine (not of the destination application and print server).

</dd> <dt>

*pDriverName* \[in\]
</dt> <dd>

A pointer to a null-terminated string specifying the name of the driver that should be deleted.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The caller must have the [SeLoadDriverPrivilege](/windows/desktop/SecAuthZ/authorization-constants).

The **DeletePrinterDriver** function does not delete the associated files, it merely removes the driver name from the list returned by the [**EnumPrinterDrivers**](enumprinterdrivers.md) function.

Before calling **DeletePrinterDriver**, you must delete all printer objects that use the printer driver.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **DeletePrinterDriverW** (Unicode) and **DeletePrinterDriverA** (ANSI)<br/>                         |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**DeletePrinterDriverEx**](deleteprinterdriverex.md)
</dt> <dt>

[**EnumPrinterDrivers**](enumprinterdrivers.md)
</dt> </dl>

 

