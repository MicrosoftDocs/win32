---
description: The DeletePrinterDataEx function deletes a specified value from the configuration data for a printer.
ms.assetid: bcc9cdb3-0fbf-40b6-9de2-1479c3c0ff55
title: DeletePrinterDataEx function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeletePrinterDataEx
- DeletePrinterDataExA
- DeletePrinterDataExW
api_type: 
- DllExport
api_location: 
- Winspool.drv
- Ext-MS-Win-printer-Winspool-l1-1-1.dll
- Ext-MS-Win-Printer-WinSpool-l1-1-2.dll
- Ext-MS-Win-Printer-WinSpool-L1-1-3.dll
---

# DeletePrinterDataEx function

The **DeletePrinterDataEx** function deletes a specified value from the configuration data for a printer. A printer's configuration data consists of a set of named and typed values stored in a hierarchy of registry keys. The function deletes a specified value under a specified key.

Like the [**DeletePrinterData**](deleteprinterdata.md) function, **DeletePrinterDataEx** can delete values stored by the [**SetPrinterData**](setprinterdata.md) function. In addition, **DeletePrinterDataEx** can delete values stored under a specified key by the [**SetPrinterDataEx**](setprinterdataex.md) function.

## Syntax


```C++
DWORD DeletePrinterDataEx(
  _In_ HANDLE  hPrinter,
  _In_ LPCTSTR pKeyName,
  _In_ LPCTSTR pValueName
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer for which the function deletes a value. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*pKeyName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the key containing the value to delete. Use the backslash ( \\ ) character as a delimiter to specify a path that has one or more subkeys.

If *pKeyName* is **NULL** or an empty string, **DeletePrinterDataEx** returns ERROR\_INVALID\_PARAMETER.

</dd> <dt>

*pValueName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the value to delete.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a system error code.

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
| Unicode and ANSI names<br/>   | **DeletePrinterDataExW** (Unicode) and **DeletePrinterDataExA** (ANSI)<br/>                         |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**DeletePrinterKey**](deleteprinterkey.md)
</dt> <dt>

[**EnumPrinterDataEx**](enumprinterdataex.md)
</dt> <dt>

[**EnumPrinterKey**](enumprinterkey.md)
</dt> <dt>

[**GetPrinterDataEx**](getprinterdataex.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**SetPrinterDataEx**](setprinterdataex.md)
</dt> </dl>

 

 




