---
Description: Defines the session and the information that the session used to enable the provider.
ms.assetid: 999dd102-5937-4b1e-b841-623dddaa0df9
title: TRACE\_ENABLE\_INFO structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TRACE\_ENABLE\_INFO structure

Defines the session and the information that the session used to enable the provider.

## Syntax


```C++
typedef struct _TRACE_ENABLE_INFO {
  ULONG     IsEnabled;
  UCHAR     Level;
  UCHAR     Reserved1;
  USHORT    LoggerId;
  ULONG     EnableProperty;
  ULONG     Reserved2;
  ULONGLONG MatchAnyKeyword;
  ULONGLONG MatchAllKeyword;
} TRACE_ENABLE_INFO, *PTRACE_ENABLE_INFO;
```



## Members

<dl> <dt>

**IsEnabled**
</dt> <dd>

Indicates if the provider is enabled to the session. The value is **TRUE** if the provider is enabled to the session, otherwise, the value is **FALSE**. This value should always be **TRUE**.

</dd> <dt>

**Level**
</dt> <dd>

Level of detail that the session asked the provider to include in the events. For details, see the *Level* parameter of the [**EnableTraceEx**](enabletraceex-func.md) function.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**LoggerId**
</dt> <dd>

Identifies the session that enabled the provider.

</dd> <dt>

**EnableProperty**
</dt> <dd>

Additional information that the session wants ETW to include in the log file. For details, see the *EnableProperty* parameter of the [**EnableTraceEx**](enabletraceex-func.md) function.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**MatchAnyKeyword**
</dt> <dd>

Keywords specify which events the session wants the provider to write. For details, see the *MatchAnyKeyword* parameter of the [**EnableTraceEx**](enabletraceex-func.md) function.

</dd> <dt>

**MatchAllKeyword**
</dt> <dd>

Keywords specify which events the session wants the provider to write. For details, see the *MatchAllKeyword* parameter of the [**EnableTraceEx**](enabletraceex-func.md) function.

</dd> </dl>

## Remarks

The [**TRACE\_PROVIDER\_INSTANCE\_INFO**](trace-provider-instance-info.md) block contains one or more of these structures.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**TRACE\_PROVIDER\_INSTANCE\_INFO**](trace-provider-instance-info.md)
</dt> </dl>

 

 




