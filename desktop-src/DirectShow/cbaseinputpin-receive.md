---
description: CBaseInputPin.Receive method - The Receive method receives the next media sample in the stream. This method implements the IMemInputPin::Receive method.
ms.assetid: 30fefc7b-7c9c-44cd-b58b-2b275dfa2520
title: CBaseInputPin.Receive method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseInputPin.Receive
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseInputPin.Receive method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Receive` method receives the next media sample in the stream. This method implements the [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method.

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

Pointer to the sample's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

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

The upstream output pin calls this method to deliver a sample to the input pin. The input pin must do one of the following:

-   Process the sample before returning.
-   Return, and process the sample in a worker thread.
-   Reject the sample.

If the pin uses a worker thread to process the sample, add a reference count to the sample inside this method. After the method returns, the upstream pin releases the sample. When the sample's reference count reaches zero, the sample returns to the allocator for re-use.

This method is synchronous and can block. If the method might block, the pin's [**CBaseInputPin::ReceiveCanBlock**](cbaseinputpin-receivecanblock.md) method should return S\_OK.

In the base class, this method performs the following steps:

1.  Calls the [**CBaseInputPin::CheckStreaming**](cbaseinputpin-checkstreaming.md) method to verify that the pin can process samples now. If it cannot for example, if the pin is stopped the method fails.
2.  Retrieves the sample properties and checks whether the format has changed (see below).
3.  If the format has changed, the method calls the [**CBasePin::CheckMediaType**](cbasepin-checkmediatype.md) method to determine whether the new format is acceptable.
4.  If the new format is not acceptable, the method calls the [**CBasePin::EndOfStream**](cbasepin-endofstream.md) method, posts an EC\_ERRORABORT event, and returns an error code.
5.  Assuming there were no errors, the method returns S\_OK.

Test for a format change as follows:

-   If the sample supports the [**IMediaSample2**](/windows/desktop/api/Strmif/nn-strmif-imediasample2) interface, check the **dwSampleFlags** member of the [**AM\_SAMPLE2\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-am_sample2_properties) structure. If the AM\_SAMPLE\_TYPECHANGED flag is present, the format has changed.
-   Otherwise, if the sample does not support **IMediaSample2**, call the [**IMediaSample::GetMediaType**](/windows/desktop/api/Strmif/nf-strmif-imediasample-getmediatype) method. If the method returns a non-**NULL** value, the format has changed.

In the base class, this method does not process the sample. The derived class must override this method to perform the processing. (What this entails depends entirely on the filter.) The derived class should call the base-class method, to check for the errors described previously.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseInputPin Class**](cbaseinputpin.md)
</dt> </dl>

 

 




