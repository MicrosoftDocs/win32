---
description: The CloseSpoolFileHandle function closes a handle to a spool file associated with the print job currently submitted by the application.
ms.assetid: e2c0e68f-b72e-4a97-ba18-8943bc5789c1
title: CloseSpoolFileHandle function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CloseSpoolFileHandle
api_type: 
- DllExport
api_location: 
- WinSpool.drv
---

# CloseSpoolFileHandle function

The **CloseSpoolFileHandle** function closes a handle to a spool file associated with the print job currently submitted by the application.

## Syntax


```C++
BOOL CloseSpoolFileHandle(
  _In_ HANDLE hPrinter,
  _In_ HANDLE hSpoolFile
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer to which the job was submitted. This should be the same handle that was used to obtain *hSpoolFile* with [**GetSpoolFileHandle**](getspoolfilehandle.md).

</dd> <dt>

*hSpoolFile* \[in\]
</dt> <dd>

A handle to the spool file being closed. If [**CommitSpoolData**](commitspooldata.md) has not been called since [**GetSpoolFileHandle**](getspoolfilehandle.md) was called, then this should be the same handle that was returned by **GetSpoolFileHandle**. Otherwise, it should be the handle that was returned by the most recent call to **CommitSpoolData**.

</dd> </dl>

## Return value

**TRUE**, if it succeeds, **FALSE** otherwise.

## Remarks

Your application must not call [**ClosePrinter**](closeprinter.md) on *hPrinter* until after it has accessed the spool file for the last time. Then it should call **CloseSpoolFileHandle** followed by **ClosePrinter**. Attempts to access the spool file handle after the original *hPrinter* has been closed will fail even if the file handle itself has not been closed. **CloseSpoolFileHandle** will fail if **ClosePrinter** is called first.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>WinSpool.drv</dt> </dl>                   |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**ClosePrinter**](closeprinter.md)
</dt> <dt>

[**GetSpoolFileHandle**](getspoolfilehandle.md)
</dt> </dl>

 

 




