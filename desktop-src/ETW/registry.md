---
description: Registry class - This class is the parent class for registry events. The following syntax is simplified from MOF code.
ms.assetid: 362d7653-1ba0-45b7-80f3-0fccca0badf1
title: Registry class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Registry
api_type: 
- NA
api_location: 
---

# Registry class

This class is the parent class for registry events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{ae53722e-c863-11d2-8659-00c04fa321a1}"), EventVersion(2)]
class Registry : MSNT_SystemTrace
{
};
```

## Members

The **Registry** class does not define any members.

## Remarks

To enable registry events in an NT Kernel logging session, specify the **EVENT\_TRACE\_FLAG\_REGISTRY** in the **EnableFlags** member of an [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure when calling the [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea) function.

Event trace consumers can implement special processing for registry events by calling the [**SetTraceCallback**](/windows/win32/api/evntrace/nf-evntrace-settracecallback) function and specifying [**RegistryGuid**](nt-kernel-logger-constants.md) as the *pGuid* parameter. Use the following event types to identify the actual registry event when consuming events.



| Event type                                                                       | Description                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EVENT\_TRACE\_TYPE\_REGCREATE**(Event type value is 10)<br/>             | Create key event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                            |
| **EVENT\_TRACE\_TYPE\_REGDELETE**(Event type value is 12)<br/>             | Delete key event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                            |
| **EVENT\_TRACE\_TYPE\_REGDELETEVALUE**(Event type value is 15)<br/>        | Delete value event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                          |
| **EVENT\_TRACE\_TYPE\_REGENUMERATEKEY**(Event type value is 17)<br/>       | Enumerate key event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                         |
| **EVENT\_TRACE\_TYPE\_REGENUMERATEVALUEKEY**(Event type value is 18)<br/>  | Enumerate value key event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                   |
| **EVENT\_TRACE\_TYPE\_REGFLUSH**(Event type value is 21)<br/>              | Flush key event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                             |
| **EVENT\_TRACE\_TYPE\_REGKCBDMP**(Event type value is 22)<br/>             | Create key event. Generated when a registry operation uses handles rather than strings to reference subkeys. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event. |
| **EVENT\_TRACE\_TYPE\_REGOPEN**(Event type value is 11)<br/>               | Open key event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                              |
| **EVENT\_TRACE\_TYPE\_REGQUERY**(Event type value is 13)<br/>              | Query key event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                             |
| **EVENT\_TRACE\_TYPE\_REGQUERYMULTIPLEVALUE**(Event type value is 19)<br/> | Query multiple value event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                  |
| **EVENT\_TRACE\_TYPE\_REGQUERYVALUE**(Event type value is 16)<br/>         | Query value event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                           |
| **EVENT\_TRACE\_TYPE\_REGSETINFORMATION**(Event type value is 20)<br/>     | Set information event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                       |
| **EVENT\_TRACE\_TYPE\_REGSETVALUE**(Event type value is 14)<br/>           | Set value event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                             |
| Event type value, 23                                                             | delete key event. Generated when a registry operation uses handles rather than strings to reference subkeys. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event. |
| Event type value, 24                                                             | Enumerates the registry keys open at the beginning of the session. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                           |
| Event type value, 25                                                             | Enumerates the registry keys open at the end of the session.The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                  |
| Event type value, 26                                                             | The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                                              |
| Event type value, 27                                                             | Open key event. The [**Registry\_TypeGroup1**](registry-typegroup1.md) MOF class defines the event data for this event.                                                                                              |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**MSNT\_SystemTrace**](msnt-systemtrace.md)
</dt> <dt>

[**Registry\_TypeGroup1**](registry-typegroup1.md)
</dt> <dt>

[**Registry\_V0**](registry-v0.md)
</dt> <dt>

[**Registry\_V1**](registry-v1.md)
</dt> </dl>

 

 
