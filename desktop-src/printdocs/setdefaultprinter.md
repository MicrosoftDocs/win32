---
description: The SetDefaultPrinter function sets the printer name of the default printer for the current user on the local computer.
ms.assetid: 55eec548-577f-422b-80e3-8b23aa4d2159
title: SetDefaultPrinter function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SetDefaultPrinter
- SetDefaultPrinterA
- SetDefaultPrinterW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# SetDefaultPrinter function

The **SetDefaultPrinter** function sets the printer name of the default printer for the current user on the local computer.

## Syntax


```C++
BOOL SetDefaultPrinter(
  _In_ LPCTSTR pszPrinter
);
```



## Parameters

<dl> <dt>

*pszPrinter* \[in\]
</dt> <dd>

A pointer to a null-terminated string containing the default printer name. For a remote printer connection, the name format is **\\\\***server***\\***printername*. For a local printer, the name format is *printername*.

If this parameter is **NULL** or an empty string, that is, "", **SetDefaultPrinter** will select a default printer from one of the installed printers. If a default printer already exists, calling **SetDefaultPrinter** with a **NULL** or an empty string in this parameter might change the default printer.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

When using this method, you must specify a valid printer, driver, and port. If they are invalid, the APIs do not fail but the result is not defined. This could cause other programs to set the printer back to the previous valid printer. You can use [**EnumPrinters**](enumprinters.md) to retrieve the printer name, driver name, and port name of all available printers.

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **SetDefaultPrinterW** (Unicode) and **SetDefaultPrinterA** (ANSI)<br/>                             |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**EnumPrinters**](enumprinters.md)
</dt> <dt>

[**GetDefaultPrinter**](getdefaultprinter.md)
</dt> </dl>

 

 




