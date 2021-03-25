---
description: The Copy method copies a media sample.
ms.assetid: 3fbc6925-6e9c-4419-ab0d-0bbdbdf9bb8e
title: CTransInPlaceFilter.Copy method (Transip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceFilter.Copy
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransInPlaceFilter.Copy method

The `Copy` method copies a media sample.

## Syntax


```C++
IMediaSample* Copy(
   IMediaSample *pSource
);
```



## Parameters

<dl> <dt>

*pSource* 
</dt> <dd>

Pointer to the [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface of the sample.

</dd> </dl>

## Return value

Returns a pointer to the **IMediaSample** interface on the new sample.

## Remarks

This method retrieves an empty buffer from the downstream allocator. It copies all of the sample properties from *pSource* into the new sample, along with the actual data in the sample. If the filter is using two allocators, it calls this method to copy data across buffers.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceFilter Class**](ctransinplacefilter.md)
</dt> </dl>

 

 




