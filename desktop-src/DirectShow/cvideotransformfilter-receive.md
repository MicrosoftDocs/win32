---
description: The Receive method receives a media sample, processes it, and delivers an output sample to the downstream filter. This method overrides the CTransformFilter::Receive method.
ms.assetid: 35e22a63-471e-4ca8-be3b-d84920cec7cb
title: CVideoTransformFilter.Receive method (Vtrans.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CVideoTransformFilter.Receive
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CVideoTransformFilter.Receive method

The `Receive` method receives a media sample, processes it, and delivers an output sample to the downstream filter. This method overrides the [**CTransformFilter::Receive**](ctransformfilter-receive.md) method.

## Syntax


```C++
HRESULT Receive(
   IMediaSample *pSample
);
```



## Parameters

<dl> <dt>

*pSample* 
</dt> <dd>

Pointer to the [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface on the input sample.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following:



| Return code                                                                             | Description                                                 |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | The upstream filter should stop sending samples.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                                         |



 

## Remarks

This method calls [**CVideoTransformFilter::ShouldSkipFrame**](cvideotransformfilter-shouldskipframe.md) to determine whether it should deliver this sample or simply discard it. If **ShouldSkipFrame** returns **FALSE** (indicating the sample should be delivered), the method does the following:

1.  Calls [**CTransformFilter::InitializeOutputSample**](ctransformfilter-initializeoutputsample.md) to prepare the output sample
2.  Calls [**CTransformFilter::Transform**](ctransformfilter-transform.md) to process the input sample. This method is pure virtual, and must be implemented in the derived class.
3.  Calls [**CBaseOutputPin::Deliver**](cbaseoutputpin-deliver.md) to deliver the output sample.

Also, this method checks for format changes on the input or output sample, by calling [**IMediaSample::GetMediaType**](/windows/desktop/api/Strmif/nf-strmif-imediasample-getmediatype). If there is a format change, the method sets the connection type on the corresponding pin. Before it sets the new type, it calls **StopStreaming**. After it sets the new type, it calls **StartStreaming**. The derived class can use these methods to update its internal state. The derived class might also need to check for the new format in its **Transform** method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Vtrans.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CVideoTransformFilter Class**](cvideotransformfilter.md)
</dt> </dl>

 

 




