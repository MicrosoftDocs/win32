---
description: The SetJob function pauses, resumes, cancels, or restarts a print job on a specified printer. You can also use the SetJob function to set print job parameters, such as the print job priority and the document name.
ms.assetid: 21947c69-c517-4962-8eb7-b45ed4211d9a
title: SetJob function (WinSpool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SetJob
- SetJobA
- SetJobW
api_type: 
- DllExport
api_location: 
- WinSpool.drv
- Ext-MS-Win-Printer-WinSpool-l1-1-2.dll
- Ext-MS-Win-Printer-WinSpool-L1-1-3.dll
---

# SetJob function

The **SetJob** function pauses, resumes, cancels, or restarts a print job on a specified printer. You can also use the **SetJob** function to set print job parameters, such as the print job priority and the document name.

You can use the **SetJob** function to give a command to a print job, or to set print job parameters, or to do both in the same call. The value of the *Command* parameter does not affect how the function uses the *Level* and *pJob* parameters. Also, you can use **SetJob** with [**JOB\_INFO\_3**](job-info-3.md) to link together a set of print jobs. See Remarks for more information.

## Syntax


```C++
BOOL SetJob(
  _In_ HANDLE hPrinter,
  _In_ DWORD  JobId,
  _In_ DWORD  Level,
  _In_ LPBYTE pJob,
  _In_ DWORD  Command
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer object of interest. Use the [**OpenPrinter**](openprinter.md), [**OpenPrinter2**](openprinter2.md), or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*JobId* \[in\]
</dt> <dd>

Identifier that specifies the print job. You obtain a print job identifier by calling the [**AddJob**](addjob.md) function or the [**StartDoc**](/windows/desktop/api/Wingdi/nf-wingdi-startdoca) function.

If the *Level* parameter is set to 3, the *JobId* parameter must match the **JobId** member of the [**JOB\_INFO\_3**](job-info-3.md) structure pointed to by *pJob*

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The type of job information structure pointed to by the *pJob* parameter.

**All versions of Windows**: You can set the *Level* parameter to 0, 1, or 2. When you set *Level* to 0, *pJob* should be **NULL**. Use these values when you are not setting any print job parameters.

You can also set the *Level* parameter to 3.

Starting with **Windows Vista**: You can also set the *Level* parameter to 4.

</dd> <dt>

*pJob* \[in\]
</dt> <dd>

A pointer to a structure that sets the print job parameters.

**All versions of Windows**: *pJob* can point to a [**JOB\_INFO\_1**](job-info-1.md) or [**JOB\_INFO\_2**](job-info-2.md) structure.

*pJob* can also point to a [**JOB\_INFO\_3**](job-info-3.md) structure. You must have **JOB\_ACCESS\_ADMINISTER** access permission for the jobs specified by the **JobId** and **NextJobId** members of the **JOB\_INFO\_3** structure.

Starting with **Windows Vista**: *pJob* can also point to a [**JOB\_INFO\_4**](job-info-4.md) structure.

If the *Level* parameter is 0, *pJob* should be **NULL**.

</dd> <dt>

*Command* \[in\]
</dt> <dd>

The print job operation to perform. This parameter can be one of the following values.



| Value                                                                                                                                                                                                            | Meaning                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <span id="JOB_CONTROL_CANCEL"></span><span id="job_control_cancel"></span><dl> <dt>**JOB\_CONTROL\_CANCEL**</dt> </dl>                                    | Do not use. To delete a print job, use **JOB\_CONTROL\_DELETE**.<br/>        |
| <span id="JOB_CONTROL_PAUSE"></span><span id="job_control_pause"></span><dl> <dt>**JOB\_CONTROL\_PAUSE**</dt> </dl>                                       | Pause the print job.<br/>                                                    |
| <span id="JOB_CONTROL_RESTART"></span><span id="job_control_restart"></span><dl> <dt>**JOB\_CONTROL\_RESTART**</dt> </dl>                                 | Restart the print job. A job can only be restarted if it was printing.<br/>  |
| <span id="JOB_CONTROL_RESUME"></span><span id="job_control_resume"></span><dl> <dt>**JOB\_CONTROL\_RESUME**</dt> </dl>                                    | Resume a paused print job.<br/>                                              |
| <span id="JOB_CONTROL_DELETE"></span><span id="job_control_delete"></span><dl> <dt>**JOB\_CONTROL\_DELETE**</dt> </dl>                                    | Delete the print job.<br/>                                                   |
| <span id="JOB_CONTROL_SENT_TO_PRINTER"></span><span id="job_control_sent_to_printer"></span><dl> <dt>**JOB\_CONTROL\_SENT\_TO\_PRINTER**</dt> </dl>       | Used by port monitors to end the print job.<br/>                             |
| <span id="JOB_CONTROL_LAST_PAGE_EJECTED"></span><span id="job_control_last_page_ejected"></span><dl> <dt>**JOB\_CONTROL\_LAST\_PAGE\_EJECTED**</dt> </dl> | Used by language monitors to end the print job.<br/>                         |
| <span id="JOB_CONTROL_RETAIN"></span><span id="job_control_retain"></span><dl> <dt>**JOB\_CONTROL\_RETAIN**</dt> </dl>                                    | **Windows Vista and later**: Keep the job in the queue after it prints.<br/> |
| <span id="JOB_CONTROL_RELEASE"></span><span id="job_control_release"></span><dl> <dt>**JOB\_CONTROL\_RELEASE**</dt> </dl>                                 | **Windows Vista and later**: Release the print job.<br/>                     |



 

You can use the same call to the **SetJob** function to set print job parameters and to give a command to a print job. Thus, *Command* does not need to be 0 if you are setting print job parameters, although it can be.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

You can use the **SetJob** function to set various print job parameters by supplying a pointer to a [**JOB\_INFO\_1**](job-info-1.md), [**JOB\_INFO\_2**](job-info-2.md), [**JOB\_INFO\_3**](job-info-3.md), or [**JOB\_INFO\_4**](job-info-4.md) structure that contains the necessary data.

To remove or delete all of the print jobs for a particular printer, call the [**SetPrinter**](setprinter.md) function with its *Command* parameter set to **PRINTER\_CONTROL\_PURGE**.

The following members of a [**JOB\_INFO\_1**](job-info-1.md), [**JOB\_INFO\_2**](job-info-2.md), or [**JOB\_INFO\_4**](job-info-4.md) structure are ignored on a call to **SetJob**: **JobId**, **pPrinterName**, **pMachineName**, **pUserName**, **pDrivername**, **Size**, **Submitted**, **Time**, and **TotalPages**.

You must have **PRINTER\_ACCESS\_ADMINISTER** access permission for a printer in order to change a print job's position in the print queue.

If you do not want to set a print job's position in the print queue, you should set the **Position** member of the [**JOB\_INFO\_1**](job-info-1.md), [**JOB\_INFO\_2**](job-info-2.md), or [**JOB\_INFO\_4**](job-info-4.md) structure to **JOB\_POSITION\_UNSPECIFIED**.

Use the **SetJob** function with the [**JOB\_INFO\_3**](job-info-3.md) structure to link together a set of print jobs (also known as a chain). This is useful in situations where a single document consists of several parts that you want to render separately. To print jobs A, B, C, and D in order, call **SetJob** with [**JOB\_INFO\_4**](job-info-4.md) to link A to B, B to C, and C to D.

If you link print jobs, note the following:

-   Jobs can be added to the beginning or end of a chain.
-   All jobs in the chain must have the same data type.
-   The chain must be completely linked before spooling begins, otherwise the spooler may print and delete spooled jobs before you link them all. There are two ways to keep the chain from printing prematurely:

    -   Pause the first job in the chain until the chain is completely linked. The paused state of the first job governs the state of all jobs in the chain.
    -   Keep the first job incomplete, that is, do not call [**EndDoc**](/windows/desktop/api/Wingdi/nf-wingdi-enddoc) or [**ScheduleJob**](schedulejob.md) for the first job. However, if 'print while spooling' is enabled (the default), this method blocks the port while the chain is built, which also prevents the printing of non-related jobs.

-   The application must handle the case where the user deletes a job in the chain before the chain finishes printing. [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns **INVALID\_PARAMETER** when a JobID does not exist.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>WinSpool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>WinSpool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>WinSpool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **SetJobW** (Unicode) and **SetJobA** (ANSI)<br/>                                                   |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddJob**](addjob.md)
</dt> <dt>

[**GetJob**](getjob.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**SetPrinter**](setprinter.md)
</dt> <dt>

[**JOB\_INFO\_1**](job-info-1.md)
</dt> <dt>

[**JOB\_INFO\_2**](job-info-2.md)
</dt> <dt>

[**JOB\_INFO\_3**](job-info-3.md)
</dt> <dt>

[**JOB\_INFO\_4**](job-info-4.md)
</dt> </dl>

 

