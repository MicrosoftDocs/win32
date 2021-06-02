---
description: The EnumPrintProcessorDatatypes function enumerates the data types that a specified print processor supports.
ms.assetid: 27b6e074-d303-446b-9e5f-6cfa55c30d26
title: EnumPrintProcessorDatatypes function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EnumPrintProcessorDatatypes
- EnumPrintProcessorDatatypesA
- EnumPrintProcessorDatatypesW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# EnumPrintProcessorDatatypes function

The **EnumPrintProcessorDatatypes** function enumerates the data types that a specified print processor supports.

## Syntax


```C++
BOOL EnumPrintProcessorDatatypes(
  _In_  LPTSTR  pName,
  _In_  LPTSTR  pPrintProcessorName,
  _In_  DWORD   Level,
  _Out_ LPBYTE  pDatatypes,
  _In_  DWORD   cbBuf,
  _Out_ LPDWORD pcbNeeded,
  _Out_ LPDWORD pcReturned
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the server on which the print processor resides. If this parameter is **NULL**, the data types for the local print processor are enumerated.

</dd> <dt>

*pPrintProcessorName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the print processor whose data types are enumerated.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The type of information returned in the *pDatatypes* buffer. This parameter must be 1.

</dd> <dt>

*pDatatypes* \[out\]
</dt> <dd>

A pointer to a buffer that receives an array of [**DATATYPES\_INFO\_1**](datatypes-info-1.md) structures. Each structure describes an available data type. The buffer must be large enough to receive the array of structures and any strings or other data to which the structure members point.

To determine the required buffer size, call **EnumPrintProcessorDatatypes** with *cbBuf* set to zero. **EnumPrintProcessorDatatypes** fails, [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns ERROR\_INSUFFICIENT\_BUFFER, and the *pcbNeeded* parameter returns the size, in bytes, of the buffer required to hold the array of structures and their data.

</dd> <dt>

*cbBuf* \[in\]
</dt> <dd>

The size, in bytes, of the buffer pointed to by *pDatatypes*.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of bytes copied to the *pDatatypes* buffer if the function succeeds. If the buffer is too small, the function fails and the variable receives the number of bytes required.

</dd> <dt>

*pcReturned* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of structures returned in the *pDatatypes* buffer. This is the number of supported data types.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

v

Starting with Windows Vista, the data type information from remote print servers is retrieved from a local cache.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **EnumPrintProcessorDatatypesW** (Unicode) and **EnumPrintProcessorDatatypesA** (ANSI)<br/>         |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**DATATYPES\_INFO\_1**](datatypes-info-1.md)
</dt> <dt>

[**EnumPrintProcessors**](enumprintprocessors.md)
</dt> </dl>

 

