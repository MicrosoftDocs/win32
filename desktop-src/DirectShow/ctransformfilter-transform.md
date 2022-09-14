---
description: The Transform method transforms an input sample to produce an output sample.
ms.assetid: 30ef8c0c-e834-481a-93ff-d06e6fa1ddeb
title: CTransformFilter.Transform method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.Transform
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformFilter.Transform method

The `Transform` method transforms an input sample to produce an output sample.

## Syntax


```C++
virtual HRESULT Transform(
   IMediaSample *pIn,
   IMediaSample *pOut
);
```



## Parameters

<dl> <dt>

*pIn* 
</dt> <dd>

Pointer to the input sample's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

</dd> <dt>

*pOut* 
</dt> <dd>

Pointer to the output sample's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

</dd> </dl>

## Return value

The base class returns E\_UNEXPECTED.

The derived class should return an **HRESULT** value, indicating success or failure. Possible values include those shown in the following table.



| Return code                                                                             | Description                            |
|-----------------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | Do not deliver this sample.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                    |



 

## Remarks

Override this method to produce output data. Read the input data from the sample specified by the *pIn* parameter, and write the new data into the sample specified by the *pOut* parameter.

Before the filter calls this method, it copies the properties from the input sample to the output sample. The `Transform` method should set any properties that differ between the two samples, using **IMediaSample** methods or the [**IMediaSample2**](/windows/desktop/api/Strmif/nn-strmif-imediasample2) interface (if available).

If the filter should not deliver this sample (for example, to support quality control), the method should return S\_FALSE.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




