---
description: The Receive method receives a media sample, processes it, and delivers an output sample to the downstream filter. This method overrides the CTransformFilter::Receive method.
ms.assetid: 35e22a63-471e-4ca8-be3b-d84920cec7cb
title: CVideoTransformFilter.Receive method (Vtrans.h)
ms.topic: reference
ms.date: 4/26/2023
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
ms.custom: UpdateFrequency5
---

# CVideoTransformFilter.Receive method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




