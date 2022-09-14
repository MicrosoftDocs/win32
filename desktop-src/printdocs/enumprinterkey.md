---
description: The EnumPrinterKey function enumerates the subkeys of a specified key for a specified printer.
ms.assetid: 721b1d23-a594-4439-b8f9-9b11be5fe874
title: EnumPrinterKey function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EnumPrinterKey
- EnumPrinterKeyA
- EnumPrinterKeyW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# EnumPrinterKey function

The **EnumPrinterKey** function enumerates the subkeys of a specified key for a specified printer.

Printer data is stored in the registry. While enumerating printer data, do not call registry functions that might change the data.

## Syntax


```C++
DWORD EnumPrinterKey(
  _In_  HANDLE  hPrinter,
  _In_  LPCTSTR pKeyName,
  _Out_ LPTSTR  pSubkey,
  _In_  DWORD   cbSubkey,
  _Out_ LPDWORD pcbSubkey
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer for which the function enumerates subkeys. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*pKeyName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the key containing the subkeys to enumerate. Use the backslash '\\' character as a delimiter to specify a path with one or more subkeys. **EnumPrinterKey** enumerates all subkeys of the key, but does not enumerate the subkeys of those subkeys.

If *pKeyName* is an empty string (""), **EnumPrinterKey** enumerates the top-level key for the printer. If *pKeyName* is **NULL**, **EnumPrinterKey** returns ERROR\_INVALID\_PARAMETER.

</dd> <dt>

*pSubkey* \[out\]
</dt> <dd>

A pointer to a buffer that receives an array of null-terminated subkey names. The array is terminated by two null characters.

</dd> <dt>

*cbSubkey* \[in\]
</dt> <dd>

The size, in bytes, of the buffer pointed to by *pSubkey*. If you set *cbSubkey* to zero, the *pcbSubkey* parameter returns the required buffer size.

</dd> <dt>

*pcbSubkey* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of bytes retrieved in the *pSubkey* buffer. If the buffer size specified by *cbSubkey* is too small, the function returns ERROR\_MORE\_DATA and *pcbSubkey* indicates the required buffer size.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a system error code. If *pKeyName* does not exist, the return value is ERROR\_FILE\_NOT\_FOUND.

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
| Unicode and ANSI names<br/>   | **EnumPrinterKeyW** (Unicode) and **EnumPrinterKeyA** (ANSI)<br/>                                   |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**DeletePrinterDataEx**](deleteprinterdataex.md)
</dt> <dt>

[**GetPrinterDataEx**](getprinterdataex.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**SetPrinterDataEx**](setprinterdataex.md)
</dt> </dl>

 

 




