---
description: The parent class for log header events. This class is always the first event trace class sent to a consumer (this event is not sent to real-time consumers). The following syntax is simplified from MOF code.
ms.assetid: fb507d9a-6ed2-4cb1-8cea-85c0a3832e51
title: EventTraceEvent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EventTraceEvent
api_type: 
- NA
api_location: 
---

# EventTraceEvent class

The parent class for log header events. This class is always the first event trace class sent to a consumer (this event is not sent to real-time consumers).

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{68fdd900-4a3e-11d1-84f4-0000f80464e3}")]
class EventTraceEvent : MSNT_SystemTrace
{
};
```

## Members

The **EventTraceEvent** class does not define any members.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**MSNT\_SystemTrace**](msnt-systemtrace.md)
</dt> <dt>

[**EventTrace\_Header**](eventtrace-header.md)
</dt> </dl>

 

 




