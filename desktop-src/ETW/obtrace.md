---
Description: 'Represents the parent class from which all object manager event trace classes are derived.'
ms.assetid: '07cfc4a2-c665-4080-bc4b-fe9ec7191fdc'
title: ObTrace class
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

To enable object manager event tracing, call the [**TraceSetInformation**](tracesetinformation.md) function with the *InformationClass* parameter equal to the [**TRACE\_INFO\_CLASS**](trace-info-class.md) enumeration value **TraceSystemTraceEnableFlagsInfo** and the [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure's **EnableFlags** member equal to **PERF\_OB\_HANDLE** (0x80000040).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                   |
| MOF<br/>                      | <dl> <dt>Wmicore.mof</dt> </dl> |



 

 




