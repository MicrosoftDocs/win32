---
description: The StartDocPrinter function notifies the print spooler that a document is to be spooled for printing.
ms.assetid: caa2bd80-4af3-4968-a5b9-d12f16cac6fc
title: StartDocPrinter function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- StartDocPrinter
- StartDocPrinterA
- StartDocPrinterW
api_type: 
- DllExport
api_location: 
- Winspool.drv
- Ext-MS-Win-Printer-WinSpool-l1-1-2.dll
- Ext-MS-Win-Printer-WinSpool-L1-1-3.dll
---

# StartDocPrinter function

The **StartDocPrinter** function notifies the print spooler that a document is to be spooled for printing.

## Syntax


```C++
DWORD StartDocPrinter(
  _In_ HANDLE hPrinter,
  _In_ DWORD  Level,
  _In_ LPBYTE pDocInfo
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The version of the structure to which *pDocInfo* points. This value must be 1.

</dd> <dt>

*pDocInfo* \[in\]
</dt> <dd>

A pointer to a [**DOC\_INFO\_1**](doc-info-1.md) structure that describes the document to print.

</dd> </dl>

## Return value

If the function succeeds, the return value identifies the print job.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The typical sequence for a print job is as follows:

1.  To begin a print job, call **StartDocPrinter**.
2.  To begin each page, call [**StartPagePrinter**](startpageprinter.md).
3.  To write data to a page, call [**WritePrinter**](writeprinter.md).
4.  To end each page, call [**EndPagePrinter**](endpageprinter.md).
5.  Repeat 2, 3, and 4 for as many pages as necessary.
6.  To end the print job, call [**EndDocPrinter**](enddocprinter.md).

Note that calling [**StartPagePrinter**](startpageprinter.md) and [**EndPagePrinter**](endpageprinter.md) may not be necessary, such as if the print data type includes the page information.

When a page in a spooled file exceeds approximately 350 MB, it can fail to print and not send an error message. For example, this can occur when printing large EMF files. The page size limit depends on many factors including the amount of virtual memory available, the amount of memory allocated by calling processes, and the amount of fragmentation in the process heap.

## Examples

For a sample program that uses this function, see [How To: Print Using the GDI Print API](how-to--print-using-the-gdi-print-api.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **StartDocPrinterW** (Unicode) and **StartDocPrinterA** (ANSI)<br/>                                 |



## See also

<dl> <dt>

[**AddJob**](addjob.md)
</dt> <dt>

[**DOC\_INFO\_1**](doc-info-1.md)
</dt> <dt>

[**DOC\_INFO\_2**](doc-info-2.md)
</dt> <dt>

[**EndDocPrinter**](enddocprinter.md)
</dt> <dt>

[**EndPagePrinter**](endpageprinter.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**StartDocPrinter**](startdocprinter.md)
</dt> <dt>

[**StartPagePrinter**](startpageprinter.md)
</dt> <dt>

[**WritePrinter**](writeprinter.md)
</dt> </dl>

 

 




