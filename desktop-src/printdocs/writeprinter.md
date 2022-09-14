---
description: The WritePrinter function notifies the print spooler that data should be written to the specified printer.
ms.assetid: 9411b71f-d686-44ed-9051-d410e5ab228e
title: WritePrinter function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WritePrinter
api_type: 
- DllExport
api_location: 
- Spoolss.dll
- Ext-MS-Win-Printer-WinSpool-l1-1-2.dll
- WinSpool.Drv
- Ext-MS-Win-Printer-WinSpool-L1-1-3.dll
---

# WritePrinter function

The **WritePrinter** function notifies the print spooler that data should be written to the specified printer.

> [!Note]  
> **WritePrinter** only supports GDI printing and must not be used for XPS printing. If your print job uses the XPS or the OpenXPS print path, then use the [XPS Print API](/windows/desktop/printdocs/xps-printing). Sending XPS or OpenXPS print jobs to the spooler using **WritePrinter** is not supported and can result in undetermined results.

 

## Syntax


```C++
BOOL WritePrinter(
  _In_  HANDLE  hPrinter,
  _In_  LPVOID  pBuf,
  _In_  DWORD   cbBuf,
  _Out_ LPDWORD pcWritten
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*pBuf* \[in\]
</dt> <dd>

A pointer to an array of bytes that contains the data that should be written to the printer.

</dd> <dt>

*cbBuf* \[in\]
</dt> <dd>

The size, in bytes, of the array.

</dd> <dt>

*pcWritten* \[out\]
</dt> <dd>

A pointer to a value that receives the number of bytes of data that were written to the printer.

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
3.  To write data to a page, call **WritePrinter**.
4.  To end each page, call [**EndPagePrinter**](endpageprinter.md).
5.  Repeat 2, 3, and 4 for as many pages as necessary.
6.  To end the print job, call [**EndDocPrinter**](enddocprinter.md).

When a high-level document (such as an Adobe PDF or Microsoft Word file) or other printer data (such PCL, PS, or HPGL) is sent directly to a printer, the print settings defined in the document take precedent over Windows print settings. Documents output when the value of the *pDatatype* member of the [**DOC\_INFO\_1**](doc-info-1.md) structure that was passed in the *pDocInfo* parameter of the [**StartDocPrinter**](startdocprinter.md) call is "RAW" must fully describe the [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea)-style print job settings in the language understood by the hardware.

In versions of Windows prior to Windows XP, when a page in a spooled file exceeds approximately 350 MB, it can fail to print and not send an error message. For example, this can occur when printing large EMF files. The page size limit in versions of Windows prior to Windows XP depends on many factors including the amount of virtual memory available, the amount of memory allocated by calling processes, and the amount of fragmentation in the process heap. In Windows XP and later versions of Windows, EMF files must be 2GB or less in size. If **WritePrinter** is used to write non EMF data, such as printer-ready PDL, the size of the file is limited only by the available disk space.

## Examples

For a sample program that uses this function, see [How To: Print Using the GDI Print API](how-to--print-using-the-gdi-print-api.md).

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

 

