---
description: The ReceiveConnection method accepts a connection from another pin. This method implements the IPin::ReceiveConnection method.
ms.assetid: f17e7d93-ac45-4b8a-98c6-0c76ec7117c9
title: CBasePin.ReceiveConnection method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.ReceiveConnection
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePin.ReceiveConnection method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `ReceiveConnection` method accepts a connection from another pin. This method implements the [**IPin::ReceiveConnection**](/windows/desktop/api/Strmif/nf-strmif-ipin-receiveconnection) method.

## Syntax


```C++
HRESULT ReceiveConnection(
   IPin          *pConnector,
   AM_MEDIA_TYPE *pmt
);
```



## Parameters

<dl> <dt>

*pConnector* 
</dt> <dd>

Pointer to the connecting pin's [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface.

</dd> <dt>

*pmt* 
</dt> <dd>

Pointer to an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure that specifies the media type.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those in the following table.



| Return code                                                                                                | Description                                                                        |
|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Success.<br/>                                                                |
| <dl> <dt>**E\_POINTER**</dt> </dl>                  | **NULL** pointer argument.<br/>                                              |
| <dl> <dt>**VFW\_E\_ALREADY\_CONNECTED**</dt> </dl>  | The pin is already connected.<br/>                                           |
| <dl> <dt>**VFW\_E\_NOT\_STOPPED**</dt> </dl>        | The filter is active and the pin does not support dynamic reconnection.<br/> |
| <dl> <dt>**VFW\_E\_TYPE\_NOT\_ACCEPTED**</dt> </dl> | The specified media type is not acceptable.<br/>                             |



 

## Remarks

The output pin calls this method on the input pin. If the input pin returns an error code, the connection fails.

In the base class, this method performs the following steps:

-   Checks whether the pin is already connected.
-   Checks whether the filter is stopped.
-   Calls the [**CBasePin::CheckConnect**](cbasepin-checkconnect.md) method to test whether the connecting pin is suitable.
-   Calls the [**CBasePin::CheckMediaType**](cbasepin-checkmediatype.md) method to test whether the media type is acceptable.

If all of these steps succeed, the method calls the [**CBasePin::CompleteConnect**](cbasepin-completeconnect.md) and [**SetMediaType**](cbasepin-setmediatype.md) methods to complete the connection. These methods store the media type and a pointer to the output pin.

If **CheckConnect** or **CheckMediaType** fail, the base class calls the [**CBasePin::BreakConnect**](cbasepin-breakconnect.md) method to break the connection and then returns an error code from `ReceiveConnection`.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




