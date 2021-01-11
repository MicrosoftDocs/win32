---
description: The CommitSpoolData function notifies the print spooler that a specified amount of data has been written to a specified spool file and is ready to be rendered.
ms.assetid: cb8899e0-2fdf-4928-adff-17ef5af39f63
title: CommitSpoolData function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CommitSpoolData
api_type: 
- DllExport
api_location: 
- WinSpool.drv
---

# CommitSpoolData function

The **CommitSpoolData** function notifies the print spooler that a specified amount of data has been written to a specified spool file and is ready to be rendered.

## Syntax


```C++
HANDLE CommitSpoolData(
  _In_ HANDLE hPrinter,
  _In_ HANDLE hSpoolFile,
       DWORD  cbCommit
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

A handle to the spool file being changed. On the first call of **CommitSpoolData**, this should be the same handle that was returned by [**GetSpoolFileHandle**](getspoolfilehandle.md). Subsequent calls to **CommitSpoolData** should pass the handle returned by the preceding call. See Remarks.

</dd> <dt>

*cbCommit* 
</dt> <dd>

The number of bytes committed to the print spooler.

</dd> </dl>

## Return value

If the function succeeds, it returns a handle to the spool file.

If the function fails, it returns INVALID\_HANDLE\_VALUE.

## Remarks

Applications submitting a spooler print job can call [**GetSpoolFileHandle**](getspoolfilehandle.md) and then directly write data to the spool file handle by calling [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile). To notify the print spooler that the file contains data which is ready to be rendered, the application must call **CommitSpoolData** and provide the number of available bytes.

If **CommitSpoolData** is called multiple times, each call must use the spool file handle returned by the previous call. When no more data will be written to the spool file, [**CloseSpoolFileHandle**](closespoolfilehandle.md) should be called for the file handle returned by the last call to **CommitSpoolData**.

Before calling **CommitSpoolData**, applications must set the file pointer to the position it had before it wrote data to the file. In the process of rendering the data in the spooler file, the print spooler will move the spool file pointer *cbCommit* bytes from the current value of file pointer.

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

[**GetSpoolFileHandle**](getspoolfilehandle.md)
</dt> <dt>

[**CloseSpoolFileHandle**](closespoolfilehandle.md)
</dt> </dl>

 

