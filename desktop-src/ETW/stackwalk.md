---
description: This class is the parent class for stack tracing events.
ms.assetid: 3c0ff01b-fb37-4931-9484-ff8048abca66
title: StackWalk class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- StackWalk
api_type: 
- NA
api_location: 
---

# StackWalk class

This class is the parent class for stack tracing events.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Guid("{def2fe46-7bd6-4b80-bd94-f57fe20d0ce3}")]
class StackWalk : MSNT_SystemTrace
{
};
```

## Members

The **StackWalk** class does not define any members.

## Remarks

To enable stack tracing of kernel events, call the [**TraceSetInformation**](/windows/win32/api/evntrace/nf-evntrace-tracesetinformation) function and specify the kernel events and types for which you want to capture the stack trace. To enable stack tracing for other events, set the **EnableProperty** member of [**ENABLE\_TRACE\_PARAMETERS**](/windows/win32/api/evntrace/ns-evntrace-enable_trace_parameters) to **EVENT\_ENABLE\_PROPERTY\_STACK\_TRACE**.

Use the following event type to identify the actual event when consuming events.



| Event type           | Description                                                                                                           |
|----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Event type value, 32 | Stack tracing event. The [**StackWalk\_Event**](stackwalk-event.md) MOF class defines the event data for this event. |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 
