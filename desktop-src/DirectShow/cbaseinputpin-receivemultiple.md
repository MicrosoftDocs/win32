---
description: The ReceiveMultiple method receives an array of samples. This method implements the IMemInputPin::ReceiveMultiple method.
ms.assetid: 21e757c7-f623-4ccb-8e37-512ee4dd7aa7
title: CBaseInputPin.ReceiveMultiple method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseInputPin.ReceiveMultiple
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseInputPin.ReceiveMultiple method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `ReceiveMultiple` method receives an array of samples. This method implements the [**IMemInputPin::ReceiveMultiple**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receivemultiple) method.

## Syntax


```C++
HRESULT ReceiveMultiple(
   IMediaSample **pSamples,
   long         nSamples,
   long         *nSamplesProcessed
);
```



## Parameters

<dl> <dt>

*pSamples* 
</dt> <dd>

Address of an array of [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) pointers, of size *nSamples*.

</dd> <dt>

*nSamples* 
</dt> <dd>

Number of samples to process.

</dd> <dt>

*nSamplesProcessed* 
</dt> <dd>

Pointer to a variable that receives the number of samples that were processed.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                                             | Description                                                |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Success.<br/>                                        |
| <dl> <dt>**S\_FALSE**</dt> </dl>                 | Pin is currently flushing; sample was rejected.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>               | **NULL** pointer argument.<br/>                      |
| <dl> <dt>**VFW\_E\_INVALIDMEDIATYPE**</dt> </dl> | Invalid media type.<br/>                             |
| <dl> <dt>**VFW\_E\_RUNTIME\_ERROR**</dt> </dl>   | A run-time error occurred.<br/>                      |
| <dl> <dt>**VFW\_E\_WRONG\_STATE**</dt> </dl>     | The pin is stopped.<br/>                             |



 

## Remarks

This method behaves like the [**CBaseInputPin::Receive**](cbaseinputpin-receive.md) method, but receives an array of samples. In the base class, the method loops through the array and calls **Receive** with each sample. Override this function if your filter can process batches of samples more efficiently than processing them one at a time.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseInputPin Class**](cbaseinputpin.md)
</dt> </dl>

 

 




