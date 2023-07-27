---
description: The Connect method connects the pin to another pin. This method implements the IPin::Connect method.
ms.assetid: 8ea99d2f-09da-4b15-a3b0-04ceb7888bc1
title: CBasePin.Connect method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.Connect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePin.Connect method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Connect` method connects the pin to another pin. This method implements the [**IPin::Connect**](/windows/desktop/api/Strmif/nf-strmif-ipin-connect) method.

## Syntax


```C++
HRESULT Connect(
         IPin          *pReceivePin,
   const AM_MEDIA_TYPE *pmt
);
```



## Parameters

<dl> <dt>

*pReceivePin* 
</dt> <dd>

Pointer to the receiving pin's [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface.

</dd> <dt>

*pmt* 
</dt> <dd>

Pointer to an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure that specifies the media type for the connection.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those in the following table.



| Return code                                                                                                  | Description                                                                        |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | Success.<br/>                                                                |
| <dl> <dt>**VFW\_E\_ALREADY\_CONNECTED**</dt> </dl>    | The pin is already connected.<br/>                                           |
| <dl> <dt>**VFW\_E\_NO\_ACCEPTABLE\_TYPES**</dt> </dl> | Could not find an acceptable media type.<br/>                                |
| <dl> <dt>**VFW\_E\_NOT\_STOPPED**</dt> </dl>          | The filter is active and the pin does not support dynamic reconnection.<br/> |
| <dl> <dt>**VFW\_E\_TYPE\_NOT\_ACCEPTED**</dt> </dl>   | The specified media type is not acceptable.<br/>                             |



 

## Remarks

The *pmt* parameter can be **NULL**. It can also specify a partial media type, with a value of GUID\_NULL for the major type, subtype, or format.

In the base class, this method tests whether the pin is already connected and whether the filter is stopped. It delegates the rest of the connection process to the [**CBasePin::AgreeMediaType**](cbasepin-agreemediatype.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




