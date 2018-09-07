---
Description: Determines the version information of the TraceLogging session.
ms.assetid: E2B291DB-928F-4170-8684-4B26A7E067BD
title: TRACE_VERSION_INFO enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TRACE_VERSION_INFO
api_type: 
- HeaderDef
api_location: 
- Evntrace.h
---

# TRACE\_VERSION\_INFO enumeration

Determines the version information of the TraceLogging session.

## Syntax


```C++
typedef enum  { 
  EtwTraceProcessingVersion  = UINT,
  Reserved                   = UINT
} TRACE_VERSION_INFO;
```



## Constants

<dl> <dt>

<span id="EtwTraceProcessingVersion"></span><span id="etwtraceprocessingversion"></span><span id="ETWTRACEPROCESSINGVERSION"></span>**EtwTraceProcessingVersion**
</dt> <dd>

TraceLogging version information.

</dd> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>**Reserved**
</dt> <dd>

Not used.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**TraceSetInformation**](tracesetinformation.md)
</dt> </dl>

 

 




