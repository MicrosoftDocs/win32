---
Description: 'Frees a memory block that was allocated from a heap by RtlAllocateHeap.'
ms.assetid: '0A08FB6B-23A3-450B-8745-AEB927CEB7BB'
title: RtlFreeHeap function
---

# RtlFreeHeap function

Frees a memory block that was allocated from a heap by [**RtlAllocateHeap**](ifsk.rtlallocateheap).

## Syntax


```C++
BOOLEAN RtlFreeHeap(
  _In_     PVOID HeapHandle,
  _In_opt_ ULONG Flags,
  _In_     PVOID HeapBase
);
```



## Parameters

<dl> <dt>

*HeapHandle* \[in\]
</dt> <dd>

A handle for the heap whose memory block is to be freed. This parameter is a handle returned by [**RtlCreateHeap**](ifsk.rtlcreateheap).

</dd> <dt>

*Flags* \[in, optional\]
</dt> <dd>

A set of flags that controls aspects of freeing a memory block. Specifying the following value overrides the corresponding value that was specified in the *Flags* parameter when the heap was created by [**RtlCreateHeap**](ifsk.rtlcreateheap).



| Flag                           | Meaning                                                                                   |
|--------------------------------|-------------------------------------------------------------------------------------------|
| HEAP\_NO\_SERIALIZE<br/> | Mutual exclusion will not be used when **RtlFreeHeap** is accessing the heap. <br/> |



 

</dd> <dt>

*HeapBase* \[in\]
</dt> <dd>

A pointer to the memory block to free. This pointer is returned by [**RtlAllocateHeap**](ifsk.rtlallocateheap).

</dd> </dl>

## Return value

Returns **TRUE** if the block was freed successfully; **FALSE** otherwise.

> [!Note]  
> Starting with Windows 8 the return value is typed as **LOGICAL**, which has a different size than **BOOLEAN**.

 

## Requirements



|                                     |                                                                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                    |
| Target platform<br/>          | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>                   | <dl> <dt>Ntifs.h (include Ntifs.h)</dt> </dl>                                    |
| Library<br/>                  | <dl> <dt>Ntdll.lib</dt> </dl>                                                    |
| DLL<br/>                      | <dl> <dt>Ntdll.dll</dt> </dl>                                                    |



## See also

<dl> <dt>

[**RtlAllocateHeap**](ifsk.rtlallocateheap)
</dt> <dt>

[**RtlCreateHeap**](ifsk.rtlcreateheap)
</dt> <dt>

[**RtlDestroyHeap**](ifsk.rtldestroyheap)
</dt> </dl>

 

 




