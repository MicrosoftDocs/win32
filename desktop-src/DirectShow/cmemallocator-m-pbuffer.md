---
description: Pointer to the memory block that contains the buffers.
ms.assetid: b9d08f5b-8616-4f68-869a-e8ebb77ccdc1
title: CMemAllocator::m_pBuffer member (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_pBuffer
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMemAllocator::m\_pBuffer member

Pointer to the memory block that contains the buffers.

## Syntax


```C++
LPBYTE m_pBuffer;
```



## Remarks

Sample buffers are calculated as offsets from this pointer.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMemAllocator Class**](cmemallocator.md)
</dt> </dl>

 

 




