---
description: The GetDeliveryBuffer method retrieves a media sample that contains an empty buffer.
ms.assetid: 5a20c11b-50f8-443e-a4d5-6bcffde741d5
title: CBaseOutputPin.GetDeliveryBuffer method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseOutputPin.GetDeliveryBuffer
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseOutputPin.GetDeliveryBuffer method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetDeliveryBuffer` method retrieves a media sample that contains an empty buffer.

## Syntax


```C++
virtual HRESULT GetDeliveryBuffer(
   IMediaSample   **ppSample,
   REFERENCE_TIME *pStartTime,
   REFERENCE_TIME *pEndTime,
   DWORD          dwFlags
);
```



## Parameters

<dl> <dt>

*ppSample* 
</dt> <dd>

Address of a variable that receives a pointer to the buffer's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

</dd> <dt>

*pStartTime* 
</dt> <dd>

Pointer to the start time of the sample, or **NULL**.

</dd> <dt>

*pEndTime* 
</dt> <dd>

Pointer to the ending time of the sample, or **NULL**.

</dd> <dt>

*dwFlags* 
</dt> <dd>

Bitwise combination of flags supported by the [**IMemAllocator::GetBuffer**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-getbuffer) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                                   | Description                        |
|-----------------------------------------------------------------------------------------------|------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | No allocator available.<br/> |



 

## Remarks

This method calls the **IMemAllocator::GetBuffer** method on the allocator, and passes the parameters to that method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseOutputPin Class**](cbaseoutputpin.md)
</dt> </dl>

 

 




