---
description: The GetSpoolFileHandle function retrieves a handle for the spool file associated with the job currently submitted by the application.
ms.assetid: df6f28b3-66a6-4fb7-bdde-40cd7d934c5f
title: GetSpoolFileHandle function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetSpoolFileHandle
- GetSpoolFileHandleA
- GetSpoolFileHandleW
api_type: 
- DllExport
api_location: 
- WinSpool.drv
---

# GetSpoolFileHandle function

The **GetSpoolFileHandle** function retrieves a handle for the spool file associated with the job currently submitted by the application.

## Syntax


```C++
HANDLE GetSpoolFileHandle(
  _In_ HANDLE hPrinter
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer to which the job was submitted. This should be the same handle that was used to submit the job. (Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.)

</dd> </dl>

## Return value

If the function succeeds, it returns a handle to the spool file.

If the function fails, it returns **INVALID\_HANDLE\_VALUE**.

## Remarks

With the handle to the spool file, your application can write to the spool file with calls to [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile) followed by [**CommitSpoolData**](commitspooldata.md).

Your application must not call [**ClosePrinter**](closeprinter.md) on *hPrinter* until after it has accessed the spool file for the last time. Then it should call [**CloseSpoolFileHandle**](closespoolfilehandle.md) followed by **ClosePrinter**. Attempts to access the spool file handle after the original *hPrinter* has been closed will fail even if the file handle itself has not been closed. **CloseSpoolFileHandle** will itself fail if **ClosePrinter** is called first.

This function will fail if it is called before the print job has finished spooling.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>WinSpool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **GetSpoolFileHandleW** (Unicode) and **GetSpoolFileHandleA** (ANSI)<br/>                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**AddPrinter**](addprinter.md)
</dt> <dt>

[**ClosePrinter**](closeprinter.md)
</dt> <dt>

[**CloseSpoolFileHandle**](closespoolfilehandle.md)
</dt> <dt>

[**CommitSpoolData**](commitspooldata.md)
</dt> </dl>

 

