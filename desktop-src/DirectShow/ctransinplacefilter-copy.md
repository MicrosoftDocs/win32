---
Description: 'The Copy method copies a media sample.'
ms.assetid: '3fbc6925-6e9c-4419-ab0d-0bbdbdf9bb8e'
title: 'CTransInPlaceFilter.Copy method'
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

Pointer to the [**IMediaSample**](imediasample.md) interface of the sample.

</dd> </dl>

## Return value

Returns a pointer to the **IMediaSample** interface on the new sample.

## Remarks

This method retrieves an empty buffer from the downstream allocator. It copies all of the sample properties from *pSource* into the new sample, along with the actual data in the sample. If the filter is using two allocators, it calls this method to copy data across buffers.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceFilter Class**](ctransinplacefilter.md)
</dt> </dl>

 

 




