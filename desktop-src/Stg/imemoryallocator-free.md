---
title: IMemoryAllocator Free method
description: The Free method frees the memory allocated by the Allocate method.
ms.assetid: 41f81cba-4431-4ff7-ac84-8ff5bea71b65
keywords:
- Free method Structured Storage
- Free method Structured Storage , IMemoryAllocator interface
- IMemoryAllocator interface Structured Storage , Free method
topic_type:
- apiref
api_name:
- IMemoryAllocator.Free
api_location:
- Ole32.lib
- Ole32.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMemoryAllocator::Free method

The **Free** method frees the memory allocated by the [**Allocate**](imemoryallocator-allocate.md) method.

## Syntax


```C++
virtual void Free(
   void* pv
);
```



## Parameters

<dl> <dt>

*pv* 
</dt> <dd>

Pointer to the memory to be freed.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Library<br/>                  | <dl> <dt>Ole32.lib</dt> </dl> |



 

 





