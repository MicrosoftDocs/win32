---
description: The ScheduleJob function requests that the print spooler schedule a specified print job for printing.
ms.assetid: a103a29c-be4d-491e-9b04-84571fe969a5
title: ScheduleJob function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ScheduleJob
api_type: 
- DllExport
api_location: 
- Spoolss.dll
---

# ScheduleJob function

The **ScheduleJob** function requests that the print spooler schedule a specified print job for printing.

## Syntax


```C++
BOOL ScheduleJob(
  _In_ HANDLE hPrinter,
  _In_ DWORD  dwJobID
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer for the print job. This must be a local printer that is configured as a spooled printer. If *hPrinter* is a handle to a remote printer connection, or if the printer is configured for direct printing, the **ScheduleJob** function fails. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

*hPrinter* must be the same printer handle specified in the call to [**AddJob**](addjob.md) that obtained the *dwJobID* print job identifier.

</dd> <dt>

*dwJobID* \[in\]
</dt> <dd>

The print job to be scheduled. You obtain this print job identifier by calling the [**AddJob**](addjob.md) function.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

You must successfully call the [**AddJob**](addjob.md) function before calling the **ScheduleJob** function. **AddJob** obtains the print job identifier that you pass to **ScheduleJob** as *dwJobID*. Both calls must use the same value for *hPrinter*.

The **ScheduleJob** function checks for a valid spool file. If there is an invalid spool file, or if it is empty, **ScheduleJob** deletes both the spool file and the corresponding print job entry in the print spooler.

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

[**AddJob**](addjob.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> </dl>

 

 




