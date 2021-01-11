---
description: Represents the parent class from which all object manager event trace classes are derived.
ms.assetid: 07cfc4a2-c665-4080-bc4b-fe9ec7191fdc
title: ObTrace class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ObTrace
api_type: 
- NA
api_location: 
---

# ObTrace class

Represents the parent class from which all object manager event trace classes are derived.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[DisplayName("Object"), Dynamic, EventVersion(2), Guid("{89497f50-effe-4440-8cf2-ce6b1cdcaca7}")]
class ObTrace : MSNT_SystemTrace
{
};
```

## Members

The **ObTrace** class does not define any members.

## Remarks

To enable object manager event tracing, call the [**TraceSetInformation**](/windows/win32/api/evntrace/nf-evntrace-tracesetinformation) function with the *InformationClass* parameter equal to the [**TRACE\_INFO\_CLASS**](/windows/win32/api/evntrace/ne-evntrace-trace_query_info_class) enumeration value **TraceSystemTraceEnableFlagsInfo** and the [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure's **EnableFlags** member equal to **PERF\_OB\_HANDLE** (0x80000040).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                   |
| MOF<br/>                      | <dl> <dt>Wmicore.mof</dt> </dl> |



 

 
