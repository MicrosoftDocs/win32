---
Description: The TRACE\_GUID\_PROPERTIES structure contains information about an event trace provider.
ms.assetid: 849f2d34-14e0-43e8-a735-d46e94671725
title: TRACE_GUID_PROPERTIES structure
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TRACE_GUID_PROPERTIES
api_type: 
- HeaderDef
api_location: 
- Evntrace.h
---

# TRACE\_GUID\_PROPERTIES structure

The **TRACE\_GUID\_PROPERTIES** structure contains information about an event trace provider.

## Syntax


```C++
typedef struct _TRACE_GUID_PROPERTIES {
  GUID    Guid;
  ULONG   GuidType;
  ULONG   LoggerId;
  ULONG   EnableLevel;
  ULONG   EnableFlags;
  BOOLEAN IsEnable;
} TRACE_GUID_PROPERTIES, *PTRACE_GUID_PROPERTIES;
```



## Members

<dl> <dt>

**Guid**
</dt> <dd>

Control GUID of the event trace provider.

</dd> <dt>

**GuidType**
</dt> <dd>

Not used.

</dd> <dt>

**LoggerId**
</dt> <dd>

Session handle that identifies the event tracing session.

</dd> <dt>

**EnableLevel**
</dt> <dd>

Value passed as the *EnableLevel* parameter to the [**EnableTrace**](enabletrace.md) function.

</dd> <dt>

**EnableFlags**
</dt> <dd>

Value passed as the *EnableFlag* parameter to the [**EnableTrace**](enabletrace.md) function.

</dd> <dt>

**IsEnable**
</dt> <dd>

If this member is **TRUE**, the element identified by the **Guid** member is currently enabled for the session identified by the **LoggerId** member. If this member is **FALSE**, all other members have no meaning and should be zero.

</dd> </dl>

## Remarks

Be sure to initialize the memory for this structure to zero before setting any members or passing to any functions.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**EnumerateTraceGuids**](enumeratetraceguids.md)
</dt> </dl>

 

 




