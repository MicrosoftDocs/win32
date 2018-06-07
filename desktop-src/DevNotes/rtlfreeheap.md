---
Description: Frees a memory block that was allocated from a heap by RtlAllocateHeap.
ms.assetid: 0A08FB6B-23A3-450B-8745-AEB927CEB7BB
title: RtlFreeHeap function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RtlFreeHeap function

Frees a memory block that was allocated from a heap by [**RtlAllocateHeap**](https://msdn.microsoft.com/38f4c2b7-f9cd-42f2-b75e-725976b6b9dd).

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

A handle for the heap whose memory block is to be freed. This parameter is a handle returned by [**RtlCreateHeap**](https://msdn.microsoft.com/77ba5ba3-11d3-4c28-86e6-91f3189b5403).

</dd> <dt>

*Flags* \[in, optional\]
</dt> <dd>

A set of flags that controls aspects of freeing a memory block. Specifying the following value overrides the corresponding value that was specified in the *Flags* parameter when the heap was created by [**RtlCreateHeap**](https://msdn.microsoft.com/77ba5ba3-11d3-4c28-86e6-91f3189b5403).



| Flag                           | Meaning                                                                                   |
|--------------------------------|-------------------------------------------------------------------------------------------|
| HEAP\_NO\_SERIALIZE<br/> | Mutual exclusion will not be used when **RtlFreeHeap** is accessing the heap. <br/> |



 

</dd> <dt>

*HeapBase* \[in\]
</dt> <dd>

A pointer to the memory block to free. This pointer is returned by [**RtlAllocateHeap**](https://msdn.microsoft.com/38f4c2b7-f9cd-42f2-b75e-725976b6b9dd).

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

[**RtlAllocateHeap**](https://msdn.microsoft.com/38f4c2b7-f9cd-42f2-b75e-725976b6b9dd)
</dt> <dt>

[**RtlCreateHeap**](https://msdn.microsoft.com/77ba5ba3-11d3-4c28-86e6-91f3189b5403)
</dt> <dt>

[**RtlDestroyHeap**](https://msdn.microsoft.com/e62855a0-284b-434b-88a4-1f21f1b77cf2)
</dt> </dl>

 

 




