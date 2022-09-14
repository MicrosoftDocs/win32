---
description: The InitializeOutputSample method retrieves a new output sample and initializes it.
ms.assetid: a4f8f514-cf1a-4f8f-ac17-17378705c2ea
title: CTransformFilter.InitializeOutputSample method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.InitializeOutputSample
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformFilter.InitializeOutputSample method

The `InitializeOutputSample` method retrieves a new output sample and initializes it.

## Syntax


```C++
HRESULT InitializeOutputSample(
   IMediaSample *pSample,
   IMediaSample **ppOutSample
);
```



## Parameters

<dl> <dt>

*pSample* 
</dt> <dd>

Pointer to the input sample's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

</dd> <dt>

*ppOutSample* 
</dt> <dd>

Receives a pointer to the output sample's **IMediaSample** interface.

</dd> </dl>

## Return value

Returns S\_OK or another **HRESULT** value.

## Remarks

This method is called by the [**CTransformFilter::Receive**](ctransformfilter-receive.md) method to prepare the output sample. Generally you do not have to call this method in your derived class, unless you override the **Receive** method.

This method retrieves a new sample from the output pin's allocator. Then it copies the sample properties from the input sample to the output sample. The sample properties are defined in the [**AM\_SAMPLE2\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-am_sample2_properties) structure.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




