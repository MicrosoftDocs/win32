---
description: Registers the provider and initializes the counter sets.
ms.assetid: edcf8df3-0f6d-4849-b41d-270509499b8e
title: CounterInitialize function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CounterInitialize
api_type: 
- NA
api_location: 
---

# CounterInitialize function

Registers the provider and initializes the counter sets.

## Syntax


```C++
ULONG WINAPI CounterInitialize(void);
```



## Parameters

This function has no parameters.

## Return value

Returns ERROR\_SUCCESS on success; otherwise, a standard Win32 error code.

## Remarks

Your provider calls this function. The function includes calls to the [**PerfStartProvider**](/windows/desktop/api/Perflib/nf-perflib-perfstartprovider) function and the [**PerfSetCounterSetInfo**](/windows/desktop/api/Perflib/nf-perflib-perfsetcountersetinfo) function.

The [**CTRPP**](ctrpp.md) tool generates this inline function when you specify the **-o** argument. The function's name include a *prefix* string if you specify the **-prefix** argument.

If you specify the **-MemoryRoutines** or **-NotificationCallback** arguments (or specify the **callback** attribute for the [**provider**](/windows/desktop/PerfCtrs/performance-counters-provider--counters--element) element), the **CounterInitialize** signature changes to the following:

``` syntax
ULONG WINAPI CounterInitialize(
    __in_opt PERFLIBREQUEST NotificationCallback,
    __in_opt PERF_MEM_ALLOC MemoryAllocationFunction,
    __in_opt PERF_MEM_FREE MemoryFreeFunction,
    __inout_opt PVOID MemoryFunctionContext
);
```

where,

<dl> <dt>

<span id="NotificationCallback"></span><span id="notificationcallback"></span><span id="NOTIFICATIONCALLBACK"></span>NotificationCallback
</dt> <dd>

The name of your [*ControlCallback*](/windows/desktop/api/Perflib/nc-perflib-perflibrequest) callback function that you implement to receive notification of consumer requests (for example, requests to add or remove counters from the query). Set to **NULL** if you do not implement the *ControlCallback* callback function.

</dd> <dt>

<span id="MemoryAllocationFunction"></span><span id="memoryallocationfunction"></span><span id="MEMORYALLOCATIONFUNCTION"></span>MemoryAllocationFunction
</dt> <dd>

The name of your [*AllocateMemory*](/windows/desktop/api/Perflib/nc-perflib-perf_mem_alloc) callback function that PERFLIB calls to allocate memory. Set to **NULL** if you did not specify the **-MemoryRoutines** argument.

</dd> <dt>

<span id="MemoryFreeFunction"></span><span id="memoryfreefunction"></span><span id="MEMORYFREEFUNCTION"></span>MemoryFreeFunction
</dt> <dd>

The name of your [*FreeMemory*](/windows/desktop/api/Perflib/nc-perflib-perf_mem_free) callback function that PERFLIB calls to free the memory allocated using the [*AllocateMemory*](/windows/desktop/api/Perflib/nc-perflib-perf_mem_alloc) function. Set to **NULL** if *MemoryAllocationFunction* is **NULL**.

</dd> <dt>

<span id="MemoryFunctionContext"></span><span id="memoryfunctioncontext"></span><span id="MEMORYFUNCTIONCONTEXT"></span>MemoryFunctionContext
</dt> <dd>

Context information to pass to your memory allocation and free routines. Can be **NULL**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

