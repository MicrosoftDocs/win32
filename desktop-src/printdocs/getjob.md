---
description: The GetJob function retrieves information about a specified print job.
ms.assetid: 57e59f84-d2a0-4722-b0fc-6673f7bb5c57
title: GetJob function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetJob
- GetJobA
- GetJobW
api_type: 
- DllExport
api_location: 
- Winspool.drv
- Ext-MS-Win-Printer-WinSpool-l1-1-2.dll
- Ext-MS-Win-Printer-WinSpool-L1-1-3.dll
---

# GetJob function

The **GetJob** function retrieves information about a specified print job.

## Syntax


```C++
BOOL GetJob(
  _In_  HANDLE  hPrinter,
  _In_  DWORD   JobId,
  _In_  DWORD   Level,
  _Out_ LPBYTE  pJob,
  _In_  DWORD   cbBuf,
  _Out_ LPDWORD pcbNeeded
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer for which the print-job data is retrieved. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*JobId* \[in\]
</dt> <dd>

Identifies the print job for which to retrieve data. Use the [**AddJob**](addjob.md) function or [**StartDoc**](/windows/desktop/api/Wingdi/nf-wingdi-startdoca) function to get a print job identifier.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The type of information returned in the *pJob* buffer. If *Level* is 1, *pJob* receives a [**JOB\_INFO\_1**](job-info-1.md) structure. If *Level* is 2, *pJob* receives a [**JOB\_INFO\_2**](job-info-2.md) structure.

</dd> <dt>

*pJob* \[out\]
</dt> <dd>

A pointer to a buffer that receives a [**JOB\_INFO\_1**](job-info-1.md) or a [**JOB\_INFO\_2**](job-info-2.md) structure containing information about the job. The buffer must be large enough to store the strings pointed to by the structure members.

To determine the required buffer size, call **GetJob** with *cbBuf* set to zero. **GetJob** fails, [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns ERROR\_INSUFFICIENT\_BUFFER, and the *pcbNeeded* parameter returns the size, in bytes, of the buffer required to hold the array of structures and their data.

</dd> <dt>

*cbBuf* \[in\]
</dt> <dd>

The size, in bytes, of the array.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

A pointer to a value that specifies the number of bytes copied if the function succeeds or the number of bytes required if *cbBuf* is too small.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **GetJobW** (Unicode) and **GetJobA** (ANSI)<br/>                                                   |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddJob**](addjob.md)
</dt> <dt>

[**JOB\_INFO\_1**](job-info-1.md)
</dt> <dt>

[**JOB\_INFO\_2**](job-info-2.md)
</dt> <dt>

[**ScheduleJob**](schedulejob.md)
</dt> <dt>

[**SetJob**](setjob.md)
</dt> </dl>

 

