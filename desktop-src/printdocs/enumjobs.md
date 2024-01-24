---
description: The EnumJobs function retrieves information about a specified set of print jobs for a specified printer.
ms.assetid: 1cf429ea-b40e-4063-b6de-c43b7b87f3d3
title: EnumJobs function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EnumJobs
- EnumJobsA
- EnumJobsW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# EnumJobs function

The **EnumJobs** function retrieves information about a specified set of print jobs for a specified printer.

## Syntax


```C++
BOOL EnumJobs(
  _In_  HANDLE  hPrinter,
  _In_  DWORD   FirstJob,
  _In_  DWORD   NoJobs,
  _In_  DWORD   Level,
  _Out_ LPBYTE  pJob,
  _In_  DWORD   cbBuf,
  _Out_ LPDWORD pcbNeeded,
  _Out_ LPDWORD pcReturned
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer object whose print jobs the function enumerates. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*FirstJob* \[in\]
</dt> <dd>

The zero-based position within the print queue of the first print job to enumerate. For example, a value of 0 specifies that enumeration should begin at the first print job in the print queue; a value of 9 specifies that enumeration should begin at the tenth print job in the print queue.

</dd> <dt>

*NoJobs* \[in\]
</dt> <dd>

The total number of print jobs to enumerate.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The type of information returned in the *pJob* buffer.



| Value                                                                                                | Meaning                                                                              |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | *pJob* receives an array of [**JOB\_INFO\_1**](job-info-1.md) structures<br/> |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | *pJob* receives an array of [**JOB\_INFO\_2**](job-info-2.md) structures<br/> |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | *pJob* receives an array of [**JOB\_INFO\_3**](job-info-3.md) structures<br/> |



 

</dd> <dt>

*pJob* \[out\]
</dt> <dd>

A pointer to a buffer that receives an array of [**JOB\_INFO\_1**](job-info-1.md), [**JOB\_INFO\_2**](job-info-2.md), or [**JOB\_INFO\_3**](job-info-3.md) structures. The buffer must be large enough to receive the array of structures and any strings or other data to which the structure members point.

To determine the required buffer size, call **EnumJobs** with *cbBuf* set to zero. **EnumJobs** fails, [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns ERROR\_INSUFFICIENT\_BUFFER, and the *pcbNeeded* parameter returns the size, in bytes, of the buffer required to hold the array of structures and their data.

</dd> <dt>

*cbBuf* \[in\]
</dt> <dd>

The size, in bytes, of the *pJob* buffer.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of bytes copied if the function succeeds. If the function fails, the variable receives the number of bytes required.

</dd> <dt>

*pcReturned* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of [**JOB\_INFO\_1**](job-info-1.md), [**JOB\_INFO\_2**](job-info-2.md), or [**JOB\_INFO\_3**](job-info-3.md) structures returned in the *pJob* buffer.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The [**JOB\_INFO\_1**](job-info-1.md) structure contains general print-job information; the [**JOB\_INFO\_2**](job-info-2.md) structure has much more detailed information. The [**JOB\_INFO\_3**](job-info-3.md) structure contains information about how jobs are linked.

To determine the number of print jobs in the printer queue, call the [**GetPrinter**](getprinter.md) function with the *Level* parameter set to 2.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **EnumJobsW** (Unicode) and **EnumJobsA** (ANSI)<br/>                                               |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**GetJob**](getjob.md)
</dt> <dt>

[**GetPrinter**](getprinter.md)
</dt> <dt>

[**JOB\_INFO\_1**](job-info-1.md)
</dt> <dt>

[**JOB\_INFO\_2**](job-info-2.md)
</dt> <dt>

[**JOB\_INFO\_3**](job-info-3.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**SetJob**](setjob.md)
</dt> </dl>

 

