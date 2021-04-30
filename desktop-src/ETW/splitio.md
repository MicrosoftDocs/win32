---
description: This class is the parent class for split IO events. The following syntax is simplified from MOF code.
ms.assetid: d65c5180-6f1a-45cc-bca8-eac13857d383
title: SplitIo class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SplitIo
api_type: 
- NA
api_location: 
---

# SplitIo class

This class is the parent class for split IO events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{d837ca92-12b9-44a5-ad6a-3a65b3578aa8}")]
class SplitIo : MSNT_SystemTrace
{
};
```

## Members

The **SplitIo** class does not define any members.

## Remarks

To enable split IO events in an NT Kernel logging session, specify the **EVENT\_TRACE\_FLAG\_SPLIT\_IO** flag in the **EnableFlags** member of an [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure when calling the [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea) function.

Event trace consumers can implement special processing for split IO events by calling the [**SetTraceCallback**](/windows/win32/api/evntrace/nf-evntrace-settracecallback) function and specifying [**SplitIoGuid**](nt-kernel-logger-constants.md) as the *pGuid* parameter. Use the following event type to identify the actual event when consuming events.



| Event type           | Description                                                                                                |
|----------------------|------------------------------------------------------------------------------------------------------------|
| Event type value, 32 | Split IO event. The [**SplitIo\_Info**](splitio-info.md) MOF class defines the event data for this event. |



 

Split IO events indicate that the IO requests have been split into multiple disk IO requests due to the underlying mirroring disk hardware.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 
