---
Description: The m\_pAlloc member variable is a pointer to the IMemAllocator interface of the memory allocator.
ms.assetid: a3be5982-83f0-4552-9bcd-85da4a4918ff
title: CPullPinm\_pAlloc member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPullPin::m\_pAlloc member

The `m_pAlloc` member variable is a pointer to the [**IMemAllocator**](/windows/win32/Strmif/nn-strmif-imemallocator?branch=master) interface of the memory allocator.

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

 

 




