---
title: ILogReaderCallback LogReaderCallback method
description: The AXE Core raises this event to send information for a single log entry to the solution for processing.
ms.assetid: '0594FFCA-D9B7-4DF5-8995-610DA6C3AD52'
keywords: ["LogReaderCallback method Access Execution Engine", "LogReaderCallback method Access Execution Engine , ILogReaderCallback interface", "ILogReaderCallback interface Access Execution Engine , LogReaderCallback method"]
topic_type:
- apiref
api_name:
- ILogReaderCallback.LogReaderCallback
api_location:
- AxeCore.dll
api_type:
- COM
---

# ILogReaderCallback::LogReaderCallback method

The AXE Core raises this event to send information for a single log entry to the solution for processing.

## Syntax


```C++
virtual BOOL LogReaderCallback(
   const LogReaderCallbackData *data
) = 0;
```



## Parameters

<dl> <dt>

*data* 
</dt> <dd>

The information of the AXE log entry.

</dd> </dl>

## Return value

The solution’s callback function returns **FALSE** to abort processing of the log files or a non-zero value to receive the next log entry.

## Remarks

When a solution calls [**ReadLogFile**](solution-readlogfile.md) and specifies the AXE .ETL files to process, the AXE Core invokes this method once for each entry in the file being processed.

Managed code uses the [**LogReaderCallback**](axe-logreadercallback_om)delegate

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ILogReaderCallback**](ilogreadercallback.md)
</dt> <dt>

[**ReadLogFile**](solution-readlogfile.md)
</dt> <dt>

[**LogReaderCallbackData**](logreadercallbackdata.md)
</dt> </dl>

 

 





