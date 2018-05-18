---
Description: 'Pointer to the allocator that created this sample.'
ms.assetid: 'b4faccec-9124-4ae6-8662-ac5eb017328a'
title: 'CMediaSample::m\_pAllocator member'
---

# CMediaSample::m\_pAllocator member

Pointer to the allocator that created this sample.

## Syntax


```C++
CBaseAllocator *m_pAllocator;
```



## Remarks

Although the sample keeps a pointer to the allocator, it does not hold a reference count. Instead, the allocator increments its own reference count in the [**IMemAllocator::GetBuffer**](imemallocator-getbuffer.md) method, and releases itself in the [**IMemAllocator::ReleaseBuffer**](imemallocator-releasebuffer.md) method. This guarantees that the allocator will be available as long as another object is using the sample.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




