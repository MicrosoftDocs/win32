---
description: The EnumPrinterData function enumerates configuration data for a specified printer.
ms.assetid: 0a4c8436-46fe-4e21-8d55-c5031a3d1b38
title: EnumPrinterData function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EnumPrinterData
- EnumPrinterDataA
- EnumPrinterDataW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# EnumPrinterData function

The **EnumPrinterData** function enumerates configuration data for a specified printer.

To retrieve the configuration data in a single call, use the [**EnumPrinterDataEx**](enumprinterdataex.md) function.

## Syntax


```C++
DWORD EnumPrinterData(
  _In_  HANDLE  hPrinter,
  _In_  DWORD   dwIndex,
  _Out_ LPTSTR  pValueName,
  _In_  DWORD   cbValueName,
  _Out_ LPDWORD pcbValueName,
  _Out_ LPDWORD pType,
  _Out_ LPBYTE  pData,
  _In_  DWORD   cbData,
  _Out_ LPDWORD pcbData
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer whose configuration data is to be obtained. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*dwIndex* \[in\]
</dt> <dd>

An index value that specifies the configuration data value to retrieve.

Set this parameter to zero for the first call to **EnumPrinterData** for a specified printer handle. Then increment the parameter by one for subsequent calls involving the same printer, until the function returns ERROR\_NO\_MORE\_ITEMS. See the following Remarks section for further information.

If you use the technique mentioned in the descriptions of the *cbValueName* and *cbData* parameters to obtain adequate buffer size values, setting both those parameters to zero in a first call to **EnumPrinterData** for a specified printer handle, the value of *dwIndex* does not matter for that call. Set *dwIndex* to zero in the next call to **EnumPrinterData** to start the actual enumeration process.

Configuration data values are not ordered. New values will have an arbitrary index. This means that the **EnumPrinterData** function may return values in any order.

</dd> <dt>

*pValueName* \[out\]
</dt> <dd>

A pointer to a buffer that receives the name of the configuration data value, including a terminating null character.

</dd> <dt>

*cbValueName* \[in\]
</dt> <dd>

The size, in bytes, of the buffer pointed to by *pValueName*.

If you want to have the operating system supply an adequate buffer size, set both this parameter and the *cbData* parameter to zero for the first call to **EnumPrinterData** for a specified printer handle. When the function returns, the variable pointed to by *pcbValueName* will contain a buffer size that is large enough to successfully enumerate all of the printer's configuration data value names.

</dd> <dt>

*pcbValueName* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of bytes stored into the buffer pointed to by *pValueName*.

</dd> <dt>

*pType* \[out\]
</dt> <dd>

A pointer to a variable that receives a code indicating the type of data stored in the specified value. For a list of the possible type codes, see [Registry Value Types](/windows/desktop/SysInfo/registry-value-types). The *pType* parameter can be **NULL** if the type code is not required.

</dd> <dt>

*pData* \[out\]
</dt> <dd>

A pointer to a buffer that receives the configuration data value.

This parameter can be **NULL** if the configuration data value is not required.

</dd> <dt>

*cbData* \[in\]
</dt> <dd>

The size, in bytes, of the buffer pointed to by *pData*.

If you want to have the operating system supply an adequate buffer size, set both this parameter and the *cbValueName* parameter to zero for the first call to **EnumPrinterData** for a specified printer handle. When the function returns, the variable pointed to by *pcbData* will contain a buffer size that is large enough to successfully enumerate all of the printer's configuration data value names.

</dd> <dt>

*pcbData* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of bytes stored into the buffer pointed to by *pData*.

This parameter can be **NULL** if *pData* is **NULL**.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a system error code.

The function returns ERROR\_NO\_MORE\_ITEMS when there are no more configuration data values to retrieve for a specified printer handle.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

**EnumPrinterData** retrieves printer configuration data set by the [**SetPrinterData**](setprinterdata.md) function. A printer's configuration data consists of a set of named and typed values. The **EnumPrinterData** function obtains one of these values, and its name and a type code, each time you call it. Call the **EnumPrinterData** function several times in succession to obtain all of a printer's configuration data values.

Printer configuration data is stored in the registry. While enumerating printer configuration data, you should avoid calling registry functions that might change that data.

If you want to have the operating system supply an adequate buffer size, first call **EnumPrinterData** with both the *cbValueName* and *cbData* parameters set to zero, as noted earlier in the Parameters section. The value of *dwIndex* does not matter for this call. When the function returns, \**pcbValueName* and \**pcbData* will contain buffer sizes that are large enough to enumerate all of the printer's configuration data value names and values. On the next call, allocate value name and data buffers, set *cbValueName* and *cbData* to the sizes in bytes of the allocated buffers, and set *dwIndex* to zero. Thereafter, continue to call the **EnumPrinterData** function, incrementing *dwIndex* by one each time, until the function returns ERROR\_NO\_MORE\_ITEMS.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **EnumPrinterDataW** (Unicode) and **EnumPrinterDataA** (ANSI)<br/>                                 |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**DeletePrinterData**](deleteprinterdata.md)
</dt> <dt>

[**EnumPrinterDataEx**](enumprinterdataex.md)
</dt> <dt>

[**GetPrinterData**](getprinterdata.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**SetPrinter**](setprinter.md)
</dt> <dt>

[**SetPrinterData**](setprinterdata.md)
</dt> </dl>

 

