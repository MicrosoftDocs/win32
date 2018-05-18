---
Description: 'This class is the parent class for stack tracing events.'
ms.assetid: '3c0ff01b-fb37-4931-9484-ff8048abca66'
title: StackWalk class
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

To enable stack tracing of kernel events, call the [**TraceSetInformation**](tracesetinformation.md) function and specify the kernel events and types for which you want to capture the stack trace. To enable stack tracing for other events, set the **EnableProperty** member of [**ENABLE\_TRACE\_PARAMETERS**](enable-trace-parameters.md) to **EVENT\_ENABLE\_PROPERTY\_STACK\_TRACE**.

Use the following event type to identify the actual event when consuming events.



| Event type           | Description                                                                                                           |
|----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Event type value, 32 | Stack tracing event. The [**StackWalk\_Event**](stackwalk-event.md) MOF class defines the event data for this event. |



 

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 




