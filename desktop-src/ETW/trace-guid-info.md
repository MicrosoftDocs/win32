---
Description: Defines the header to the list of sessions that enabled the provider specified in the InBuffer parameter of EnumerateTraceGuidsEx.
ms.assetid: 2c484adf-605d-420b-8059-942b35305acd
title: TRACE\_GUID\_INFO structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# TRACE\_GUID\_INFO structure

Defines the header to the list of sessions that enabled the provider specified in the *InBuffer* parameter of [**EnumerateTraceGuidsEx**](enumeratetraceguidsex.md).

## Syntax


```C++
typedef struct _TRACE_GUID_INFO {
  ULONG InstanceCount;
  ULONG Reserved;
} TRACE_GUID_INFO, *PTRACE_GUID_INFO;
```



## Members

<dl> <dt>

**InstanceCount**
</dt> <dd>

The number of [**TRACE\_PROVIDER\_INSTANCE\_INFO**](trace-provider-instance-info.md) blocks contained in the list. You can have multiple instances of the same provider if the provider lives in a DLL that is loaded by multiple processes.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

Use the size of this structure to access the first [**TRACE\_PROVIDER\_INSTANCE\_INFO**](trace-provider-instance-info.md) block in the list.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**TRACE\_PROVIDER\_INSTANCE\_INFO**](trace-provider-instance-info.md)
</dt> </dl>

 

 




