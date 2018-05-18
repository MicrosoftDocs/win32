---
Description: 'The m\_pAlloc member variable is a pointer to the IMemAllocator interface of the memory allocator.'
ms.assetid: 'a3be5982-83f0-4552-9bcd-85da4a4918ff'
title: 'CPullPin::m\_pAlloc member'
---

# CPullPin::m\_pAlloc member

The `m_pAlloc` member variable is a pointer to the [**IMemAllocator**](imemallocator.md) interface of the memory allocator.

## Syntax


```C++
IMemAllocator *m_pAlloc;
```



## Remarks

The [**CPullPin::DecideAllocator**](cpullpin-decideallocator.md) method sets this member variable.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pullpin.h</dt> </dl>                                                                                                       |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPullPin Class**](cpullpin.md)
</dt> </dl>

 

 




