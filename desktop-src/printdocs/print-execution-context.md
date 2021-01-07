---
description: Represents the execution context when GetPrintExecutionData is called.
ms.assetid: b6c026b2-8519-45d3-9614-b502eec23cde
title: PRINT_EXECUTION_CONTEXT enumeration (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINT_EXECUTION_CONTEXT
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINT\_EXECUTION\_CONTEXT enumeration

Represents the execution context when [**GetPrintExecutionData**](getprintexecutiondata.md) is called.

## Syntax


```C++
typedef enum  { 
  PRINT_EXECUTION_CONTEXT_APPLICATION             = 0,
  PRINT_EXECUTION_CONTEXT_SPOOLER_SERVICE         = 1,
  PRINT_EXECUTION_CONTEXT_SPOOLER_ISOLATION_HOST  = 2,
  PRINT_EXECUTION_CONTEXT_FILTER_PIPELINE         = 3,
  PRINT_EXECUTION_CONTEXT_WOW64                   = 4
} PRINT_EXECUTION_CONTEXT;
```



## Constants

<dl> <dt>

<span id="PRINT_EXECUTION_CONTEXT_APPLICATION"></span><span id="print_execution_context_application"></span>**PRINT\_EXECUTION\_CONTEXT\_APPLICATION**
</dt> <dd>

The caller is running in an application.

</dd> <dt>

<span id="PRINT_EXECUTION_CONTEXT_SPOOLER_SERVICE"></span><span id="print_execution_context_spooler_service"></span>**PRINT\_EXECUTION\_CONTEXT\_SPOOLER\_SERVICE**
</dt> <dd>

The caller is running in the spooler service (spoolsv.exe).

</dd> <dt>

<span id="PRINT_EXECUTION_CONTEXT_SPOOLER_ISOLATION_HOST"></span><span id="print_execution_context_spooler_isolation_host"></span>**PRINT\_EXECUTION\_CONTEXT\_SPOOLER\_ISOLATION\_HOST**
</dt> <dd>

The caller is running in the print isolation host (PrintIsolationHost.exe)

</dd> <dt>

<span id="PRINT_EXECUTION_CONTEXT_FILTER_PIPELINE"></span><span id="print_execution_context_filter_pipeline"></span>**PRINT\_EXECUTION\_CONTEXT\_FILTER\_PIPELINE**
</dt> <dd>

The caller is running in the print filter pipeline (printfilterpipelinesvc.exe)

</dd> <dt>

<span id="PRINT_EXECUTION_CONTEXT_WOW64"></span><span id="print_execution_context_wow64"></span>**PRINT\_EXECUTION\_CONTEXT\_WOW64**
</dt> <dd>

The caller is running in splwow64.exe

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**GetPrintExecutionData**](getprintexecutiondata.md)
</dt> <dt>

[**PRINT\_EXECUTION\_DATA**](print-execution-data.md)
</dt> </dl>

 

 




