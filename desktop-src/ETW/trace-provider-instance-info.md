---
Description: Defines an instance of the provider GUID.
ms.assetid: 49c11cd5-2cb1-474a-8b51-2d86b4501da1
title: TRACE\_PROVIDER\_INSTANCE\_INFO structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TRACE\_PROVIDER\_INSTANCE\_INFO structure

Defines an instance of the provider GUID.

## Syntax


```C++
typedef struct _TRACE_PROVIDER_INSTANCE_INFO {
  ULONG NextOffset;
  ULONG EnableCount;
  ULONG Pid;
  ULONG Flags;
} TRACE_PROVIDER_INSTANCE_INFO, *PTRACE_PROVIDER_INSTANCE_INFO;
```



## Members

<dl> <dt>

**NextOffset**
</dt> <dd>

Offset, in bytes, from the beginning of this structure to the next **TRACE\_PROVIDER\_INSTANCE\_INFO** structure. The value is zero if there is not another instance info block.

</dd> <dt>

**EnableCount**
</dt> <dd>

Number of [**TRACE\_ENABLE\_INFO**](trace-enable-info.md) structures in this block. Each structure represents a session that enabled the provider.

</dd> <dt>

**Pid**
</dt> <dd>

Process identifier of the process that registered the provider.

</dd> <dt>

**Flags**
</dt> <dd>

Can be one of the following flags.



| Value                                                                                                                                                                                                               | Meaning                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TRACE_PROVIDER_FLAG_LEGACY"></span><span id="trace_provider_flag_legacy"></span><dl> <dt>**TRACE\_PROVIDER\_FLAG\_LEGACY**</dt> </dl>              | The provider used [**RegisterTraceGuids**](registertraceguids.md) instead of [**EventRegister**](/windows/win32/Evntprov/nf-evntprov-eventregister?branch=master) to register itself. <br/> |
| <span id="TRACE_PROVIDER_FLAG_PRE_ENABLE"></span><span id="trace_provider_flag_pre_enable"></span><dl> <dt>**TRACE\_PROVIDER\_FLAG\_PRE\_ENABLE**</dt> </dl> | The provider is not registered; however, one or more sessions have enabled the provider.<br/>                                                       |



 

</dd> </dl>

## Remarks

If more than one provider uses the same GUID, the [**TRACE\_GUID\_INFO**](trace-guid-info.md) block contains more than one **TRACE\_PROVIDER\_INSTANCE\_INFO** structure.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**TRACE\_ENABLE\_INFO**](trace-enable-info.md)
</dt> <dt>

[**TRACE\_GUID\_INFO**](trace-guid-info.md)
</dt> </dl>

 

 




