---
description: Reports to the Print Spooler service whether an XPS print job is in the spooling or the rendering phase and what part of the processing is currently underway.
ms.assetid: 66f7483d-be98-410d-b0c7-430743397de2
title: ReportJobProcessingProgress function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ReportJobProcessingProgress
api_type: 
- DllExport
api_location: 
- Spoolss.dll
- Ext-MS-Win-Printer-WinSpool-l1-1-2.dll
- WinSpool.Drv
- Ext-MS-Win-Printer-WinSpool-L1-1-3.dll
---

# ReportJobProcessingProgress function

Reports to the Print Spooler service whether an XPS print job is in the spooling or the rendering phase and what part of the processing is currently underway.

## Syntax


```C++
HRESULT ReportJobProcessingProgress(
  _In_ HANDLE                printerHandle,
  _In_ ULONG                 jobId,
       EPrintXPSJobOperation jobOperation,
       EPrintXPSJobProgress  jobProgress
);
```



## Parameters

<dl> <dt>

*printerHandle* \[in\]
</dt> <dd>

A printer handle for which the function is to retrieve information. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*jobId* \[in\]
</dt> <dd>

Identifies the print job for which to retrieve data. Use the [**AddJob**](addjob.md) function or [**StartDoc**](/windows/desktop/api/Wingdi/nf-wingdi-startdoca) function to get a print job identifier.

</dd> <dt>

*jobOperation* 
</dt> <dd>

Specifies whether the job is in the spooling phase or the rendering phase.

</dd> <dt>

*jobProgress* 
</dt> <dd>

Specifies what part of the processing is currently underway. This value refers to events in either the spooling or rendering phase depending on the value of *jobOperation*.

</dd> </dl>

## Return value

If the operation succeeds, the return value is S\_OK, otherwise the **HRESULT** will contain an error code.

For more information about COM error codes, see [Error Handling](../com/error-handling-in-com.md).

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

> [!Note]  
> **ReportJobProcessingProgress** will only report the progress of the XPS print job if the print job is in the spooling or rendering phase. **ReportJobProcessingProgress** will fail if it is called when the XPS print job is not in the spooling or rendering phase.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Spoolss.dll</dt> </dl>                    |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**EPrintXPSJobOperation**](eprintxpsjoboperation.md)
</dt> <dt>

[**EPrintXPSJobProgress**](eprintxpsjobprogress.md)
</dt> </dl>

 

