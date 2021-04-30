---
description: Memory management tracing event for a heap allocation operation.
ms.assetid: 572DEC3B-F909-45E5-849F-707AA62F2F5E
title: ETW_HEAP_EVENT_ALLOC event (Ntwmi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ETW_HEAP_EVENT_ALLOC
api_type: 
- HeaderDef
api_location: 
- ntwmi.h
---

# ETW\_HEAP\_EVENT\_ALLOC event

The **ETW\_HEAP\_EVENT\_ALLOC** event is a memory management tracing event for a heap allocation operation.


```C++
typedef struct ETW_HEAP_EVENT_ALLOC
```



## Parameters

<dl> <dt>

*HeapHandle* 
</dt> <dd>

The handle of the heap where the memory was allocated. This is the heap handle an app passed to the [**AllocateHeap**](/previous-versions/windows/desktop/legacy/aa374721(v=vs.85)) function when the memory was allocated.

</dd> <dt>

*Size* 
</dt> <dd>

The size in bytes allocated from the heap.

</dd> <dt>

*Address* 
</dt> <dd>

The address of the memory that was allocated.

</dd> <dt>

*Source* 
</dt> <dd>

The source of the memory that the allocator used for the heap allocation.

The following table lists the possible values for the *Source* parameter as defined in the *ntetw.h* header file:



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <span id="MEMORY_FROM_LOOKASIDE"></span><span id="memory_from_lookaside"></span><dl> <dt>**MEMORY\_FROM\_LOOKASIDE**</dt> <dt>1</dt> </dl>                                       | Memory from the lookaside list.<br/>                                   |
| <span id="MEMORY_FROM_LOWFRAG"></span><span id="memory_from_lowfrag"></span><dl> <dt>**MEMORY\_FROM\_LOWFRAG**</dt> <dt>2</dt> </dl>                                             | Memory from the low-fragmentation heap.<br/>                           |
| <span id="MEMORY_FROM_MAINPATH"></span><span id="memory_from_mainpath"></span><dl> <dt>**MEMORY\_FROM\_MAINPATH**</dt> <dt>3</dt> </dl>                                          | Memory from main code path.<br/>                                       |
| <span id="MEMORY_FROM_SLOWPATH____________________"></span><span id="memory_from_slowpath____________________"></span><dl> <dt>**MEMORY\_FROM\_SLOWPATH** </dt> <dt>4</dt> </dl> | Memory from slow path.<br/>                                            |
| <span id="MEMORY_FROM_INVALID"></span><span id="memory_from_invalid"></span><dl> <dt>**MEMORY\_FROM\_INVALID**</dt> <dt>5</dt> </dl>                                             | Memory that was not valid.<br/>                                        |
| <span id="MEMORY_FROM_SEGMENT_HEAP"></span><span id="memory_from_segment_heap"></span><dl> <dt>**MEMORY\_FROM\_SEGMENT\_HEAP**</dt> <dt>6</dt> </dl>                             | This value is reserved for future use and will never be returned.<br/> |



 

</dd> </dl>

## Remarks

The **ETW\_HEAP\_EVENT\_ALLOC** event is logged on all heap allocations.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Ntwmi.h</dt> </dl> |



## See also

<dl> <dt>

[Memory Management Tracing Events](memory-management-tracing-events.md)
</dt> </dl>

 

 
