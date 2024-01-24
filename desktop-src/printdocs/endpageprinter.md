---
description: The EndPagePrinter function notifies the print spooler that the application is at the end of a page in a print job.
ms.assetid: aceb88b9-375b-4cd2-996a-c369f590154e
title: EndPagePrinter function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EndPagePrinter
api_type: 
- DllExport
api_location: 
- Spoolss.dll
---

# EndPagePrinter function

The **EndPagePrinter** function notifies the print spooler that the application is at the end of a page in a print job.

## Syntax


```C++
BOOL EndPagePrinter(
  _In_ HANDLE hPrinter
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

Handle to the printer for which the page will be concluded. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The sequence for a print job is as follows:

1.  To begin a print job, call [**StartDocPrinter**](startdocprinter.md).
2.  To begin each page, call [**StartPagePrinter**](startpageprinter.md).
3.  To write data to a page, call [**WritePrinter**](writeprinter.md).
4.  To end each page, call **EndPagePrinter**.
5.  Repeat 2, 3, and 4 for as many pages as necessary.
6.  To end the print job, call [**EndDocPrinter**](enddocprinter.md).

When a page in a spooled file exceeds approximately 350 MB, it can fail to print and not send an error message. For example, this can occur when printing large EMF files. The page size limit depends on many factors including the amount of virtual memory available, the amount of memory allocated by calling processes, and the amount of fragmentation in the process heap.

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

[**EndDocPrinter**](enddocprinter.md)
</dt> <dt>

[**EndPagePrinter**](endpageprinter.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**StartDocPrinter**](startdocprinter.md)
</dt> <dt>

[**StartPagePrinter**](startpageprinter.md)
</dt> <dt>

[**WritePrinter**](writeprinter.md)
</dt> </dl>

 

 




