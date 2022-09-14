---
description: The FlushPrinter function sends a buffer to the printer in order to clear it from a transient state.
ms.assetid: 08e54175-da68-4ebd-91ec-8f4525f49d30
title: FlushPrinter function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FlushPrinter
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# FlushPrinter function

The **FlushPrinter** function sends a buffer to the printer in order to clear it from a transient state.

## Syntax


```C++
BOOL FlushPrinter(
  _In_  HANDLE  hPrinter,
  _In_  LPVOID  pBuf,
  _In_  DWORD   cbBuf,
  _Out_ LPDWORD pcWritten,
  _In_  DWORD   cSleep
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer object. This should be the same handle that was used, in a prior [**WritePrinter**](writeprinter.md) call, by the printer driver.

</dd> <dt>

*pBuf* \[in\]
</dt> <dd>

A pointer to an array of bytes that contains the data to be written to the printer.

</dd> <dt>

*cbBuf* \[in\]
</dt> <dd>

The size, in bytes, of the array pointed to by *pBuf*.

</dd> <dt>

*pcWritten* \[out\]
</dt> <dd>

A pointer to a value that receives the number of bytes of data that were written to the printer.

</dd> <dt>

*cSleep* \[in\]
</dt> <dd>

The time, in milliseconds, for which the I/O line to the printer port should be kept idle.

</dd> </dl>

## Return value

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

**FlushPrinter** should be called only if [**WritePrinter**](writeprinter.md) failed, leaving the printer in a transient state. For example, the printer could get into a transient state when the job gets aborted and the printer driver has partially sent some raw data to the printer.

**FlushPrinter** also can specify an idle period during which the print spooler does not schedule any jobs to the corresponding printer port.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**WritePrinter**](writeprinter.md)
</dt> </dl>

 

 




