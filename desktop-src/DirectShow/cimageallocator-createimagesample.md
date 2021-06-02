---
description: The CreateImageSample method creates a media sample.
ms.assetid: dae71692-5cbc-4bc7-a363-41766ef17c58
title: CImageAllocator.CreateImageSample method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageAllocator.CreateImageSample
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImageAllocator.CreateImageSample method

The `CreateImageSample` method creates a media sample.

## Syntax


```C++
virtual CImageSample* CreateImageSample(
   LPBYTE pData,
   LONG   Length
);
```



## Parameters

<dl> <dt>

*pData* 
</dt> <dd>

Pointer to a buffer of size *Length*, allocated by the caller.

</dd> <dt>

*Length* 
</dt> <dd>

Length of the buffer.

</dd> </dl>

## Return value

Returns a [**CImageSample**](cimagesample.md) object.

## Remarks

This method creates a new media sample, implemented as a **CImageSample** object. The sample's [**IMediaSample::GetPointer**](/windows/desktop/api/Strmif/nf-strmif-imediasample-getpointer) method returns a pointer to the buffer specified in the *pData* parameter.

If you derive a new allocator class from [**CImageAllocator**](cimageallocator.md) and a new media sample class from [**CImageSample**](cimagesample.md), you should override this method to create an instance of your media sample class.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageAllocator Class**](cimageallocator.md)
</dt> <dt>

[**CImageAllocator::Alloc**](cimageallocator-alloc.md)
</dt> </dl>

 

 




