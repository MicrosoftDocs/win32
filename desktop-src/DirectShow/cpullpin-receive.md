---
description: The Receive method is called when the object receives a media sample from the output pin. The derived class must implement this method.
ms.assetid: ef45388b-b038-4838-b76b-dbbdc5388495
title: CPullPin.Receive method (Pullpin.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPullPin.Receive
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CPullPin.Receive method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Receive` method is called when the object receives a media sample from the output pin. The derived class must implement this method.

## Syntax


```C++
virtual HRESULT Receive(
   IMediaSample *pSample
) = 0;
```



## Parameters

<dl> <dt>

*pSample* 
</dt> <dd>

Pointer to the [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface of the media sample.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Returning a value other than S\_OK will stop the data-pulling thread.

## Remarks

This method is called whenever a new sample arrives from the output pin. Write this method in the same manner as the [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method.

The time stamps on the sample specify the byte offsets, relative to the original start position that was specified in [**CPullPin::Seek**](cpullpin-seek.md) method.

The start position is rounded down to the nearest alignment boundary, and the stop position is rounded up to the nearest alignment boundary. Also, if the stop position exceeds the total duration, the duration is used instead.

All time stamps are given as a byte offset multiplied by 10,000,000, defined as the constant UNITS. Thus, notionally one second is one byte. To find the actual byte offsets, call [**IMediaSample::GetTime**](/windows/desktop/api/Strmif/nf-strmif-imediasample-gettime) and divide the results by UNITS.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pullpin.h</dt> </dl>                                                                                                       |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPullPin Class**](cpullpin.md)
</dt> </dl>

 

 




