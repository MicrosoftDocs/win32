---
description: The ResetPrinter function specifies the data type and device mode values to be used for printing documents submitted by the StartDocPrinter function. These values can be overridden by using the SetJob function after document printing has started.
ms.assetid: 9efc6629-dbb7-4320-90b9-07c66f0add47
title: ResetPrinter function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ResetPrinter
- ResetPrinterA
- ResetPrinterW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# ResetPrinter function

The **ResetPrinter** function specifies the data type and device mode values to be used for printing documents submitted by the [**StartDocPrinter**](startdocprinter.md) function. These values can be overridden by using the [**SetJob**](setjob.md) function after document printing has started.

## Syntax


```C++
BOOL ResetPrinter(
  _In_ HANDLE             hPrinter,
  _In_ LPPRINTER_DEFAULTS pDefault
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

Handle to the printer. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*pDefault* \[in\]
</dt> <dd>

Pointer to a [**PRINTER\_DEFAULTS**](printer-defaults.md) structure.

The **ResetPrinter** function ignores the **DesiredAccess** member of the [**PRINTER\_DEFAULTS**](printer-defaults.md) structure. Set that member to zero.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

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
| Unicode and ANSI names<br/>   | **ResetPrinterW** (Unicode) and **ResetPrinterA** (ANSI)<br/>                                       |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**PRINTER\_DEFAULTS**](printer-defaults.md)
</dt> <dt>

[**StartDocPrinter**](startdocprinter.md)
</dt> <dt>

[**SetJob**](setjob.md)
</dt> </dl>

 

 




