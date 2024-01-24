---
description: The ReadPrinter function retrieves data from the specified printer.
ms.assetid: d7c3f186-c53e-424b-89bf-6742babb998f
title: ReadPrinter function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ReadPrinter
api_type: 
- DllExport
api_location: 
- Spoolss.dll
---

# ReadPrinter function

The **ReadPrinter** function retrieves data from the specified printer.

## Syntax


```C++
BOOL ReadPrinter(
  _In_  HANDLE  hPrinter,
  _Out_ LPVOID  pBuf,
  _In_  DWORD   cbBuf,
  _Out_ LPDWORD pNoBytesRead
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer object for which to retrieve data. Use the [**OpenPrinter**](openprinter.md) function to retrieve a printer object handle. Use the format: Printername, Job xxxx.

</dd> <dt>

*pBuf* \[out\]
</dt> <dd>

A pointer to a buffer that receives the printer data.

</dd> <dt>

*cbBuf* \[in\]
</dt> <dd>

The size, in bytes, of the buffer to which *pBuf* points.

</dd> <dt>

*pNoBytesRead* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of bytes of data copied into the array to which *pBuf* points.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

**ReadPrinter** returns an error if the device or the printer is not bidirectional.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Spoolss.dll</dt> </dl>                    |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> </dl>

 

 




