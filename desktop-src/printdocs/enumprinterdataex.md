---
description: The EnumPrinterDataEx function enumerates all value names and data for a specified printer and key.
ms.assetid: bc5ecc46-24a4-4b54-9431-0eaf6446e2d6
title: EnumPrinterDataEx function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EnumPrinterDataEx
- EnumPrinterDataExA
- EnumPrinterDataExW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# EnumPrinterDataEx function

The **EnumPrinterDataEx** function enumerates all value names and data for a specified printer and key.

Printer data is stored in the registry. While enumerating printer data, do not call registry functions that might change the data.

## Syntax


```C++
DWORD EnumPrinterDataEx(
  _In_  HANDLE  hPrinter,
  _In_  LPCTSTR pKeyName,
  _Out_ LPBYTE  pEnumValues,
  _In_  DWORD   cbEnumValues,
  _Out_ LPDWORD pcbEnumValues,
  _Out_ LPDWORD pnEnumValues
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer for which the function retrieves configuration data. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*pKeyName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the key containing the values to enumerate. Use the backslash ( \\ ) character as a delimiter to specify a path with one or more subkeys. **EnumPrinterDataEx** enumerates all values of the key, but does not enumerate values of subkeys of the specified key. Use the [**EnumPrinterKey**](enumprinterkey.md) function to enumerate subkeys.

If *pKeyName* is **NULL** or an empty string, **EnumPrinterDataEx** returns ERROR\_INVALID\_PARAMETER.

</dd> <dt>

*pEnumValues* \[out\]
</dt> <dd>

A pointer to a buffer that receives an array of [**PRINTER\_ENUM\_VALUES**](printer-enum-values.md) structures. Each structure contains the value name, type, data, and sizes of a value under the key.

</dd> <dt>

*cbEnumValues* \[in\]
</dt> <dd>

The size, in bytes, of the buffer pointed to by *pcbEnumValues*. If you set *cbEnumValues* to zero, the *pcbEnumValues* parameter returns the required buffer size.

</dd> <dt>

*pcbEnumValues* \[out\]
</dt> <dd>

A pointer to a variable that receives the size, in bytes, of the retrieved configuration data. If the buffer size specified by *cbEnumValues* is too small, the function returns ERROR\_MORE\_DATA and *pcbEnumValues* indicates the required buffer size.

</dd> <dt>

*pnEnumValues* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of [**PRINTER\_ENUM\_VALUES**](printer-enum-values.md) structures returned in *pEnumValues*.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a system error code.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

**EnumPrinterDataEx** retrieves printer configuration data set by the [**SetPrinterDataEx**](setprinterdataex.md) and [**SetPrinterData**](setprinterdata.md) functions.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **EnumPrinterDataExW** (Unicode) and **EnumPrinterDataExA** (ANSI)<br/>                             |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**DeletePrinterDataEx**](deleteprinterdataex.md)
</dt> <dt>

[**EnumPrinterKey**](enumprinterkey.md)
</dt> <dt>

[**GetPrinterDataEx**](getprinterdataex.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**PRINTER\_ENUM\_VALUES**](printer-enum-values.md)
</dt> <dt>

[**SetPrinterData**](setprinterdata.md)
</dt> <dt>

[**SetPrinterDataEx**](setprinterdataex.md)
</dt> </dl>

 

 




