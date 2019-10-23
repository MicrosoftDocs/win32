---
Description: Specifies what kind of operation will be done on a handle.
ms.assetid: 92932E4C-0A06-4CDE-B14B-BF53226E133B
title: ETW_PROCESS_HANDLE_INFO_TYPE enumeration
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ETW_PROCESS_HANDLE_INFO_TYPE
api_type: 
- HeaderDef
api_location: 
- evntrace.h
---

# ETW\_PROCESS\_HANDLE\_INFO\_TYPE enumeration

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Specifies what kind of operation will be done on a handle. currently used with the [**QueryTraceProcessingHandle**](querytraceprocessinghandle.md) function.

## Syntax


```C++
typedef enum _ETW_PROCESS_HANDLE_INFO_TYPE { 
  EtwQueryPartitionInformation  = 1,
  EtwQueryProcessHandleInfoMax  = 2
} ETW_PROCESS_HANDLE_INFO_TYPE;
```



## Constants

<dl> <dt>

<span id="EtwQueryPartitionInformation"></span><span id="etwquerypartitioninformation"></span><span id="ETWQUERYPARTITIONINFORMATION"></span>**EtwQueryPartitionInformation**
</dt> <dd>

Used to query partition identifying information. *InBuffer* should be Null. *OutBuffer* should be large enough to hold the returned [**ETW\_TRACE\_PARTITION\_INFORMATION**](etw-trace-partition-information.md) structure. Note that this will only return a non-zero structure when the queried handle is for a trace file generated from a non-host partition on Windows 10, version 1709.

</dd> <dt>

<span id="EtwQueryProcessHandleInfoMax"></span><span id="etwqueryprocesshandleinfomax"></span><span id="ETWQUERYPROCESSHANDLEINFOMAX"></span>**EtwQueryProcessHandleInfoMax**
</dt> <dd>

Marks the last value in the enumeration for testing purposes. Should not be used.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



 

 




