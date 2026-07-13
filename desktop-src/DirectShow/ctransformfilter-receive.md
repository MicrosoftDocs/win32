---
description: The Receive method receives a media sample, processes it, and delivers an output sample to the downstream filter.
ms.assetid: 036b209a-3535-4922-b7e9-dbed25b812f5
title: CTransformFilter.Receive method (Transfrm.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.Receive
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransformFilter.Receive method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Receive` method receives a media sample, processes it, and delivers an output sample to the downstream filter.

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

The filter's input pin calls this method when it receives a sample. This method calls the [**CTransformFilter::InitializeOutputSample**](ctransformfilter-initializeoutputsample.md) method, which prepares a new output sample. Then it calls the [**CTransformFilter::Transform**](ctransformfilter-transform.md) method, which the derived class must implement. The **Transform** method processes the input data and produces output data.

If the **Transform** method returns S\_FALSE, the `Receive` method drops this sample. On the first dropped sample, the filter sends an [**EC\_QUALITY\_CHANGE**](ec-quality-change.md) event to the filter graph manager. Otherwise, if the **Transform** method returns S\_OK, the filter delivers the output sample. To do so, it calls the [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method on the downstream input pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




