---
description: Registry_V1 class - This class is the parent class for registry events. The following syntax is simplified from MOF code.
ms.assetid: 7ad92377-3fd7-47e0-b96e-bab530ea9d99
title: Registry_V1 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Registry_V1
api_type: 
- NA
api_location: 
---

# Registry\_V1 class

This class is the parent class for registry events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{ae53722e-c863-11d2-8659-00c04fa321a1}"), EventVersion(1)]
class Registry_V1 : MSNT_SystemTrace
{
};
```

## Members

The **Registry\_V1** class does not define any members.

## Remarks

To enable registry events in an NT Kernel logging session, specify the **EVENT\_TRACE\_FLAG\_REGISTRY** in the **EnableFlags** member of an [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure when calling the [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea) function.

Event trace consumers can implement special processing for registry events by calling the [**SetTraceCallback**](/windows/win32/api/evntrace/nf-evntrace-settracecallback) function and specifying **RegistryGuid** as the *pGuid* parameter. Use the following event types to identify the actual registry event when consuming events.



| Event type                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EVENT\_TRACE\_TYPE\_REGCREATE**(Event type value is 10)<br/>             | Create key event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                                                                                                                                                                                                                                                     |
| **EVENT\_TRACE\_TYPE\_REGDELETE**(Event type value is 12)<br/>             | Delete key event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                                                                                                                                                                                                                                                     |
| **EVENT\_TRACE\_TYPE\_REGDELETEVALUE**(Event type value is 15)<br/>        | Delete value event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                                                                                                                                                                                                                                                   |
| **EVENT\_TRACE\_TYPE\_REGENUMERATEKEY**(Event type value is 17)<br/>       | Enumerate key event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                                                                                                                                                                                                                                                  |
| **EVENT\_TRACE\_TYPE\_REGENUMERATEVALUEKEY**(Event type value is 18)<br/>  | Enumerate value key event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                                                                                                                                                                                                                                            |
| **EVENT\_TRACE\_TYPE\_REGFLUSH**(Event type value is 21)<br/>              | Flush key event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                                                                                                                                                                                                                                                      |
| **EVENT\_TRACE\_TYPE\_REGKCBDMP**(Event type value is 22)<br/>             | Generated when a registry operation uses handles rather than strings to reference subkeys. These events are recorded once for each handle—the first time the handle is referenced. Repeated references to the handle do not generate multiple events.<br/> The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.<br/> **Windows 2000:** This value is not supported.<br/> |
| **EVENT\_TRACE\_TYPE\_REGOPEN**(Event type value is 11)<br/>               | Open key event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                                                                                                                                                                                                                                                       |
| **EVENT\_TRACE\_TYPE\_REGQUERY**(Event type value is 13)<br/>              | Query key event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                                                                                                                                                                                                                                                      |
| **EVENT\_TRACE\_TYPE\_REGQUERYMULTIPLEVALUE**(Event type value is 19)<br/> | Query multiple value event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                                                                                                                                                                                                                                           |
| **EVENT\_TRACE\_TYPE\_REGQUERYVALUE**(Event type value is 16)<br/>         | Query value event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                                                                                                                                                                                                                                                    |
| **EVENT\_TRACE\_TYPE\_REGSETINFORMATION**(Event type value is 20)<br/>     | Set information event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                                                                                                                                                                                                                                                |
| **EVENT\_TRACE\_TYPE\_REGSETVALUE**(Event type value is 14)<br/>           | Set value event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                                                                                                                                                                                                                                                      |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**MSNT\_SystemTrace**](msnt-systemtrace.md)
</dt> <dt>

[**Registry**](registry.md)
</dt> <dt>

[**Registry\_V0**](registry-v0.md)
</dt> <dt>

[**Registry\_V1\_TypeGroup1**](registry-v1-typegroup1.md)
</dt> </dl>

 

 
